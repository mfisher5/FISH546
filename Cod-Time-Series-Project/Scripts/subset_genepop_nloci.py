# Natalie Lowell 20161214
# Purpose of script: subset a genepop file to a certain number of loci
# Command line arguments: [1] genepop file and [2] number of loci to subset

import sys

n = int(sys.argv[2]) + 1 # add 1 because the first column is just the same of the 

# open your genepop file and read lines into a list of lines
gpfile = open(sys.argv[1], "r") 
lines = gpfile.readlines()
gpfile.close()

# open new file for your output file, the truncated genepop file
newfilename = "genepop_"+str(sys.argv[2])+"_loci.gen"
newfile = open(newfilename, "w")

# write the header line with stacks version and date to the new file
newfile.write(lines[0])

# get header and split into list on commas, for a list of all the loci
header_list = lines[1].strip().split(",")

# grab only the first n, as designated at the command line
retrieve_header = header_list[0:int(sys.argv[2])]


# initiate string for header line w loci
headerstring = "" 

# make a loop to stick the commas back in
for locus in retrieve_header:
	headerstring += locus + ","
	
	
# remove the last comma
headerstring = headerstring[:-1]
headerstring = headerstring + "\n"

# print headerstring # CHECK
	
# write it to the file
newfile.write(headerstring)

# remaining lines = after header w loci
remlines = lines[2:]

# loop: if pop, write pop. if not pop, truncate line to n and add to file
for line in remlines:
	if "pop" in line:
		newfile.write(line)
	else:
		linelist = line.strip().split()
		keep = linelist[0:n] # TESTING THIS LINE
		newline = ""
		for item in keep:
			newline += item + "\t"
		newline = newline[:-1] # remove final tab
		newline = newline + "\n" # add new line
		newfile.write(newline)

newfile.close()
			