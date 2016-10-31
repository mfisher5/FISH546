###--- Natalie's Python Pipeline for Processing RAD data ---###
# Pacific Cod Time Series Project #

#### WHEN RUNNING THIS SCRIPT
## INPUTS: python [txt file with sample names] []

# call necessary modules

import subprocess # call module that will run shell scripts from this python script
import sys 

### ``cstacks``
# **PURPOSE*** ustacks creates a catalog from a subset of individuals to call SNPs
# **Input** ustacks out put files of ~10 individuals ?
# **Output** ?

# ---A) COUNT LINES IN EACH FASTQ FILE. You want to use ~10 individuals to make your 
#		catalog, and you want those individuals to have the most sequence reads. You also
#		want representation from each of your populations. So fist, a script to get line 
#		count for each file.

myfile = open(sys.argv[1], "r")	#open the file with your list of barcodes and sample IDs
newfile = open("cstacks_linecount", "w")	#create a new file where the ustacks code will go
filestring = ""
for line in myfile: 					#for each line in the barcode file
	linelist = line.strip().split()		#make a list of character strings broken by tabs
	sampID = linelist[2]				#pick out file name
	newstring = "zcat " + sampID + " | wc -l >> LineCounts.shell.txt\n" # make line of code to run at command line
	filestring += newstring # add to a list of strings we'll write to a file
myfile.close()
newfile.write(filestring) # write to file
newfile.close()

# run shell script that will calculate line counts
subprocess.call(['LineCounts.shell.txt'], shell=True)
