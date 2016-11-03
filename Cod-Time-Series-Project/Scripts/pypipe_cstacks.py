###--- Natalie's Python Pipeline for Processing RAD data ---###
# Pacific Cod Time Series Project #

#### WHEN RUNNING THIS SCRIPT
## INPUTS at command line: 
# python 
# {0}[pypipe_cstacks.py] 
# {1}[txt file with sample names] 	
# {2}[wd for data files] 
# {3}[# individuals for cstacks] 
# {4}[batch number] 
# {5}[output directory] 
# {6}[num mismatches allowed] 
# {7}[num threads]

## --- DEPENDENCIES: your file names coming out of ustacks cannot have a period other than before file extension

### ---  Call necessary modules

import sys 
import subprocess # call module that will run shell scripts from this python script

### ``cstacks``
# **PURPOSE*** ustacks creates a catalog from a subset of individuals to call SNPs
# **Input** ustacks out put files of ~10 individuals ?
# **Output** ?



# ---A) COUNT LINES IN EACH FASTQ FILE. You want to use ~10 individuals to make your 
#		catalog, and you want those individuals to have the most sequence reads. You also
#		want representation from each of your populations. So fist, a script to get line 
#		count for each file.

myfile = open(sys.argv[1], "r")	#open the file with your list of barcodes and sample IDs
newfile = open("cstacks_linecount_shell.txt", "w")	#create a new file where the ustacks code will go
line_cd = sys.argv[2]
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
newfile.write(filestring) # write to file
newfile.close()

# run shell script that will calculate line counts
subprocess.call(['sh cstacks_linecount_shell.txt'], shell=True)

# *** if you have to rerun this script, it will append onto it! make sure no file w name!



# ---B) Create a list of lists that has the filename and the number of lines in each 
#		sublist, and then sort in descending order of second sublist item to pick the most 
#		prolific ten individuals. 

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
    



# --- C) Write shell script that will run ``cstacks``

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



 
