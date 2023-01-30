# GENESPACE-Companion-Script
This contains a python script developed as a companion to the GENESPACE pan-genome tool to obtain statistics from the output of GENESPACE.

[GENESPACE GitHub](https://github.com/jtlovell/GENESPACE)

[GENESPACE Manuscript](https://elifesciences.org/articles/78526)

## Input file

The input file is a TSV file, unique from the standard `results/[reference_genome]_pangenome.txt.gz` file. This file was generated based on the information provided in Section 9.4 in the official [GENESPACE Vignette](https://htmlpreview.github.io/?https://github.com/jtlovell/GENESPACE/blob/master/doc/genespaceOverview.html).

The following code can be run after following GENESPACE's documentation and obtaining the `pangenome` data.table object.

```
fwrite(pg, file = 'pangenome.tsv', quote = FALSE, sep = '\t')
```

## Current output statistics

* Total number of single-species orthogroups (one species, at least one gene).
* Total number of singletons (one species, only one gene).
* Number of singletons for each individual gene set.
* Total number of complete orthogroups (each gene set has at least one gene present in the orthogroup).
* Total number of single-copy orthogroups (each gene set has exactly one gene present in the orthogroup).
