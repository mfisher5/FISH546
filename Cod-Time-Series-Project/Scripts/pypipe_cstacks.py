##########################################################################################
# 
###--- ``cstacks`` script
#
# PURPOSE: ustacks creates a catalog from a subset of individuals to call SNPs
# INPUT: ustacks out put files for specified number of individuals with most sequence reads
# OUTPUT: catalog file + associated files
# 
#### WHEN RUNNING THIS SCRIPT, INPUTS AT THE COMMAND LINE ARE:
# python 
# {0}[pypipe_cstacks.py] 
# {1}[shell script with changed file names] 	
# {2}[directory of input files] 
# {3}[# individuals for cstacks] 
# {4}[batch number] 
# {5}[output directory] 
# {6}[num mismatches allowed] 
# {7}[num threads]
# 
### DEPENDENCIES: 
# [1] Your file names coming out of ustacks cannot have a period other than before file extension (not sure if true! check?)
# 
### WARNINGS:
# [1] If you have to rerun this script, it will append onto it! make sure no file w name or else won't even run!
# 
##########################################################################################

### --- [A] Call necessary modules

import sys 
import subprocess





### --- [B] Count lines in each sequence file

myfile = open(sys.argv[1], "r")	#open the file with your list of barcodes and sample IDs

dirfrom = sys.argv[2] # get directory for input files
firststr = "cd " + "sys.argv[2]" + "\n" # write first line of shell to cd to this directory

filestring = ""
samplename_list = [] # to be used in loop later in this script

for line in myfile: 					#for each line in the barcode file
	linelist = line.strip().split()		#make a list of character strings broken by tabs
	sampID = linelist[2]				#pick out file name
	samplename_list.append(sampID)
	newstring = "gunzip -c " + sampID + " | wc -l >> cstacks_linecount.txt\n" # make line of code to run at command line
	filestring += newstring # add to a list of strings we'll write to a file
myfile.close()
# print filestring # CHECK^


filestring = firststr + filestring # write cd line before rest of file string

#create a new file where the ustacks code will go, write string to file, close
newfile = open("cstacks_linecount_shell.txt", "w")
newfile.write(filestring)
newfile.close()

# run shell script that will calculate line counts
subprocess.call(['sh cstacks_linecount_shell.txt'], shell=True)





### --- [C] Get sample names for specified # of samples with most sequence reads 

linecounts = open("cstacks_linecount.txt", "r") # read in line counts file
linecounts_list = [] # initiate a list for the line counts so I can get.item later

for line in linecounts:
	count = line.strip().split() # get line count
	linecounts_list.append(line)

list_samp_ct = [] # initiate empty list
i = 0 # start counter

# --- CHECK^ if lists look normal
# print "sample name list "
# print samplename_list
# print "line counts list "
# print linecounts_list

for item in linecounts_list:
	new_item = [samplename_list[i], linecounts_list[i]]
	list_samp_ct.append(new_item)
	i += 1
	
def getKey(item): # so that sorted will sort by second item in list
	return item[1]
sortedlist = sorted(list_samp_ct, key = getKey, reverse = True)
# print sortedlist # CHECK^

with open('all_sorted_name_counts.txt', 'w') as file:
    file.writelines('\t'.join(i) + '\n' for i in sortedlist) # makes file
    




### --- [D] Write and run shell script for ``cstacks``

cstacks_shell = ""
firststr = "cstacks -b " + sys.argv[4] + " "
cstacks_shell += firststr

endrange = int(sys.argv[3]) # set end of range for loop
for i in range(0, endrange):
	filename = samplename_list[i]
	trmd_filename = filename.rsplit(".",2)[0]
	# print trmd_filename # CHECK^
	string = "-s " + trmd_filename + " "
	cstacks_shell += string
laststr = "-o " + sys.argv[5] + " -n " + sys.argv[6] + " -p " + sys.argv[7]
cstacks_shell += laststr
# print cstacks_shell # CHECK^

cstacks_shell_txt = write("cstacks_shell.txt", "w")
cstacks_shell_txt.write(cstacks_shell)
cstacks_shell_txt.close()

# run shell script
subprocess.call(["cstacks_shell.txt"], shell = True)

##########################################################################################

### --- DOCUMENTATION FOR CSTACKS

# cstacks -b batch_id -s sample_file [-s sample_file_2 ...] [-o path] [-n num] [-g] [-p num_threads] [--catalog path] [-h]
# p — enable parallel execution with num_threads threads.
# b — MySQL ID of this batch.
# s — TSV file from which to load radtags.
# o — output path to write results.
# m — include tags in the catalog that match to more than one entry.
# n — number of mismatches allowed between sample tags when generating the catalog.
# g — base catalog matching on genomic location, not sequence identity.
# h — display this help messsage.
# Catalog editing:
# 
# --catalog [path] — provide the path to an existing catalog. cstacks will add data to this existing catalog.
# Advanced options:
# 
# --report_mmatches — report query loci that match more than one catalog locus.
