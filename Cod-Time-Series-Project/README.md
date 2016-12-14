# Cod Time Series Project #

![alt text](https://upload.wikimedia.org/wikipedia/commons/9/96/Gadus_macrocephalus.png)

#### Background #####

The Pacific cod (*Gadus macrocephalus*) population in the Salish Sea has significantly diminished since the 1980's, and may have disappeared entirely. A leading hypothesis suggests that these waters were already at the southern-most and warmest extent of their range. Perhaps the waters have warmed enough that Pacific cod have shifted their range to avoid unfavorable conditions.

If heat is the selection factor that is causing a northward range shift, then a first test of this hypothesis would be to see if cohorts of Pacific cod in the Salish Sea from distinctly hot years demonstrate higher adaptive differentiation than cohorts from distinctly cold temperature regimes. Futher evidence to support this hypothesis would be particular outlier loci sorting with temperature regime, and sorting loci occuring in genes that relate to temperature regulation.

##### Goal #####

The goal of this project is to measure adaptive difference within and between cohorts of Pacific cod in the Salish Sea using RADseq data from 2005, 2009, 2010, and 2014. The specific objectives are **(1)** to build loci de novo for each individual, **(2)** assemble a catalog of loci with a subset of individuals to call single nucleotide polymorphisms (SNPs), **(3)** estimate heterozygosity and Fst between cohorts, **(4)** test to see whether particular alleles sort with cohorts associated with particular temperature regimes, and **(5)** if any loci do sort, align them to the Atlantic cod (*Gadus morhua*) genome to see whether these loci occur within genes associated with temperature regulation.

##### The Stacks pipeline #####
Much of the data analysis work will be done using the [Stacks pipeline](http://catchenlab.life.illinois.edu/stacks/). The major programs that make up the milestones of the Stacks pipeline are (1) ``process_radtags``, (2) ``ustacks``, (3) ``cstacks``, (4) ``sstacks``, and (5) ``populations``.

``process_radtags`` is a program that renames each file by the barcode of the sample and allows you to filter the data by quality thresholds. The input is a fasta file, and the output is a fastq file. The previous user of my data already ran it through ``process_radtags``. My notebook for running ``process_radtags`` on my data is [here](https://github.com/nclowell/FISH546/blob/master/Cod-Time-Series-Project/Notebooks/Cod-Time-Series-Project%20-%20process_radtags.ipynb) and my markdown file to interpret the script is [here](https://github.com/nclowell/FISH546/blob/master/Cod-Time-Series-Project/Scripts/Markdown_files_for_scripts/pypipe_processtags.md).

<br>
![image](http://catchenlab.life.illinois.edu/stacks/manual/process_radtags.png)

<br>

``ustacks`` is a program that identifies unique loci by matching sequence reads into "stacks." Then, ``ustacks`` allows you to assign a certain number of mismatches which you use to call SNPs within an individual. The input for ``ustacks`` is the fastq file, and the output is 4 files: models, snps, tags, and alleles files. My notebook for running ``ustacks`` on my data is [here](https://github.com/nclowell/FISH546/blob/master/Cod-Time-Series-Project/Notebooks/Cod%20Time%20Series%20Project%20-%20ustacks.ipynb).

``cstacks`` is a program that creates a catalog of SNPs that you will use to genotype your data. The input to ``cstacks`` is a subset of your samples' output from ``ustacks``. In our lab group, we choose 10 samples that represent variation (across time or space) and that produced the highest number of sequence reads. The output of ``cstacks`` is 3 files per sample: catalog alleles, catalog tags, and catalog SNPs. My notebook for running ``cstacks`` on my data is [here](https://github.com/nclowell/FISH546/blob/master/Cod-Time-Series-Project/Notebooks/Cod%20Time%20Series%20Project%20-%20cstacks.ipynb).

``sstacks`` is a program that produces matches of each sample's reads to the catalog of SNPs. The input is the output of ``cstacks`` and the output is one file of the matches.

<br>

![image](http://catchenlab.life.illinois.edu/stacks/manual/denovo_pipeline.png)

<br>

``populations`` is a program that produces Fst and heterozygosity estimates, as well as a table of haplotype calls and summary statistics. The input file is the matches file, and the output is two summary statistic files, the haplotype file, and a populations file.

<br>

![image](http://catchenlab.life.illinois.edu/stacks/manual/stacks_pipeline.png)

<br>

In our lab, we run RAD data through this pipeline and then return to ``cstacks`` and change the way the program calls heterozygotes. Then, we rerun ``sstacks`` and ``populations``. We also have several in-house scripts we use to add additional quality filtering to the final genotype calls.

##### Statistics #####

Our lab uses a collection of R packages to calculate statistics of population differentiation, instead of using the statistics produced by the Stacks pipeline.

Our lab collected environmental data on temperature regimes for the years these samples were collected. I will use this data to see whether any outlier loci sort with temperature regime, and whether those loci match to temperature regulation related genes in the Atlantic cod genome.

##### Directory Structure #####

Within my class repo FISH546, I have a directory for this project. Within this directory, I made a directory for **Data** that has directories for raw data, processed data, and  metadata. Raw data is never altered and stored in its own directory to protect it. Metadata includes information on the individual fish, environmental conditions, etc. Processed data is for data that has made it through part of the pipeline. However, after making my directory structure I realized that my data files are too large and that I would never be pushing them to Git Hub, so I stored 3 (of ~100) on the Owl server to use in class as an example.

Within the project directory, I also made a directory for **Analyses**. This directory has a directory for fast qc results, which describe the quality of the sequence data. My lab uses R packages to calculate statistics instead of the Stacks pipeline. This is where I will store those results.

Within the project directory, I also made a **Notebooks** directory that contains all of my Jupyter notebooks for the project, and their checkpoints.

Within the project directory, I also made a **Scripts** directory that will eventually contain any scripts associated with the project. I expect to have a custom script for each stage of the Stacks pipeline by the end of the quarter. Within this folder, there is also a **Markdown_files_for_scripts** directory, where I've made interpretive markdown files to explain why and how to use my custom scripts.

#### End of Quarter Progress

I learned what our whole lab's pipeline is for RADseq data and successfully completed most steps, but was unable to execute them on all of my data by the end of the quarter. 

However, I did still accomplish a lot this quarter. I learned how to use all of the basic programs in the Stacks pipeline (``ustacks``, ``pstacks``, ``cstacks``, ``sstacks``, and ``populations``), learned how to use ``bowtie`` for filtering loci and making alignments, learned how to use ``BLAST`` for filtering loci, relearned a lot of python and learned some bash scripting, wrote python scripts that produce shell scripts and run them for each step, wrote a bash script, solved a problem of few retained loci at the end of ``populations``, and wrote interpretive markdown files for most of my scripts. 

