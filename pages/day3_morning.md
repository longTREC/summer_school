---
layout: page
title: Page title
schemadotorg:
  "@context": http://schema.org/
  "@type": CreativeWork
  "genre": TrainingMaterial
  isPartOf:
      url: "https://longtrec.github.io/summer_school/"
      name: "LongTREC summer school - long-read transcriptomics"
---

<img src="../assets/logos/LongTREC_logo_FINAL.png" width="200" />

# Day 3 Morning Agenda

## Goals
* To learn how long-read RNA-seq can be used for differential isofrom expression/usage analysis and what are the current challenges
* To learn about specific chase of expression analysis: allele-specific expression analysis


## Timetable
| Time | Cctivity | Details | Literature |
|------|---------|---------|------------|
| 9:00 - 9:30 | How to build your expression matrix and concept of DE analysis vs DIU | call and join, join and call |  |
| 9:30 - 10:30 | Hands on | tappAS, IsoTools | [tappAS](https://genomebiology.biomedcentral.com/articles/10.1186/s13059-020-02028-w), [IsoTools](https://isotools.readthedocs.io/en/latest/)|
| **Break** | 
| 10:30 - 11:00 | Allele-specific expression | Specificity of long-reads<br>* Introduction.<br>* Biases and limitations.<br>* Main steps.<br>* Minimum input.<br>* Expected output<br>* Existing pipelines: LORALS, FALIR2, IDP-ASE |  [Review about allele-specific expression analyis](https://www.annualreviews.org/content/journals/10.1146/annurev-biodatasci-021621-122219), [LORALS](https://www.nature.com/articles/s41586-022-05035-y)|
| 11:00 - 12:30 | Hands on | analyze ASE dataset<br>**Hands-on Task 1**<br>Description of the data. QC and filtering of already mapped samples.<br>**Hands-on Task 2**<br>Allele-specific expression quantification<br>**Hands-on Task 3**<br>Allele-imbalance testing<br>**Hands-on Task 4**<br>Interpretation of results and output. Real example application<br>**Conclusion and remarks**<br>* |  |



## Learning objectives

- understand the difficulties of assigning reads to isoforms
- understand biological mechanisms of allelic imbalance
- understand different sources of bias in allele-specific expression analysis


### Back

Back to [main page](../index.md).
