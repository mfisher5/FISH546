##########################################################################################
# 
### ``ustacks``
#
# PURPOSE: This step aligns identical RAD tags within an individual into stacks & provides data for calling SNPs
# INPUT: fastq or gzfastq files
# OUTPUT: 4 files - alleles, modules, snps, tags
# 
# 
### WHEN RUNNING THIS SCRIPT, YOUR INPUTS AT THE COMMAND LINE ARE:
# python  
# {0}[pipeline filename] 
# {1}[barcodes & samples textfile] 
# {2}[start directory] 
# {3}[end directory]
# {4}[-m, stacking depth, usually 10]
# {5}[-M, maximum distance allowed between nucleotides, default 2, usually 3]
# {6}[-p, num threads]
# 
### DEPENDENCIES
# 
# [1] You need a file where first column is barcode and second is unique sample name
# 
### WARNINGS
# 
# [1] ustacks only works when your working directory is one direcotry above the folders you are
#		calling and storing data in 
# 
##########################################################################################

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

##########################################################################################
