##########################################################################################
# 
### ``sstacks``
#
# PURPOSE: To match individual samples against your catalog for genotyping
# INPUT: TSV output files from cstacks
# OUTPUT: match files
# 
# 
### WHEN RUNNING THIS SCRIPT, YOUR INPUTS AT THE COMMAND LINE ARE:
# python  
# {0}[pipeline filename] 
# {1}[shell script w sample names]
# {2}[batch ID number]
# {3}[filepath to directory with catalog filename without file extension]
# {4}[filepath to directory w ustacks output files per sample]
# {5}[number of threads to use]
# 
### DEPENDENCIES
# 
# [1]
# 
### WARNINGS
# 
# [1] 
# 
##########################################################################################

# --- [A] call necessary modules

import subprocess
import sys 





# --- [B] make shell script for sstacks

trim_names = [] # initiate list

rename_shell = open(sys.argv[1], "r") # open file w filenames 
lines = rename_shell.readlines()[2:]

for line in lines:
	linelist = line.strip().split()
	trim_name = linelist[2].rsplit(".",2)[0]
	trim_names.append(trim_name)
# print trim_names # CHECK^

rename_shell.close()

numsamples = len(trim_names)

newfile = open("sstacks_shell.txt", "w") # create new file for shell script

filestring = ""

for i in range(0,numsamples):
	filestring += "sstacks -b " + sys.argv[2] + " -c " + sys.argv[3]
	substr = " -s " + sys.argv[4] + "/" + trim_names[i] + " -p " + sys.argv[5] + "\n"
	filestring += substr	

# print filestring # ^CHECK

newfile.write(filestring)
newfile.close()





# --- [C] run shell script for sstacks

subprocess.call(["sh sstacks_shell.txt"], shell=True)

