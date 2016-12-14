##########################################################################################
# 
###--- ``pstacks`` script
#
# PURPOSE: similar to ustacks, except extracts stacks that have been aligned to a genome
# INPUT: either SAM or bowtie reference genome
# OUTPUT: tags, snps, and alleles files like ustacks
# 
#### WHEN RUNNING THIS SCRIPT, INPUTS AT THE COMMAND LINE ARE:
# python 
# {0}[pypipe_pstacks.py] 
# {1}[number of threads]
# {2}[file type, either "sam" or "bowtie"]
# {3}[input file path directory]
# {4}[output path to write results]
# {5}[SQL ID number]
# {6}[minimum depth of coverage to report stack, default = 1]
# {7}[text file with names of SAM files to run pstacks, each on its own new line
#
### DEPENDENCIES: 
# [1] 
# 
### WARNINGS:
# [1] 
# 
##########################################################################################


import sys
import subprocess

namelist = []

names = open(sys.argv[7], "r")
for line in names:
	name = line.strip()
	namelist.append(name)
	
names.close()

string = ""
numnames = int(len(namelist))

for i in range(0,numnames):
	string += "pstacks -p " + sys.argv[1] + " -t " + sys.argv[2] + " -f " + sys.argv[3] + namelist[i] + " -o " + sys.argv[4] + " -i " + sys.argv[5] + " -m " + sys.argv[6] + "\n"
pstacks_shell = open("pstacks_shell.txt", "w")
pstacks_shell.write(string)
pstacks_shell.close()

subprocess.call(["sh pstacks_shell.txt"], shell = True)

print "Finished running pstacks_shell.txt script."

# example text from Eleni's code
# pstacks -p 8 -t sam -f ./aligned/exp1_dam.sam -o ./stacks -i 1 -m 3