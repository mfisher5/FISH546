## pypipe_sstacks.py

<br><br>
##### PURPOSE
This script writes a shell script for ``sstacks`` and then runs the shell script. Sstacks matches individual samples against the catalog for genotyping. It will return a match file.

#####WHEN RUNNING THIS SCRIPT, YOUR INPUTS AT THE COMMAND LINE ARE:
python  
{0}[pipeline filename] 
<br>{1}[shell script w sample names]
<br>{2}[batch ID number]
<br>{3}[filepath to directory with catalog filename without file extension]
<br>{4}[filepath to directory w ustacks output files per sample]
<br>{5}[number of threads to use]

```

# --- [A] call necessary modules

import subprocess
import sys 





# --- [B] make shell script for sstacks

trim_names = [] # initiate list

rename_shell = open(sys.argv[1], "r") # open file w filenames 
for line in rename_shell:
	linelist = line.strip().split()
	trim_name = linelist[2].rsplit(".",2)[0]
	trim_names.append(trim_name)
# print trim_names # CHECK^

rename_shell.close()

numsamples = len(trim_names)

newfile = open("sstacks_shell.txt", "w") # create new file for shell script
filestring = "sstacks -b " + sys.argv[2] + " -c " + sys.argv[3]

for i in range(0,numsamples):
	substr = " -s " + sys.argv[4] + "/" + trim_names[i]
	filestring += substr
	
filestring += " -p " + sys.argv[5]
# print filestring # ^CHECK

newfile.write(filestring)
newfile.close()





# --- [C] run shell script for sstacks

subprocess.call(["sh sstacks_shell.txt"], shell=True)





##########################################################################################

# SSTACKS DOCUMENTATION
# p - enable parallel execution with num_threatds threads
# b - MySQL ID of this batch
# c - TSV file from which to load the catalog loci
# s - TSV file from which to load sample loci
# o - output path to write results
# g - base matching on genomic location, not sequence identity
# x - don't verify haplotype of matching locus
# v - print program values
# h - display this help message
```
