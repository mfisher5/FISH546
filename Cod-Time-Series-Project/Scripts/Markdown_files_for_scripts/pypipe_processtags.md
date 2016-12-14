##pypipe_processtags.py 

<br><br>
##### Purpose
This script is for making directories you will need to store files after each milestone in the Stacks pipeline. In addition, it will run ``process_radtags`` on a given raw file from the sequencing center.

Note! I wrote this file before I had a lot of experience running the ``Stacks`` pipeline, and now I prefer keeping all of my outputs of the Stacks steps in one folder. Adjust as you see fit.


Command line arguemnts are 
{0}[name of script file]
<br>{1}[number of files you'll be running through process_radtags]
<br>{2}[directory with raw sequence files]
<br>{3}[input sequence file type]
<br>{4}[output sequence file type]
<br>{5}[directory for output files]
<br>{6}[filepath to text file with barcodes]
<br>{7}[length to trim sequences based on fastqc results]

##### Outputs
Named directories and a group of sequence files (you determine file type) that is demultiplexed,trimmed, and cleaned

##### Assumptions and Dependencies
[1] You want the following # and names of directories
<br>[2] You used restriction enzyme sbf1
<br>[3] You have quality scores encoded with Phred33
<br>[4] You want to rescue barcodes and RAD-Tags (-r)
<br>[5] You want to clean data, remove any read with an uncalled base (-c)
<br>[6] You want to discard reads with low quality scores (-q)

```
# [A] call necessary modules

import sys
import subprocess





# [B] make necessary directories for whole project

# name your directories
dir1 = "post-fastqc"
dir2 = "post-ustacks"
dir3 = "post-cstacks"
dir4 = "post-stacks"
dir5 = "post-re-cstacks"
dir6 = "post-extra-filtering"
dir7 = "final-files"
dirlist = [dir1, dir2, dir3, dir4, dir5, dir6, dir7] # make into list

# open text file for shell script, make string that will be written to the file
newfile = open("make_proj_dirs.txt", "w")
str_for_file = ""

for i in range(0, len(dirlist)):
	dirname = dirlist[i]
	tempstr = "mkdir " + dirname + "\n"
	str_for_file += tempstr

newfile.write(str_for_file) # write string to file
newfile.close() # close file

# run shell script to make directories	
subprocess.call(['sh make_proj_dirs.txt'], shell=True)





# --- [C] process_radtags

str_for_prt_file = "process_radtags -p " + sys.argv[2] + " -P  -i " + sys.argv[3] + " -y " + sys.argv[4] + " -o " + sys.argv[5] + " -b " + sys.argv[6] + " -e sbfI -E phred33 -r -c -q -t " + sys.argv[7]

prt_file = open("process_radtags.txt", "w")
prt_file.write(str_for_prt_file)
prt_file.close()




# --- DOCUMENTATION FOR PROCESS_RADTAGS
# 
#  process_radtags [-f in_file | -p in_dir [-P] [-I] | -1 pair_1 -2 pair_2] -b barcode_file -o out_dir -e enz 
# 
#                 [-c] [-q] [-r] [-t len] [-D] [-w size] [-s lim] [-h]
# f — path to the input file if processing single-end seqeunces.
# i — input file type, either 'bustard' for the Illumina BUSTARD format, 'bam', 'fastq' (default), or 'gzfastq' for gzipped FASTQ.
# y — output type, either 'fastq', 'gzfastq', 'fasta', or 'gzfasta' (default is to match the input file type).
# p — path to a directory of files.
# P — files contained within directory specified by '-p' are paired.
# I — specify that the paired-end reads are interleaved in single files.
# 1 — first input file in a set of paired-end sequences.
# 2 — second input file in a set of paired-end sequences.
# o — path to output the processed files.
# b — path to a file containing barcodes for this run.
# c — clean data, remove any read with an uncalled base.
# q — discard reads with low quality scores.
# r — rescue barcodes and RAD-Tags.
# t — truncate final read length to this value.
# E — specify how quality scores are encoded, 'phred33' (Illumina 1.8+, Sanger, default) or 'phred64' (Illumina 1.3 - 1.5).
# D — capture discarded reads to a file.
# w — set the size of the sliding window as a fraction of the read length, between 0 and 1 (default 0.15).
# s — set the score limit. If the average score within the sliding window drops below this value, the read is discarded (default 10).
# h — display this help messsage.
```

20161214NL
