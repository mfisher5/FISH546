##########################################################################################
# 
### ``sstacks``
#
# PURPOSE: 
# INPUT: 
# OUTPUT: 
# 
# 
### WHEN RUNNING THIS SCRIPT, YOUR INPUTS AT THE COMMAND LINE ARE:
# python  
# {0}[pipeline filename] 
# {1}[file with sample names]
# {2}[batch ID number]
# {3}
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

samplenames = open(sys.argv[1], "r") # open file w sample names 
newfile = open("sstacks_shell.txt", "w") # create new file for shell script
filestring = "sstacks -b" + sys.argv[2]






##########################################################################################

### --- DOCUMENTATION FOR SSTACKS
# sstacks -b batch_id -c catalog_file -s sample_file [-s sample_file_2 ...] [-o path] [-p num_threads] [-g] [-x] [-v] [-h]
# p — enable parallel execution with num_threads threads.
# b — MySQL ID of this batch.
# c — TSV file from which to load the catalog loci.
# s — TSV file from which to load sample loci.
# o — output path to write results.
# g — base matching on genomic location, not sequence identity.
# x — don’t verify haplotype of matching locus.
# v — print program version.
# h — display this help messsage.