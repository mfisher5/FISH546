# BLAST SEA STAR HOMEWORK
# 20161027 NL

## 1--- Download DESeq2 package for R

source("http://bioconductor.org/biocLite.R") #download script for installation
biocLite("DESeq2") #install
library(DESeq2) #load

## 2--- Download data


# Andrew's code
data<- read.table("Phel_countdata.txt", header=T, sep ="\t") 
rownames(data) <- data$Feature
data<-data[,-1]
deseq2.colData <- data.frame(condition=factor(c(rep("Treated", 3), rep("Control", 3))), 
                             type=factor(rep("single-read", 6)))
rownames(deseq2.colData) <- colnames(data)
deseq2.dds <- DESeqDataSetFromMatrix(countData = data,
                                     colData = deseq2.colData, 
                                     design = ~ condition)

deseq2.dds <- DESeq(deseq2.dds)
deseq2.res <- results(deseq2.dds)
deseq2.res <- deseq2.res[order(rownames(deseq2.res)), ]

head(deseq2.res, n=30)

dim(deseq2.res[!is.na(deseq2.res$padj) & deseq2.res$padj <= 0.05, ])

tmp <- deseq2.res
# The main plot
plot(tmp$baseMean, tmp$log2FoldChange, pch=20, cex=0.45, ylim=c(-3, 3), log="x", col="darkgray",
     main="DEG Virus Exposure  (pval <= 0.05)",
     xlab="mean of normalized counts",
     ylab="Log2 Fold Change")
# Getting the significant points and plotting them again so they're a different color
tmp.sig <- deseq2.res[!is.na(deseq2.res$padj) & deseq2.res$padj <= 0.05, ]
points(tmp.sig$baseMean, tmp.sig$log2FoldChange, pch=20, cex=0.45, col="purple")
# 2 FC lines
abline(h=c(-1,1), col="green")

head(tmp)
sig<-deseq2.res[!is.na(deseq2.res$padj) & deseq2.res$padj <= 0.05, ]
head(sig)
?write.table
write.table(sig, file="sig.txt")