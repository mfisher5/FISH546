# How to filter your catalog with ``bowtie`` and ``BLAST``
##### Introduction

Our lab uses additional screening steps to remove repetitive loci and loci with tandem repeats, like microsatellites, from our catalogs we produce in ``cstacks``. These should not be included in our population genomics analyses, and are often not filtered out in the ``Stacks`` pipeline. So, we use ``bowtie`` and ``BLAST`` to filter these out.


To install ``bowtie``, download the software and unzip the folder. You must be in this folder to use the program. Click [here](http://bowtie-bio.sourceforge.net/manual.shtml#the--v-alignment-mode) for the ``bowtie`` manual.

To install ``BLAST``, follow the [instructions on their website](https://blast.ncbi.nlm.nih.gov/Blast.cgi?PAGE_TYPE=BlastDocs&DOC_TYPE=Download). If you would like to be able to call ``BLAST`` from any directory, you can edit your ``.bash_profile`` file. Click [here](https://www.ncbi.nlm.nih.gov/books/NBK279688/) for the ``BLAST`` manual.
<br>
<br>
<br>
## ``bowtie`` filtering

During ``ustacks``, we designate how many mismatches we allow between "identical" matches of reads. Many of use use a mismatch parameter value of 3. Therefore, if a locus aligns to several loci including itself, it likely has a repeat sequence and should be removed from the catalog. To do this, we must [1] build a ``bowtie`` index ("index" is somewhat interchangeable with "database," "catalog," and "reference genome" here) and [2] align our index to itself.

##### [1] Making a fasta file for your ``bowtie`` index

To build a ``bowtie`` index, Mary made a script that creates a fasta file of the tags you would like to include in your index based on the output of ``populations``. You will need the .genepop file and the batch.catalog.tags.tsv file. Open your .genepop file and copy and paste the header that has the names of all of the SNPs (with format number_number, e.g., 4_26,4_140,5_9,8_24...) into a new text file. This will be your first command line argument. Then, unzip your batch.catalog.tags.tsv file. This will be your second command line argument. Afterwards, you can run Mary's [script](https://github.com/nclowell/FISH546/blob/master/Cod-Time-Series-Project/Scripts/genBOWTIEfasta.py). 

Example code:
<br>
<br>
```
$	python genBOWTIEfasta.py ../test_20k_cutoff/batch_3_loci.txt ../test_20k_cutoff/batch_3.catalog.tags.tsv
```
<br>
<br>
This will produce a file called seqsforBOWTIE.fa

##### [2] Building a ``bowtie`` index using ``bowtie-build``

The ``bowtie-build`` command main arguments are [i] a fasta file of sequences that you want to include in your index and [ii] the filename for your index. The index output files are named NAME.1.ebwt, NAME.2.ebwt, NAME.3.ebwt, NAME.4.ebwt, NAME.rev.1.ebwt, and NAME.rev.2.ebwt.


Example code:
<br>
<br>
```
$	./bowtie-build seqsforBOWTIE.fa batch_3
```

##### [3] Aligning our ``bowtie`` index to itself

Use the ``bowtie`` command to align your index to itself. The command line arguments indlude [i] the filetype parameter (here, -f for fasta), [ii] the mismatch paramter -v (here, 3), [iii] the --sam-nohead paramter that creates a SAM file as the alignment filetype output without a header line, [iv] the name of your ``bowtie`` index files (here, batch_3), and [v] the name for your output alignment file.



Example code:
<br>
<br>
```
$	./bowtie -f -v 3 --sam --sam-nohead
batch_3
seqsforBOWTIE.fa
batch_3_BOWTIEout.sam
```


##### [4] Filtering out repetive loci with custom script

Lastly, you will use Dan's custom [script](https://github.com/nclowell/FISH546/blob/master/Cod-Time-Series-Project/Scripts/parseBowtie_DD.py) for parsing the ``bowtie`` results. This script will only retain the loci that did not align to loci other than themselves by rewriting your ``bowtie`` filtered file.

The command line arguments for this script are [i] your ``bowtie`` SAM file and [ii] the fasta file of ``bowtie``-filtered tags that you used to build your ``bowtie`` index.


Example code:
<br>
<br>
```
$	python parseBowtie_DD.py ../Bowtie/bowtie-1.1.2/batch_3_BOWTIEout.sam ../Bowtie/bowtie-1.1.2/batch_3_BOWTIEout_filtered.fa
```
<br>
<br>
<br>
## ``BLAST`` filtering

``BLAST`` searches of your catalog against your catalog using the low-complexity filter implemented in the search tool can be used to filter out loci with repetitive motifs. A ``BLAST`` search of a locus with low complexity against itself will rarely return  a match or might return a match with another sequence. Therefore, we can use ``BLAST`` to parse out bad loci in a similar way to our ``bowtie`` filtering step.

##### [1] Make a ``BLAST`` database using ``bowtie``-filtered file

Use the ``makeblastdb`` command to make your database. The command line arguments are [i] your -in paramter for input file, which is the ``bowtie``-filtered fasta you are using to make your database, [ii] the -parse_seqids flag, which allows you to retrieve sequences using the sequence identifiers, [iii] the -dbtype parameter for database type, which here is nucleotide, and [iv] the -out paramter for output filename for your ``bowtie``-filtered database.

Example code:
<br>
<br>
```
$	makeblastdb -in batch_3_BOWTIEout_filtered.fa
-parse_seqids
-dbtype nucl
-out batch_3_BOWTIEfiltered
```

##### [2] ``BLAST`` query against itself

Use the ``blastn`` command to search the query against itself. The command line arguments are [i] the -query parameter for your ``bowtie``-filtered fasta file, [ii] -db parameter for your database you just made in ``BLAST``, and [iii] -out parameter for the output filename.

Example code:
<br>
<br>
```
$	blastn -query batch_3_BOWTIEout_filtered.fa
-db batch_3_BOWTIEfiltered
-out batch_3_BowtieBlastFiltered
```

##### [3] Filtering out repetitive loci with custom script

Lastly, you will use Dan's custom [script](https://github.com/nclowell/FISH546/blob/master/Cod-Time-Series-Project/Scripts/checkBlastResults_DD.py) for parsing out the repetitive loci. The command line arguments for this script are [i] the ``BLAST`` input file, [ii] the ``bowtie``-filtered fasta file, [iii] output filename for storing "good" data, and [iv] output filename for storing "bad" data.


Example code:
<br>
<br>
```
$	python checkBlastResults_DD.py
../Blast_b3_20k/batch_3_BowtieBlastFiltered
../Blast_b3_20k/batch_3_BOWTIEout_filtered.fa
../Blast_b3_20k/batch_3_BowtieBlastFiltered_GOOD.fa
../Blast_b3_20k/batch_3_BowtieBlastFiltered_BAD.fa
```

This will output a fasta file with only non-repetitive loci. This is what you will use to build your final SAM file to feed into ``pstacks``.

<br>
<br>

## Creating final SAM with ``bowtie``

Now that you have double-filtered out repetitive loci, you need to build your final index, and align your fastq files to it. Then, ``pstacks`` will be able to identify stacks from the alignment.

##### [1] Building your final ``bowtie`` index

Again, the ``bowtie-build`` command main arguments are [i] a fasta file of sequences that you want to include in your index and [ii] the filename for your index. Use your double-filtered fasta to build this index.

Example code:
<br>
<br>
```
$	./bowtie-build batch_3_BowtieBlastFiltered_GOOD.fa batch_3_final_index
```


##### [2] Aligning your fastq files

NOTE: This step is time intensive!

Use ``bowtie-build`` to align your fastq files (from ``process_radtags`` output) to your final ``bowtie`` index. The command line arguments indlude [i] the mismatch paramter -v (here, 3), [ii] the --sam parameter signifying a SAM output file type, [iii] the --sam-nohead paramter that leaves off the header line, [iv] the name of your bowtie index files (here, batch_3), and [v] a list of the filenames for your fasta files separated by comma, and [vi] the output file name. Make sure your fastq files are unzipped. *The --sam and --sam-nohead arguments may be redundant. The example code is from the first time I've tried this, so there may be a more efficient way to do this.

Example code:
<br>
<br>
```
$	./bowtie -v 3 --sam --sam-nohead batch_3_final_index ./fastq_files/2005_297_1.fq,./fastq_files/2005_298_1.fq,./fastq_files/2015_139_1.fq,./fastq_files/2015_140_1.fq batch_3_final.sam
```

I wrote a python [script](https://github.com/nclowell/FISH546/blob/master/Cod-Time-Series-Project/Scripts/final_bowtie_shell.py) to produce the shell script because it can be tedious to list all of the filenames. The command line arguments for this script are [i] text file with each fastq file name on its own line, [ii] number of mismatches allowed, usually 3, [iii] doube-filtered ``bowtie`` index name, and [iv] output filename path. Make sure your file names call the unzipped files.

Example code:
<br>
<br>
```
$	python final_bowtie_shell.py prt_out_filenames_20k.txt 3 batch_3_final_index batch_3_final.sam
```

This will spit out a SAM file that you can feed into ``pstacks``.

<br>
<br>

### Helpful Reference
[Brieuc, M. S., Waters, C. D., Seeb, J. E., & Naish, K. A. (2014). A dense linkage map for Chinook salmon (Oncorhynchus tshawytscha) reveals variable chromosomal divergence after an ancestral whole genome duplication event. G3: Genes| Genomes| Genetics, 4(3), 447-460.](http://www.g3journal.org/content/4/3/447.full)

<br>
<br>
20161211NL



