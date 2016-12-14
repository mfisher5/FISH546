##########################################################################################
# 
###--- ``cstacks`` script
#
# PURPOSE: ustacks creates a catalog from a subset of individuals to call SNPs
# INPUT: ustacks out put files for specified number of individuals with most sequence reads
# OUTPUT: catalog file + associated files
# 
#### WHEN RUNNING THIS SCRIPT, INPUTS AT THE COMMAND LINE ARE:
# python 
# {0}[pypipe_cstacks.py] 
# {1}[text file with names of files that came out of process rad tags] 	
# {2}[directory of input files, after process rad tags] 
# {3}[# individuals for cstacks] 
# {4}[batch number] 
# {5}[output directory] 
# {6}[num mismatches allowed] 
# {7}[num threads]
# 
### DEPENDENCIES: 
# [1] Your file names coming out of ustacks cannot have a period other than before file extension (not sure if true! check?)
# 
### WARNINGS:
# [1] If you have to rerun this script, it will append onto it! make sure no file w name or else won't even run!
# 
##########################################################################################

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
