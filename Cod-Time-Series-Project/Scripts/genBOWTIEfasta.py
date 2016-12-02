import sys
batchFile = open(sys.argv[1], "r") #file with the comma-delimited list of loci from genepop

#read row of loci names into a string
Filestring = batchFile.read()
batchFile.close()

#identify the unique loci
lociList = Filestring.split(",")
UniqueLoci = []
for locus in lociList:
	templocus = locus.split("_")
	if templocus[0] not in UniqueLoci:
		UniqueLoci.append(templocus[0])



#open the UNZIPPED catalog file
catalog = open(sys.argv[2], "r")


#extract the sequences from the catalog file
fasta = ""
for line in catalog: 
	linelist = line.strip().split()
	if linelist[2] in UniqueLoci: 
		newline = ">"+linelist[2]+"\n"+linelist[8]+"\n"
		fasta += newline
catalog.close()


#open a new file to write into 
newfile = open("seqsforBOWTIE.fa", "w")
newfile.write(fasta)
newfile.close()

