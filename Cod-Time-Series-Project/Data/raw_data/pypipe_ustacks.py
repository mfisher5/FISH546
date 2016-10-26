###--- Natalie's Python Pipeline for Processing RAD data ---###
# Pacific Cod Time Series Project #


### WHEN RUNNING THIS SCRIPT, YOUR INPUTS ARE
### python  [pipeline filename] [barcodes & samples textfile] [start directory] [end directory]
### python pypipe_ustacks.py barcodes_samplenames.txt raw_data processed_data

# call necessary modules

import subprocess # call module that will run shell scripts from this python script
import sys 


### ``ustacks``

# **PURPOSE*** This step aligns identical RAD tags within an individual
# **Input** fastq or gzfastq files
# **Output** 4 files - alleles, modules, snps, tags



# ---A) Rename your files by the sample name

# you must first make a tab delimited text file where first col = barcode & second col = unique sample name

myfile = open(sys.argv[1], "r")				# myfile =  CSV mentioned, called after your script
new_file = open("new_filenames1.txt", "w") # new txt file
for line in myfile:						   # loop through each line
	linelist=line.strip().split()		   # splits into list by white space
	barcodefile = linelist[0] + "_1.fq.gz"
	# print barcodefile 				   # troubleshooting loop
	samplefile = linelist[1] + "_1.fq.gz"
	# print samplefile 					   # troubleshooting loop
	newstring = "mv" + "\t" + barcodefile + "\t" + samplefile + "\n"
	# print newstring  # troubleshooting loop
	new_file.write(newstring)

myfile.close()
new_file.close()

# change your working directory to the folder that includes with absolute path
subprocess.call(['cd /users/natalielowell/Git-repos/FISH546/Cod-Time-Series-Project/Data/raw_data'], shell=True)

# run the script you just made as a shell script to rename your files
subprocess.call(['sh new_filenames1.txt'], shell=True)



# ---B) Make shell script to run all samples through command line through ``ustacks``

# ``ustacks`` requires an arbitrary integer for every sample, although unclear how it gets used as it does not become the name of the file

# cd to one folder above where you are calling the fq files and one folder above where you are storing your results
subprocess.call(['cd /users/natalielowell/Git-repos/FISH546/Cod-Time-Series-Project/Data/'], shell=True)
dirfrom = sys.argv[2]

ID_int = 001								# start integer counter
for line in new_filenames1.txt: 			#for each line in the barcode file	
	linelist=line.strip().split()	
	sampID = linelist[1] 					#save the second object as "sampID"
	if ID_int < 10: 
		ustacks_code = "ustacks -t gzfasta -f samplesT146/" + sampID + " -r -d -o stacks -i 00" + str(ID_int) + " -m 5 -M 3 -p 10" + "\n"
								#create a line of code for ustacks that includes the new sample ID (with 2 leading 0s)
	elif ID_int >= 10 & ID_int < 100: 
		ustacks_code = "ustacks -t gzfasta -f samplesT146/" + sampID + " -r -d -o stacks -i 0" + str(ID_int) + " -m 5 -M 3 -p 10" + "\n"
								#create a line of code for ustacks that includes the new sample ID (with 1 leading 0)
	else: 
		ustacks_code = "ustacks -t gzfasta -f samplesT146/" + sampID + " -r -d -o stacks -i " + str(ID_int) + " -m 5 -M 3 -p 10" + "\n"
								#create a line of code for ustacks that includes the new sample ID (with no leading 0s)
	newfile.write(ustacks_code)	#append this new line of code to the output file
	ID_int += 1

myfile.close()
newfile.close()












