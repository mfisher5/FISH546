### Running ``cstacks``


##### Purpose

``cstacks`` is a program in the ``Stacks`` pipeline that produces a catalog of loci that you can use later to genotype your individuals. In our lab, we tend to use about 10 individuals, and we pick those that represent as many of our populations as possible and individuals with the most reads as possible.

At first I was hoping to automate the process for picking which inviduals to use in the catalog, but it turns out I haven't wanted that automated every time I've run it. I want to hand pick from certain populations, avoid certain individuals, etc. So I've used this script to produce a sorted list of samples by descending number of reads, and then I manually make a text file with just the ones I'd like to use and stick it back in. I'm sure there could be a way to speed that up but I haven't figured it out yet.

##### Documentation

The most important command line arguments are [i] -b for batch number, [ii] -s for each of the fastq filepaths you want to include in your catalog, [iii] -o for the output filepath, [iv] -n for the number of allowed mismatches, and [v] -p for the number of threads.

Here is more information on the most important arguments for ``cstacks``:

cstacks -b batch_id -s sample_file [-s sample_file_2 ...] [-o path] [-n num] [-g] [-p num_threads] [--catalog path] [-h]
<br>p — enable parallel execution with num_threads threads.
<br>b — MySQL ID of this batch.
<br>s — TSV file from which to load radtags.
<br>o — output path to write results.
<br>m — include tags in the catalog that match to more than one entry.
<br>n — number of mismatches allowed between sample tags when generating the catalog.
<br>g — base catalog matching on genomic location, not sequence identity.
<br>h — display this help messsage.

You can read the Stacks manual entry for ``cstacks`` [here](http://catchenlab.life.illinois.edu/stacks/comp/cstacks.php).

Example Code:

```$	cstacks -b 3 -s stacks_b3/2015_101_1 -s stacks_b3/2005_464_1 -s stacks_b3/2010_184_1 -s stacks_b3/2005_459_1 -o stacks_b3 -n 3 -p 5```

##### Running ``cstacks`` using a custom script

I wrote a script for producing a ``cstacks`` shell and running it. The command line arguments are [i] a text file with the filenames that came out of ``process_radtags``, [ii] the directory of input files, [iii] the number of individuals for your catalog, [iv] batch number, [v] output directory, [vi] number of mismatches allowed, and [vii] number of threads to use.

Example code:

```$	python pypipe_cstacks.py prt_out_filenames.txt stacks_b3 10 3 stacks_b3 3 10```

The meat of the script:

```
### --- [A] Call necessary modules

import sys 
import subprocess





### --- [B] Count lines in each sequence file

myfile = open(sys.argv[1], "r")	# open file w file names that you got from ls > .txt
lines = myfile.readlines()


dirfrom = sys.argv[2] # get directory for input files
firststr = "cd " + sys.argv[2] + "\n" # write first line of shell to cd to this directory

filestring = ""
filestring += firststr

filename_list = [] # to be used in loop later in this script

for line in lines: 					# loop to get file names, and stick into script for counting lines
	filename = line.strip()		
	filename_list.append(filename)
	newstring = "gunzip -c " + filename + " | wc -l >> ../cstacks_linecount.txt\n" # make line of code to run at command line
	filestring += newstring # add to a list of strings we'll write to a file
myfile.close()


#create a new file where the ustacks code will go, write string to file, close
newfile = open("cstacks_linecount_shell.txt", "w")
newfile.write(filestring)
newfile.close()

# run shell script that will calculate line counts
# subprocess.call(['sh cstacks_linecount_shell.txt'], shell=True)




# ### --- [C] Get sample names for specified # of samples with most sequence reads 
# 
linecounts = open("cstacks_linecount.txt", "r") # read in line counts file
linecounts_list = [] # initiate a list for the line counts so I can get.item later

for line in linecounts:
	count = line.strip().split() # get line count
	linecounts_list.append(line)

list_samp_ct = [] # initiate empty list
i = 0 # start counter

    
# len1 = len(filename_list)
# print "The filename list is " + str(len1) + " items long."
# print filename_list
# 
# len1 = len(linecounts_list)
# print "The linecounts list is " + str(len1) + " items long."
# print linecounts_list


for item in linecounts_list:
	new_item = [filename_list[i], linecounts_list[i]]
	list_samp_ct.append(new_item)
	i += 1
	
def getKey(item): # so that sorted will sort by second item in list
	return item[1]
sortedlist = sorted(list_samp_ct, key = getKey, reverse = True)

with open('all_sorted_name_counts.txt', 'w') as file:
	file.writelines('\t'.join(i) + '\n' for i in sortedlist) # makes file



### --- [D] Write and run shell script for ``cstacks``


# ---------
# Picking the individuals to use in cstacks is actually really hard to automate, so I think I will tend to 
# manually make the file of individuals for cstacks. It needs to look like a text file where the first
# column 


samples_for_use = []
foruse = open("files_for_cstacks_b3.txt", "r")
for line in foruse:
	linelist = line.strip().split()
	samples_for_use.append(linelist[0])
foruse.close()


#----------

cstacks_shell = ""
dirstr = "cd " + sys.argv[2] + "\n"
firststr = "cstacks -b " + sys.argv[4] + " "
cstacks_shell += firststr

endrange = int(sys.argv[3]) # set end of range for loop
for i in range(0, endrange):
	filename = samples_for_use[i]
	trmd_filename = filename.rsplit(".",2)[0]
	string = "-s " + sys.argv[2] + "/" + trmd_filename + " "
	cstacks_shell += string
laststr = "-o " + sys.argv[5] + " -n " + sys.argv[6] + " -p " + sys.argv[7]
cstacks_shell += laststr

cstacks_shell_txt = open("cstacks_shell.txt", "w")
cstacks_shell_txt.write(cstacks_shell)
cstacks_shell_txt.close()

# run shell script
subprocess.call(["sh cstacks_shell.txt"], shell = True)

##########################################################################################

```

20161211NL