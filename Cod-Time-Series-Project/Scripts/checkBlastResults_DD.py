# Script written by Dan Drinan April 2016
# this script checks to see that each locus was best aligned to itself. 
# if it best (or equally) aligned to another locus, it will be removed.

# directory: 
# DataAnalysis/scripts
# files: [1]blast input file, [2]fasta file that represents the data after it went through bowtie and got filtered [3] name of fasta file to store good data [4] name of file to store bad data
# python checkBlastResults.py batch_5_bowtieOutput_filtered_blastOutput batch_5_bowtieOutput_filtered.fa batch_5_bowtieOutput_filtered_blastOutput_good.fa batch_5_bowtieOutput_filtered_blastOutput_bad

import sys

blast_results = open(sys.argv[1], 'r')
good_loci = []
bad_loci = []
counter = 1
line = blast_results.readline()

print "\nIdentifying which loci are 'good' and 'bad' based on BLAST alignments..."
while line:
    if len(line.split()) > 0:
        if line.split()[0] == 'Query=': # this means we are at the line that tells us which locus we're examining
        # the layout of the file (at least the important lines) is like this.
        #Query= 3
        #
        #Length=95
        #                                                                      Score     E
        #Sequences producing significant alignments:                          (Bits)  Value
        #
        #  3                                                                    176    3e-45
        #  85142                                                                150    2e-37
        #  35923                                                                150    2e-37
        #  19300                                                                147    2e-36
        # ...
        # Or, sometimes the locus only aligns to 1 locus, which means the lines starting
        # with 85142, 35923, and 19300 wouldn't be there.

            keep_locus = False    
            locus_of_interest = line.split()[1]
            # now we need to proceed over the next few lines to identify the loci and 
            # scores to see which loci best aligned
            line = blast_results.readline()
            line = blast_results.readline()
            line = blast_results.readline()
            line = blast_results.readline()
            line = blast_results.readline()
            if 'No hits found' not in line:
                line = blast_results.readline()
                top_match_name = line.split()[0]
                top_match_score = float(line.split()[1])
                line = blast_results.readline()
                if len(line.split()) > 0: # this means the locus aligned to multiple loci
                    if float(line.split()[1]) < top_match_score and top_match_name == locus_of_interest: # if true the locus was best aligned to itself
                        keep_locus = True
                else:
                    if top_match_name == locus_of_interest: # if true then the locus only aligned to itself
                        keep_locus = True
    
            if keep_locus:
                good_loci.append(locus_of_interest)
            else:
                bad_loci.append(locus_of_interest)

    line = blast_results.readline()

blast_results.close()


# write the good and bad loci out to their respective files
fasta_file = open(sys.argv[2], 'r')
good_file = open(sys.argv[3], 'w')
bad_file = open(sys.argv[4], 'w')

line1 = fasta_file.readline()
line2 = fasta_file.readline()

print "Writing 'good' and 'bad' loci to their respective files..."
while line1:
    if line1[1:-1] in good_loci:
        good_file.write(line1)
        good_file.write(line2)
    elif line1[1:-1] in bad_loci:
        bad_file.write(line1)
        bad_file.write(line2)

    line1 = fasta_file.readline()
    line2 = fasta_file.readline()

fasta_file.close()
good_file.close()
bad_file.close()


# now go through fasta file and write the good loci to a "good" file and the bad loci to a "bad" file







