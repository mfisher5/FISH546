# Natalie Lowell 20161214
# Purpose: Count the number of columns of genotypes in a popgen file.
# command line argument 1 = popgen file
# assumes line 3 is your first sample

import sys

popgenfile = open(sys.argv[1], "r")
lines = popgenfile.readlines()
popgenfile.close()

length = len(lines[2].strip().split())

print "Your genepop file has " + str(length) + " columns of genotypes."


	