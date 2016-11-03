###--- Natalie's Python Pipeline for Processing RAD data ---###
# Pacific Cod Time Series Project #


### WHEN RUNNING THIS SCRIPT, YOUR INPUTS AT THE COMMAND LINE ARE:
# python  
# {1}[pipeline filename] 
# {2}[barcodes & samples textfile] 
# {3}[start directory] 
# {4}[end directory]

# Example: python pypipe_ustacks.py barcodes_samplenames.txt raw_data processed_data

# --- call necessary modules

import subprocess
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

# name your 'from' and 'to' directories that will go in each line of your ustacks shell script
dirfrom = sys.argv[2]
dirto = sys.argv[3]


newfile = open("ustacks_shell.txt", "w")	 # make ustacks shell script to run through terminal
myfile = open("new_filenames1.txt", "r")	#open the file with a list of barcodes + sample IDs

newfile.write('cd /users/natalielowell/Git-repos/FISH546/Cod-Time-Series-Project/Data/' + '\n')
ID_int = 001								# start integer counter
for line in myfile: 			#for each line in the barcode file	
	linelist=line.strip().split()	
	sampID = linelist[2] 					#save the second object as "sampID"
	if ID_int < 10: 
		ustacks_code = "ustacks -t gzfastq -f " + dirfrom + "/" + sampID + " -r -d -o " + dirto + " -i 00" + str(ID_int) + " -m 5 -M 3 -p 10" + "\n"
								#create a line of code for ustacks that includes the new sample ID (with 2 leading 0s)
	elif ID_int >= 10 & ID_int < 100: 
		ustacks_code = "ustacks -t gzfastq -f " + dirfrom + "/" + sampID + " -r -d -o " + dirto + " -i 0" + str(ID_int) + " -m 5 -M 3 -p 10" + "\n"
								#create a line of code for ustacks that includes the new sample ID (with 1 leading 0)
	else: 
		ustacks_code = "ustacks -t gzfastq -f " + dirfrom + "/" + sampID + " -r -d -o " + dirto + " -i " + str(ID_int) + " -m 5 -M 3 -p 10" + "\n"
								#create a line of code for ustacks that includes the new sample ID (with no leading 0s)
	newfile.write(ustacks_code)	#append this new line of code to the output file
	ID_int += 1

myfile.close()
newfile.close()

# run this new script through the terminal
subprocess.call(['sh ustacks_shell.txt'], shell=True)



### --- DOCUMENTATION FOR USTACKS
# ustacks -t file_type -f file_path [-d] [-r] [-o path] [-i id] [-m min_cov] [-M max_dist] [-p num_threads] [-R] [-H] [-h]
# t — input file Type. Supported types: fasta, fastq, gzfasta, or gzfastq.
# f — input file path.
# o — output path to write results.
# i — SQL ID to insert into the output to identify this sample.
# m — Minimum depth of coverage required to create a stack (default 2).
# M — Maximum distance (in nucleotides) allowed between stacks (default 2).
# N — Maximum distance allowed to align secondary reads to primary stacks (default: M + 2).
# R — retain unused reads.
# H — disable calling haplotypes from secondary reads.
# p — enable parallel execution with num_threads threads.
# h — display this help messsage.
# Stack assembly options:
# 
# r — enable the Removal algorithm, to drop highly-repetitive stacks (and nearby errors) from the algorithm.
# d — enable the Deleveraging algorithm, used for resolving over merged tags.
# --max_locus_stacks [num] — maximum number of stacks at a single de novo locus (default 3).
# --k_len [len] — specify k-mer size for matching between alleles and loci (automatically calculated by default).
# Gapped assembly options:
# 
# --gapped — preform gapped alignments between stacks.
# --max_gaps — number of gaps allowed between stacks before merging (default: 2).
# --min_aln_len — minimum length of aligned sequence in a gapped alignment (default: 0.80).
# Model options:
# 
# --model_type [type] — either 'snp' (default), 'bounded', or 'fixed'
# For the SNP or Bounded SNP model:
# --alpha [num] — chi square significance level required to call a heterozygote or homozygote, either 0.1, 0.05 (default), 0.01, or 0.001.
# For the Bounded SNP model:
# --bound_low [num] — lower bound for epsilon, the error rate, between 0 and 1.0 (default 0).
# --bound_high [num] — upper bound for epsilon, the error rate, between 0 and 1.0 (default 1).
# For the Fixed model:
# --bc_err_freq [num] — specify the barcode error frequency, between 0 and 1.0.











