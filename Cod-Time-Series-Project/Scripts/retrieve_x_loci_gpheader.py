# Natalie Lowell 20161214
# Purpose: to retrieve a subset of the loci in the header of a genepop file, e.g., if you're subsetting the file
# Command line arguments:
# Assumes the second line of your file is the header with the loci names, split by commas

import sys

popgenfile = open(sys.argv[1], "r")
lines = popgenfile.readlines()
popgenfile.close()

header_list = lines[1].strip().split(",")
retrieve_header = header_list[0:205]

finalstring = ""

for item in retrieve_header:
	finalstring += item + ","
	
	
finallength = len(finalstring.split(","))
	
print "Your final string looks like " + finalstring

print "And your final header will have " + str(finallength) + " loci."

