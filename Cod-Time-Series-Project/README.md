# Cod Time Series Project #

![alt text](https://upload.wikimedia.org/wikipedia/commons/9/96/Gadus_macrocephalus.png)

#### Background 

The Pacific cod (*Gadus macrocephalus*) population in the Salish Sea has significantly diminished since the 1980's, and may have disappeared entirely. A leading hypothesis suggests that these waters were already at the southern-most and warmest extent of their range. Perhaps the waters have warmed enough that Pacific cod have shifted their range to avoid unfavorable conditions.

If warmer temperature is the selection factor that is causing a northward range shift, then a first test of this hypothesis would be to see if cohorts of Pacific cod in the Salish Sea from distinctly hot years demonstrate higher adaptive differentiation than cohorts from distinctly cold temperature regimes. Futher evidence to support this hypothesis would be particular outlier loci sorting with temperature regime, and sorting loci occuring in genes that relate to temperature regulation.

##### Goal 

The goal of this project is to measure adaptive difference within and between cohorts of Pacific cod in the Salish Sea using RADseq data from 2005, 2009, 2010, and 2014. The specific objectives are **(1)** to build loci de novo for each individual, **(2)** assemble a catalog of loci with a subset of individuals to call single nucleotide polymorphisms (SNPs), **(3)** estimate heterozygosity and Fst between cohorts, **(4)** test to see whether particular alleles sort with cohorts associated with particular temperature regimes, and **(5)** if any loci do sort, align them to the Atlantic cod (*Gadus morhua*) genome to see whether these loci occur within genes associated with temperature regulation.

##### The ``Stacks`` pipeline 
Much of the data analysis work will be done using the [``Stacks`` pipeline](http://catchenlab.life.illinois.edu/stacks/). The major programs that make up the milestones of the Stacks pipeline are (1) ``process_radtags``, (2) ``ustacks``, (3) ``cstacks``, (4) ``sstacks``, and (5) ``populations``. In addition, we use ``bowtie`` and ``BLAST`` for filtering our loci, and a custom script for filtering out any non-biallelic loci, or loci with particular minor allele values, etc.

Here's a flow chart that goes through major steps of the the pipeline.

<br>
![image](https://github.com/nclowell/FISH546/blob/master/Cod-Time-Series-Project/Notebooks/images_for_notebooks/Screen%20Shot%202016-12-14%20at%201.02.11%20PM.png?raw=true)

Here are some short descriptions of the different programs in the ``Stacks`` pipeline.

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

``bowtie`` is an alignment program and ``BLAST`` a database search tool. We use these programs to filter out highly repetitive loci, which show up as loci that align or ``BLAST`` to several loci in addition to themselves.

##### Statistics 

Our lab uses Genepop and a collection of R packages to calculate statistics of population differentiation, instead of using the statistics produced by the Stacks pipeline.

Our lab collected environmental data on temperature regimes for the years these samples were collected. I did not have time this quarter to use this data to see whether any outlier loci sort with temperature regime, and whether those loci match to temperature regulation related genes in the Atlantic cod genome. Those would be some next steps.

##### Directory Structure 

Within my class repo FISH546, I have a directory for this project. Within this directory, I made a [directory for **Data**](https://github.com/nclowell/FISH546/tree/master/Cod-Time-Series-Project/Data/metadata) which only includes metadata, because my raw and processed data are too large to push to Git Hub. Metadata includes information on the individual fish, DNA quality, environmental conditions, etc. Processed data is for data that has made it through part of the pipeline. My raw and processed data live on a hard drive, with the raw data in its own directory where it is never altered. 

Within the project directory, I also made a [directory for **Analyses**](https://github.com/nclowell/FISH546/tree/master/Cod-Time-Series-Project/Analyses/fastqc_results). This directory has a directory for fast qc results, which describe the quality of the sequence data. My lab uses R packages to calculate statistics instead of the Stacks pipeline. This is where I will store those results when I produce them. I did not get this far in class, although made some preliminary plots in a notebook [here](https://github.com/nclowell/FISH546/blob/master/Cod-Time-Series-Project/Notebooks/Cod-Time-Series-Project%20Effect%20of%20loci%20number%20on%20DAPC.ipynb).

Within the project directory, I also made a [**Notebooks** directory](https://github.com/nclowell/FISH546/tree/master/Cod-Time-Series-Project/Notebooks) that contains all of my Jupyter notebooks for the project.

Within the project directory, I also made a [**Scripts** directory](https://github.com/nclowell/FISH546/tree/master/Cod-Time-Series-Project/Scripts) for all of the scripts I used in this project. I produced a custom python script for almost every step of the pipeline. Within this folder, there is also a [**Markdown_files_for_scripts** directory](https://github.com/nclowell/FISH546/tree/master/Cod-Time-Series-Project/Scripts/Markdown_files_for_scripts), where I've made interpretive markdown files to explain why and how to use my custom scripts.

#### End of Quarter Progress


<br>
December 14, 2016

At the beginning of the quarter, my biggest goal was to look for differences in adaptive differentiation between cohorts of Pacific cod from Puget Sound. I didn't quite make it that far, but I'm still proud of how far I've come! You can see how much progress I made on my final attempt through the pipeline in this notebook [here](https://github.com/nclowell/FISH546/blob/master/Cod-Time-Series-Project/Notebooks/Cod-Time-Series-Project%20Full%20Pipeline%20%2B%20Bowtie%20%2B%20BLAST%20steps.ipynb).

Last week, I finally made it thorugh ``populations`` on all of my files, and realized that I have very few loci in my genepop file. I had roughly 50,000 loci per individual after ``ustacks``, but was losing them at some point in ``populations``. I couldn't figure out what was happening, so I tested to see how changing certain parameters affected the number of retained loci after ``populations``. It turns out that tweeking the parameters had a very small affect on the number of retained loci. So, I decided it was worth testing whether the individuals I used for my catalog in ``cstacks`` were causing the problem. I reran the pipeline from ``cstacks`` but my new catalog, with individuals from each cohort and inviduals with the most reads, didn't really change the number of retained loci either. After chatting with my lab mates, I realized that it could have had to do with a few individuals that had degraded DNA. I found out which those were, excluded them from the analysis, and my number of retained loci shot up by about 250%. Here's [the notebook](https://github.com/nclowell/FISH546/blob/master/Cod-Time-Series-Project/Notebooks/Cod-Time-Series-Project%20Solving%20low%20retained%20loci%20problem.ipynb) that describes that adventure.

In the tenth week of the quarter, I finally figured out pretty much all of the steps I need to do to get to a solid genepop file that I can use to run statistical tests and answer some of the project's questions. Unfortunately, I still ran into a ton of problems and couldn't run everything through the pipeline by today. One place I got stuck was the final ``bowtie`` step. I misread the instructions for the final ``bowtie`` step, and aligned all of my samples to the reference genome, when I was actually supposed to align each sample separately to the reference genome for feeding into ``pstacks``. This made a huge cumbersome file that slowed me down for a whole day. I figured that out two days ago (and this project is due today!) and realized that I won't have time to rerun ``bowtie`` on each individual and run it through the remainder of the pipeline: ``pstacks``, ``sstacks``, ``populations``, Marine's filtering script, and some sort of stats tests + plots. I had run most of these steps at other times, except for Marine's script and the stats packages. So I figured the best use of my time for the final two days was to learn how to visualize the data, even if it's not my final, most high quality filtered data.

I figured I could at least visualize the genepop file that came out of the first round of populations, when I only included samples that had retained at least 20,000 loci from ``ustacks`` (batch3). But when I tried to make a DAPC plot, I kept getting an error about NAs that prevented me from making the plot. Unfortunately, this wasn't a time where Stack Overflow OR our postdocs could help. To try to get around the problem, I decided to subset my genepop file yesteray, and just grabbed the first 50 loci, and the DAPC worked fine. This morning, I subsetted the first 200 loci, and it worked fine too, and even showed a little more differentiation between cohorts. So, this morning I wrote a quick script for subsetting genepop files because doing it manually was a huge hassle, and impossible after a few hundred loci. Here's a [link to the notebook](https://github.com/nclowell/FISH546/blob/master/Cod-Time-Series-Project/Notebooks/Cod-Time-Series-Project%20Effect%20of%20loci%20number%20on%20DAPC.ipynb) where I documented that adventure, and here's a [link to that script](https://github.com/nclowell/FISH546/blob/master/Cod-Time-Series-Project/Scripts/subset_genepop_nloci.py). It seems like the more loci I'm able to include, the more differentiation shows up between cohorts, suggesting that they probably are a bit different and if I could run my whole genepop, the results would be pretty sweet.

Despite not achieving the end goal, I feel like I've learned a ton on processing RADseq data and am feeling very prepared for my first batch of data-- I just sent off a lane for sequencing last week, so feeling pretty pumped about getting that in a few weeks. In addition to working towards my data analysis on this cod data, I relearned a ton of python scripting and learned a little [bash scripting](https://github.com/nclowell/FISH546/blob/master/Cod-Time-Series-Project/Scripts/check_lib_id.sh), wrote custom [scripts](https://github.com/nclowell/FISH546/tree/master/Cod-Time-Series-Project/Scripts) for most steps of the pipeline, and wrote [markdown files](https://github.com/nclowell/FISH546/tree/master/Cod-Time-Series-Project/Scripts/Markdown_files_for_scripts) that interpret and demonstrate how to use the scripts. And on top of that, I'm glad I finally got the hang of Git Hub and Jupyter Notebooks.


