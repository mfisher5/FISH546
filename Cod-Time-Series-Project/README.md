# Cod Time Series Project #

![alt text](https://upload.wikimedia.org/wikipedia/commons/9/96/Gadus_macrocephalus.png)

#### Background #####

The Pacific cod (*Gadus macrocephalus*) population in the Salish Sea has significantly diminished since the 1980's, and may have disappeared entirely. A leading hypothesis suggests that these waters were already at the southern-most and warmest extent of their range. Perhaps the waters have warmed enough that Pacific cod have shifted their range to avoid unfavorable conditions.

If heat is the selection factor that is causing a northward range shift, then a first test of this hypothesis would be to see if cohorts of Pacific cod in the Salish Sea from distinctly hot years demonstrate higher adaptive differentiation than cohorts from distinctly cold temperature regimes. Futher evidence to support this hypothesis would be particular outlier loci sorting with temperature regime, and sorting loci occuring in genes that relate to temperature regulation.

##### Goal #####

The goal of this project is to measure adaptive difference within and between cohorts of Pacific cod in the Salish Sea using RADseq data from 2005, 2009, 2010, and 2014. The specific objectives are **(1)** to build loci de novo for each individual, **(2)** assemble a catalog of loci with a subset of individuals to call single nucleotide polymorphisms (SNPs), **(3)** estimate heterozygosity and Fst between cohorts, **(4)** test to see whether particular alleles sort with cohorts associated with particular temperature regimes, and **(5)** if any loci do sort, align them to the Atlantic cod (*Gadus morhua*) genome to see whether these loci occur within genes associated with temperature regulation.

##### The Stacks pipeline #####
Much of the data analysis work will be done using the [Stacks pipeline](http://catchenlab.life.illinois.edu/stacks/). The major programs that make up the milestones of the Stacks pipeline are (1) ``process_radtags``, (2) ``ustacks``, (3) ``cstacks``, (4) ``sstacks``, and (5) ``populations``.

``process_radtags`` is a program that renames each file by the barcode of the sample and allows you to filter the data by quality thresholds. The input is a fasta file, and the output is a fastq file. The previous user of my data already ran it through ``process_radtags``.

``ustacks`` is a program that identifies unique loci by matching sequence reads into "stacks." Then, ``ustacks`` allows you to assign a certain number of mismatches which you use to call SNPs within an individual. The input for ``ustacks`` is the fastq file, and the output is 4 files: models, snps, tags, and alleles files.

``cstacks`` is a program that creates a catalog of SNPs that you will use to genotype your data. The input to ``cstacks`` is a subset of your samples' output from ``ustacks``. In our lab group, we choose 10 samples that represent variation (across time or space) and that produced the highest number of sequence reads. The output of ``cstacks`` is 3 files per sample: catalog alleles, catalog tags, and catalog SNPs.

``sstacks`` is a program that produces matches of each sample's reads to the catalog of SNPs. The input is the output of ``cstacks`` and the output is one file of the matches. 

``populations`` is a program that 

I am analyzing this data as part of FISH546 class at the University of Washington. Because I am just familiarizing myself with Stacks now, I I hope to make it through at least **objectives 1-3** by the end of the quarter, and in doing so to create scripts that are clearly annotated and that I can use easily in the future with other RADseq projects. 

##### Directory Structure #####

Within my class repo, I have a directory for this project. Within this directory, I made a directory for **Data** that has directories for raw data, processed data, and  metadata. Raw data is never altered and stored in its own directory to protect it. Metadata includes information on the individual fish, environmental conditions, etc. Processed data is for data that has made it through part of the pipeline. However, my data files are too large so I stored 3 (of ~100) on the Owl server to use in class as an example.

Within the project directory, I also made a directory for **Analyses**. This directory has a directory for fast qc results, which describe the quality of the sequence data. As I make progress working my data through the pipeline, I will make directories here for different types of analyses.

Within the project directory, I also made a **Notebooks** directory that contains all of my Jupyter notebooks for the project, and their checkpoints.

Within the project directory, I also made a **Scripts** directory that will eventually contain any scripts associated with the project. I expect to have a custom script for each stage of the Stacks pipeline by the end of the quarter. 


## Project Timeline & Progress ##

**Week 4 Goal** is it to have a script for running ustacks.

In Week **4** I have made a custom python script for ustacks that can be run at the command line with a few arguments. The script renames files from barcode names to sample names, then creates a shell script to run each sample through the command line, then runs the shell script creating 4 output files per input file. I've also started on making the custom python script for cstacks. These scripts are located in my Scripts directory. It's a lot easier for me to work in a python script than in Jupyter Notebook, so I'm trying to keep those annotated and clean because I know they're not as pretty as the notebook! I'm hoping to put everything in a notebook toward the end so it's more readable to others. I just moved a few sample files of data to the Owl server so that Steven can run the scripts to see how they work, but I haven't yet changed the file path names so that they can work from Owl.

**Week 5 Goal** is to have a script for running cstacks.
