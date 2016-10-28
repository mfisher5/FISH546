# BLAST SEA STAR HOMEWORK
# 20161027 NL

## 1--- Download DESeq2 package for R ---

source("http://bioconductor.org/biocLite.R") #download script for installation
biocLite("DESeq2") #install
library(DESeq2) #load

## 2--- Download data ---

# did manually and with !curl at command line

## 3--- Import data to R & build objects ---

data <- read.table("Phel_countdata.txt", header = T, sep = "\t")
rownames(data) <- data$Feature
data <- data[,-1]

# Build Objects
# Specify which columns are in which groups
deseq2.colData <- data.frame(condition=factor(c(rep("Treated", 3), rep("Control", 3))), 
                             type=factor(rep("single-read", 6)))
rownames(deseq2.colData) <- colnames(data)
deseq2.dds <- DESeqDataSetFromMatrix(countData = data,
                                     colData = deseq2.colData, 
                                     design = ~ condition)

## 4--- Analysis ---

deseq2.dds <- DESeq(deseq2.dds)
deseq2.res <- results(deseq2.dds)
deseq2.res <- deseq2.res[order(rownames(deseq2.res)), ]

## 5--- View results ---

head(deseq2.res)

## 6--- Look for significant hits ---

# Count number of hits with adjusted p-value less then 0.05
dim(deseq2.res[!is.na(deseq2.res$padj) & deseq2.res$padj <= 0.05, ])


## 7--- Plot ---

tmp <- deseq2.res

# The main plot
plot(tmp$baseMean, tmp$log2FoldChange, pch=20, cex=0.45, ylim=c(-3, 3), log="x", col="darkgray",
     main="DEG Virus Exposure  (pval <= 0.05)",
     xlab="mean of normalized counts",
     ylab="Log2 Fold Change")

# Getting the significant points and plotting them again so they're a different color
tmp.sig <- deseq2.res[!is.na(deseq2.res$padj) & deseq2.res$padj <= 0.05, ]
points(tmp.sig$baseMean, tmp.sig$log2FoldChange, pch=20, cex=0.45, col="mediumseagreen") # changed color to medium sea green
# 2 FC lines
abline(h=c(-1,1), col="blue")

## 8 -- Write Phel_DEGlist.tab ---

write.table(tmp.sig, "Phel_DEGlist.tab", row.names = T)

## 9 -- Look at Phel_DEGlist.tab

head(tmp.sig)

## 10 -- Read in full transcriptome

head(Phel_transcriptome_tab)

## 11 -- Merge full transcriptome w tmp.sig to get just names and seqs of significantly diff exp genes

# manually changed transcriptome fasta to tab delimited file in text wrangler by replacing /n with /t and then replacing > with /n
# manually removed quotations from names in text wrangler for dif exp gene file
# bring dif exp gene file back in

# read in names of diff exp genes file
newdif <- read.csv("justnames.txt", header = T, sep = "\t")
head(newdif) # check
names(newdif)[1] <- "Name"

# read in transcriptome file
Phel_transcriptome_tab <- read.delim("~/Desktop/Seastar-HW/Phel_transcriptome_tab.txt", header=FALSE)
trans <- Phel_transcriptome_tab
head(trans)
names(trans)[1:2] <- c("Name", "Seq")

# extract rownames
merged <- merge(newdif, trans, by = "Name", all.y = FALSE)
head(merged)

# check that merge worked
# get length of just names file, then see if matches length of merged file
nrow(newdif)
nrow(merged)

write.table(merged[,1:2], file = "signames_seqs.txt", sep = "\n", row.names = FALSE, col.names = FALSE)
