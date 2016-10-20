# Cod Time Series Project #

![alt text](https://upload.wikimedia.org/wikipedia/commons/9/96/Gadus_macrocephalus.png)

### General Description ###

Pacific cod (*Gadus macrocephalus*) are no longer found in Puget Sound, and one leading hypothesis as to why is that these waters were already at the southern-most and warmest extent of their range. Perhaps the waters have warmed enough that Pacific cod have shifted their range to avoid unfavorable conditions.

A first test of this hypothesis would be to see if different cohorts of Pacific cod from years with distinctly different temperature regimes demonstrate adaptive differences, with some of these differences in loci associated with temperature regulation and metabolism genes and alleles sorting in cohorts by the differences in environmental conditions. 

The **goal** of this project is to measure these differences using RADseq data on cohorts of cod from the Salish Sea from 2005, 2009, 2010, and 2014. The specific objectives are **(1)** to build loci de novo for each individual, **(2)** assemble a catalog of loci with a subset of individuals, **(3)** estimate heterozygosity and Fst between cohorts, **(4)** test to see whether particular alleles sort with cohorts associated with particular temperature regimes, and **(5)** if any loci do sort, align them to the Atlantic cod (*Gadus morhua*) genome to see whether these loci occur within genes associated with temperature regulation.

### Directory Structure ###

Within my class repo, I have a directory for this project. Within this directory, I made a directory for **Data** that has directories for raw data, processed data, and  metadata. Raw data is never altered and stored in its own directory to protect it. Metadata includes information on the individual fish, environmental conditions, etc. Processed data is for data that has made it through part of the pipeline. 

Within the project directory, I also made a directory for **Analyses**. This directory has a directory for fast qc results, which describe the quality of the sequence data. As I make progress working my data through the pipeline, I will make directories here for different types of analyses.

Within the project directory, I also made a **Notebooks** directory that contains all of my Jupyter notebooks for the project, and their checkpoints.

Within the project directory, I also made a **Scripts** directory that will eventually contain any scripts associated with the project. I expect to have a custom script for my general pipeline by the end of the quarter.

### Project Timeline ###

In **Week 4** I plan to write the scripts necessary to build loci for each individual.

In **Week 5** I plan to write the scripts necessary to assemble a catalog and match individuals to the catalog.

During the rest of the quarter, I plan to analyze differences between cohorts, see if they match with environmetnal data, and align them to the Atlantic genome to see whether any sorting alleles occur within genes that regulate temperature.
