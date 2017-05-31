# SRA RNAseq Workflow

This script automates the process of downloading SRA files from a GEO dataset,
preforming trimming and quality assurance of the SRA files, and mapping the
cleaned reads to a reference genome.

## Dependencies

This assumes that you have `pip` installed. I have not tested installation with other package managers (but I suspect `brew install` should work as well). 

### trim_galore

placeholder

### cutadapt

To download cutadapt, either visit the github page [here](https://github.com/marcelm/cutadapt) or simply use `pip install cutadapt`

### STAR

To download STAR, either visit the projects github page [here](https://github.com/alexdobin/STAR) or simply use `pip install STAR`

## Installation

Beside the dependencies, there is nothing to install. Clone the repository
or download the source code and run `SRA_rnaseq_workflow.py` from that directory.

## Quickstart

In this example, lets say you wanted to download SRA files with accession
numbers 1001, 1002, 1003 (these number are simply for illustration purposes).

Call `placeholder`
