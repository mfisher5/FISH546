###--- Natalie's Python Pipeline for Processing RAD data ---###
# Pacific Cod Time Series Project #

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
	barcodefile = linelist[0] + "_1.fa.gz"
	# print barcodefile 				   # troubleshooting loop
	samplefile = linelist[1] + "_1.fa.gz"
	# print samplefile 					   # troubleshooting loop
	newstring = "mv" + "\t" + barcodefile + "\t" + samplefile + "\n"
	# print newstring  # troubleshooting loop
	new_file.write(newstring)
myfile.close()
new_file.close()

# change your working directory to the folder that includes with absolute path
subprocess.call(['cd /users/natalielowell/Git-repos/FISH546/Cod-Time-Series-Project/Data/raw_data'], shell=True)

# run the script you just made as a shell script to rename your files
subprocess.call(['pwd'], shell=True)









# ---B) Produce a shell script that will run ``ustacks`` on all of your files, given desired parameters








# Simple command
# subprocess.call(['ls'], shell=True)
