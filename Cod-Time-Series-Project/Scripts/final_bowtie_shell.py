##########################################################################################
# 
###--- ``final bowtie`` script
#
# PURPOSE: align fastq files to bowtie index to feed into pstacks
# INPUT: bowtie index and fasta files of sequences to align
# OUTPUT: SAM alignment
# 
#### WHEN RUNNING THIS SCRIPT, INPUTS AT THE COMMAND LINE ARE:
# python 
# {0}[pypipe_pstacks.py] 
# {1}[file with fastq filenames, here prt_out_filenames.txt]
# {2}[number of mismatches allowed, usually 3]
# {3}[bowtie index name]
# {4}[filepath for output file]
### DEPENDENCIES: 
# [1] you want a SAM file without the header line
# [2] you're reading in fastq files
# 
### WARNINGS:
# [1] 
# 
##########################################################################################


import sys
import subprocess

namestring = ""
namelist = [] # for counting how many names we have

filenames = open(sys.argv[1], "r")

for line in filenames:					# loop that gets file names out of a text file, separated by comma with no spaces
	name = line.strip()
	name = name[:-3] # removes ".gz" because we're working with unzipped fastq files
	namestring += "./fastq_files/" + name + ","
	namelist.append(name)
	
namestring = namestring[:-1] # remove final comma

namelist_len = len(namelist)
print "You are working with " + str(namelist_len) + " files. Consider checking your code if you expected a different number of files." # print notice of how many filenames you counted, just to verify.

stringforfile = "./bowtie -v " + sys.argv[2] + " --sam --sam-nohead " + sys.argv[3] +  " " + namestring + " " + sys.argv[4] # write string for shell script

final_bowtie_shell = open("final_bowtie_shell.txt", "w") # open new file for writing shell script
final_bowtie_shell.write(stringforfile)
final_bowtie_shell.close()

subprocess.call(["sh final_bowtie_shell.txt"], shell = True) # run shell script
	