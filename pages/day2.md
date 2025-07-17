---
layout: page
title: Day 2
schemadotorg:
  "@context": http://schema.org/
  "@type": CreativeWork
  "genre": TrainingMaterial
  isPartOf:
      url: "https://longtrec.github.io/summer_school/"
      name: "LongTREC summer school - long-read transcriptomics"
---

<img src="../assets/logos/LongTREC_logo_FINAL.png" width="200" />

# Day 2 Agenda

## Goals
* Gain an overview of the challenges of transcript identification and the variety of computational methods.
* Gain practical proficiency in the identification of known and novel transcript isoforms, as well as quality control of transcriptomes using tools like `IsoTools` and `SQANTI3`.
* Understand how to create structural annotations using an ab-initio predictor and further validate such annotations with long-read sequencing data.
* Gain practical experience in deriving isoform-resolved functional annotations and drawing biological conclusions through visualization and exploration.

## Timetable

| Time          | Activity                | Details                                                                                                                                       |
| --------------------- | --------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 09:00 - 09:20 | Transcript Identification         | <u>Yalan & Fabian</u>: Give an overview of basic concepts and the space of transcript identification and quantification tools (reference-reliant vs. de novo vs. quantification only)                                                                                                     |
| 09:20 - 09:40 | IsoTools Theory                   | <u>Yalan</u>: Overview of theory and concepts of IsoTools algorithm and functionalities                                                                                                                |
| 09:40 - 10:30 | IsoTools Practice                 | <u>Yalan</u>: Applying IsoTools to identify and quantify both known and novel transcripts, investigating results                                                                                           |
| 10:30 - 11:00 | Coffee Break                      |                                                                                                                                                                   |
| 11:00 - 11:30 | SQANTI3 Theory                    | <u>Fabian</u>: Motivate why we need transcriptome quality control and filter, and introduce SQANTI3 concepts like structural categories                                                                                           |
| 11:30 - 12:20 | SQANTI3 Practice                  | <u>Fabian</u>: Applying SQANTI3 to perform quality control, filtering, and rescue on a custom transcriptome                                                                      |
| 12:30 - 13:30 | Lunch break                       |                                                                                                                                                                   |
| 13:30 - 14:00 | Structural Annotation Theory      | <u>Fabio</u>: How long-read sequencing integrates in the structural genome annotation workflow (ab initio predictions, exon vs intron merge) and why it is useful (identification of alternative splicing and lncRNA) |
| 14:00 - 14:30 | Structural Annotation Practice: Prediction | <u>Fabio</u>: Informing an ab-initio predictor with long-read models and evaluate its impact                                                                                                        |
| 14:30 - 15:00 | Structural Annotation Practice: Validation | <u>Fabio</u>: Using long-read RNA support to validate gene models in a novel annotation                                                                                                                     |
| 15:00 - 15:30 | Coffee Break                      |                                                                                                                                                                   |
| 15:30 - 16:00 | Functional Annotation Theory      | <u>Ana & Fabian</u>: How to map functions (from public databases or predictors) to isoform-resolved sequences        |
| 16:00 - 16:50 | Functional Annotation Practice    | <u>Ana & Fabian</u>: Utilizing IsoAnnotLite to obtain isoform-resolved annotations and visualization of results |
| 16:50 - 17:00 | Summary                           | Questions                                                                                                                                                         |

## Learning Objectives
* Students should be able to understand common problems for transcript identification and quantification and benchmarking resources
* Students should be able to understand the landscape of transcript identification and quantification tools.
* Students should be able to apply IsoTools and SQANTI3.
* Students should be able to understand how long-read sequencing integrates in the structural genome annotation workflow.
* Students should be able to use long-read sequences to validate gene models and assess performance
* Students should be able to functionally annotate transcript models and evaluate annotation results.

## Materials
* [Transcript identification](theory/day2/Transcript Identification.pdf)
* [Transcript identification quantification](theory/day2/Transcript identification quantification theory.pptx)
* [Isotools](theory/day2/IsoTools theory.pptx)
* [SQANTI3](theory/day2/SQANTI3.pdf)
* [Functional annotation](theory/day2/Functional Annotation.pdf)

## Data
* [Data](https://github.com/longTREC/summer_school_data_backup/day2/data): link to backup.

## Recommended Bibliography
* Monzó, C., Liu, T. & Conesa, A. Transcriptomics in the era of long-read sequencing. Nature Reviews Genetics (2025). [https://doi.org/10.1038/s41576-025-00828-z](https://doi.org/10.1038/s41576-025-00828-z)
* Bi, Yalan, et al. "IsoTools 2.0: software for comprehensive analysis of long-read transcriptome sequencing data." Journal of Molecular Biology (2025): 169049. [https://doi.org/10.1016/j.jmb.2025.169049](https://doi.org/10.1016/j.jmb.2025.169049)
* Pardo-Palacios, F.J., Arzalluz-Luque, A., Kondratova, L. et al. SQANTI3: curation of long-read transcriptomes for accurate identification of known and novel isoforms. Nature Methods (2024). [https://doi.org/10.1038/s41592-024-02229-2](https://doi.org/10.1038/s41592-024-02229-2)

### Back

Back to [main page](../index.md).
