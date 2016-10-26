###--- Natalie's Python Pipeline for Processing RAD data ---###
# Pacific Cod Time Series Project #

import subprocess # call module that will run shell scripts from this python script

### (1) - ``process_radtags`` #
# I didn't have to run this on my cod data, so skip this for now and get deets from Mary later #


### (2) - ``ustacks``
# This step aligns identical RAD tags within an individual.
# Input: fastq or gzfastq files
# Output: 4 files - alleles, modules, snps, tags

# ---A) Navigate to the directory to the directory that includes your fastq or gzfastq files and nothing else
# ---B) Produce a shell script that will run ``ustacks`` on all of your files, given desired parameters

from os import listdir
from os.path import isfile, join
onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]





# Simple command
# subprocess.call(['ls'], shell=True)
