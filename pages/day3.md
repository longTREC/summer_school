---
layout: page
title: Day 3
schemadotorg:
  "@context": http://schema.org/
  "@type": CreativeWork
  "genre": TrainingMaterial
  isPartOf:
      url: "https://longtrec.github.io/summer_school/"
      name: "LongTREC summer school - long-read transcriptomics"
---

<img src="../assets/logos/LongTREC_logo_FINAL.png" width="200" />

# Day 3 Agenda

## Goals
**Morning session: Differential expression analysis**
* To learn how long-read RNA-seq can be used for differential isoform expression/usage analysis and what are the current challenges
* To learn about specific case of expression analysis: allele-specific expression analysis

**Afternoon session: RNA modifications**
* Learn how long read sequencing technologies are utilized for the study of RNA modifications
* Hands-on session for the study of the tRNAome

## Timetable

| Time | Activity | Details | Literature |
|------|---------|---------|------------|
| 9:00 - 9:30 | How to build your expression matrix and concept of DE analysis vs DIU | call and join, join and call |  |
| 9:30 - 10:30 | Hands on | tappAS, IsoTools | [tappAS](https://genomebiology.biomedcentral.com/articles/10.1186/s13059-020-02028-w), [IsoTools](https://isotools.readthedocs.io/en/latest/)|
| **Break** | 
| 10:30 - 11:00 | Allele-specific expression | Specificity of long-reads<br>* Introduction.<br>* Biases and limitations.<br>* Main steps.<br>* Minimum input.<br>* Expected output<br>* Existing pipelines: LORALS, FALIR2, IDP-ASE |  [Review about allele-specific expression analyis](https://www.annualreviews.org/content/journals/10.1146/annurev-biodatasci-021621-122219), [LORALS](https://www.nature.com/articles/s41586-022-05035-y)|
| 11:00 - 12:30 | Hands on | analyze ASE dataset<br>**Hands-on Task 1**<br>Description of the data. QC and filtering of already mapped samples.<br>**Hands-on Task 2**<br>Allele-specific expression quantification<br>**Hands-on Task 3**<br>Allele-imbalance testing<br>**Hands-on Task 4**<br>Interpretation of results and output. Real example application<br>**Conclusion and remarks**<br>* |  |
| 12:30 - 13:30 | **Lunch break** | | |
| 13:30 - 14:30 | Introduction to epitranscriptomics | Overview of the field; use of long-read sequencing technologies for mapping RNA modifications; tRNA-specialized protocols and pipelines | |
| 14:30 - 15:00 | Hands-on | Mapping Nano-tRNAseq data | Tools: _minimap2_ |
| 15:00 - 15:30 | **Coffee Break** | | |
| 15:30 - 16:30 | Hands-on | Downstream processing: filtering, quality control, batch effect investigation, differential expression, diffenetial modifications | Tools: _AMaNITA_ |
| 16:30 - 17:00 | Closing remarks | Additional pipelines; modification-aware basecallers | |

## Learning Objectives

**Morning session: Differential expression analysis**
- understand the difficulties of assigning reads to isoforms
- understand biological mechanisms of allelic imbalance
- understand different sources of bias in allele-specific expression analysis

**Afternoon session: RNA modifications**
- understand the past and current challenges in the epitranscriptomics field
- understand why and how long-reads sequencing technologies are utilized for RNA modification detection
- familiarize with tools for epitranscriptomics data analysis


## Materials
* (here we will put links to the slides)


## Data
* 


## Recommended Bibliography
*
*
*
*


### Back

Back to [main page](../index.md).
