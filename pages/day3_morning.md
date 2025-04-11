---
layout: page
schemadotorg:
  "@context": http://schema.org/
  "@type": CreativeWork
  "genre": TrainingMaterial

  # Course details
       # "name" -> The acronym and extended name of the course, separated by " - "
       # "description" -> Short description of the course
  name: "LongTREC summer school - Differential expression and haplotype analysis using long reads"
  description: ""

  # Keywords -> Consult EDAM:Topic
  keywords:  ""

  # Audience -> Following Elixir-Tess input
  audience: ["Academia/ Research Institution"]

  # Author info
  author:
    - "@type": Organization
      name: "LongTREC"
      alternateName: "LongTREC"
      sameAs: "https://longtrec.eu/"

  # predominant type of learning resources
  "learningResourceType": ["presentation", "exercise", "scripts", "handout"]

  # Contributor info
  contributor:
    - "@type": Person
      name: "CO-AUTHOR_1"
    - "@type": Person
      name: "CO-AUTHOR_2"
    - "@type": Person
      name: "CO-AUTHOR_3"

  # License & Language & url
  license: https://creativecommons.org/licenses/by/4.0/
  inLanguage: "en-us"
  url: "https://longtrec.github.io/summer_school/day3_morning"
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
