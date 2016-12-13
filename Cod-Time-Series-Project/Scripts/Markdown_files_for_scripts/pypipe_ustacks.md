## Running ``ustacks``


##### Purpose
``ustacks`` is a program within the ``Stacks`` pipeline that takes fastq files and aligns identical reads to find tags and call SNPs. ``ustacks`` is used instead of ``pstacks`` when you do not have a reference genome. In our lab, we use ``ustacks`` to help create a de novo reference genome. Later, we rerun through the ``Stacks`` pipeline and use ``pstacks`` instead with a filtered and trusted catalog that we use as our reference genome.

##### Documentation

The most important command line arguments are [i] the -r

Here is more information on most of the important arguments in ``ustacks`` here:

ustacks -t file_type -f file_path [-d] [-r] [-o path] [-i id] [-m min_cov] [-M max_dist] [-<br>p num_threads] [-R] [-H] [-h]
<br>t — input file Type. Supported types: fasta, fastq, gzfasta, or gzfastq.
<br>f — input file path.
<br>o — output path to write results.
<br>i — SQL ID to insert into the output to identify this sample.
<br>m — Minimum depth of coverage required to create a stack (default 2).
<br>M — Maximum distance (in nucleotides) allowed between stacks (default 2).
<br>N — Maximum distance allowed to align secondary reads to primary stacks (default: M + 2).
<br>R — retain unused reads.
<br>H — disable calling haplotypes from secondary reads.
<br>p — enable parallel execution with num_threads threads.
<br>h — display this help messsage.

You can read the Stacks manual entry for ``ustacks`` [here](http://catchenlab.life.illinois.edu/stacks/comp/ustacks.php).

##### Example Code

``$	ustacks -t gzfasta -f samplesT142/PO010715_06.1.fa.gz -r -d -o stacks -i 001 -m 5 -M 3 -p 6 ``

##### Running ``ustacks`` using a custom script

I wrote a python script that will make a ``ustacks`` shell and run it. The command line arguments are [i] a text file with barcodes and sample names, with each match on its own line separated by white space, [2] your directory with the files you want to run ``ustacks`` on, [iii] the directory you want the output files to be stored in, [iv] the value for parameter -m, stacking depth, usually 10, [v] the value for parameter -M, max distance, usually 3, and [vi] the value for the parameter -p, the number of threads to use.

Example code:
<br>
```
$ python pypipe_ustacks.py barcodes_samplenames.txt ./process_radtags_out ./ustacks_out
```
<br>
<br>
The meat of the script:

```
# --- [A] call necessary modules

import subprocess
import sys 





# --- [B] Rename your files by the sample name

new_file = open("new_filenames_shell.txt", "w") # new txt file
dir = sys.argv[2] # directory files that need names changed
firststr = "cd " + dir + "\n" + "pwd\n"
new_file.write(firststr)

myfile = open(sys.argv[1], "r")				# myfile =  tab delimited file mentioned, called after your script

for line in myfile:						   # loop through each line
	linelist=line.strip().split()		   # splits into list by white space
	barcodefile1 = linelist[0] + "_1.fq.gz" # forward
	barcodefile2 = linelist[0] + "_2.fq.gz" # reverse
	samplefile1 = linelist[1] + "_1.fq.gz" # forward
	samplefile2 = linelist[1] + "_2.fq.gz" # reverse
	newstring = "mv" + "\t" + barcodefile1 + "\t" + samplefile1 + "\n" + "mv" + "\t" + barcodefile2 + "\t" + samplefile2 + "\n"
	# print newstring  # troubleshooting loop
	new_file.write(newstring)

myfile.close()
new_file.close()

# run the script you just made as a shell script to rename your files
subprocess.call(['sh new_filenames_shell.txt'], shell=True)

 



### --- [C] Make shell script to run all samples through command line through ``ustacks``

# ``ustacks`` requires an arbitrary integer for every sample, although unclear how it gets used as it does not become the name of the file


# name your 'from' and 'to' directories that will go in each line of your ustacks shell script
dirfrom = sys.argv[2]
dirto = sys.argv[3]

newfile2 = open("ustacks_shell.txt", "w")	 # make ustacks shell script to run through terminal
myfile = open("new_filenames_shell.txt", "r")	#open the file with a list of barcodes + sample IDs

# dir = sys.argv[2] # directory files that need names changed
# firststr = "cd " + dir + "\n"
# new_file.write(firststr)

dir2 = sys.argv[2] # directory with files that we want to run ustacks on

ID_int = 001								# start integer counter

lines = myfile.readlines()[2:] # skip first two lines because just cd and pwd


ID_int = 001								# start integer counter
for line in lines: 			#for each line in the barcode file	
	linelist=line.strip().split()	
	sampID = linelist[2] 					#save the second object as "sampID"
	if ID_int < 10: 
		ustacks_code = "ustacks -t gzfastq -f " + dirfrom + "/" + sampID + " -r -d -o " + dirto + " -i 00" + str(ID_int) + " -m " + sys.argv[4] + " -M " + sys.argv[5] + " -p " + sys.argv[6] + "\n"
								#create a line of code for ustacks that includes the new sample ID (with 2 leading 0s)
	elif ID_int >= 10 & ID_int < 100: 
		ustacks_code = "ustacks -t gzfastq -f " + dirfrom + "/" + sampID + " -r -d -o " + dirto + " -i 0" + str(ID_int) + " -m " + sys.argv[4] + " -M " + sys.argv[5] + " -p " + sys.argv[6] + "\n"
								#create a line of code for ustacks that includes the new sample ID (with 1 leading 0)
	else: 
		ustacks_code = "ustacks -t gzfastq -f " + dirfrom + "/" + sampID + " -r -d -o " + dirto + " -i " + str(ID_int) + " -m " + sys.argv[4] + " -M " + sys.argv[5] + " -p " + sys.argv[6] + "\n"
								#create a line of code for ustacks that includes the new sample ID (with no leading 0s)
	newfile2.write(ustacks_code)	#append this new line of code to the output file
	ID_int += 1

myfile.close()
newfile2.close()

# run this new script through the terminal
subprocess.call(['sh ustacks_shell.txt'], shell=True)

```

