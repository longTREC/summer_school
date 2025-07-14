---
layout: page
title: Day 1
schemadotorg:
  "@context": http://schema.org/
  "@type": CreativeWork
  "genre": TrainingMaterial
  isPartOf:
      url: "https://longtrec.github.io/summer_school/"
      name: "LongTREC summer school - long-read transcriptomics"
---

<img src="../assets/logos/LongTREC_logo_FINAL.png" width="200" />

# Day 1 Agenda

## Goals
* To learn different library preparation (libprep) approaches for various transcriptomics applications
* Gain practical proficiency in assessing long-read data quality: Learn to interpret key QC metrics and utilize tools like `NanoPlot` and `SQANTI-reads` for quality assessment.
* Master the fundamentals of long-read mapping: Understand the unique challenges, compare different mapping strategies (e.g., seed-chain-extend, minimizers), and apply tools like `minimap2` and `ulTRA`.
* Develop hands-on skills in executing bioinformatics workflows: Confidently run alignment and transcript quality control analyses in a cluster environment using provided datasets.
* Critically evaluate and interpret analysis results: Compare outcomes from different mapping tools and QC analyses, linking findings back to experimental design choices and library preparation methods.

## Timetable

| Time          | Activity                | Details                                                                                                                                       |
| --------------------- | --------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 09:00 - 09:10 | Introduction & Objectives         | <u>Ana</u>: Welcome participants, provide an overview of the day, outline learning objectives, and conduct a quick interactive poll (e.g., "Have you used PacBio or ONT before?")                                                                                                     |
| 09:10 - 09:50 | Long-Read Sequencing Technologies                   | <u>Carolina</u>: General Introduction to long-reads sequencing technologies (pacbio and nanopore) general introduction to designing long-read RNA-seq experiments including platform-selection, trade-offs between read length and depth, and sample replication (cDNA vs directRNA, read length, Replicates, Multiplexing strategies, Depth of sequencing)                                                                                                                |
| 09:50 - 10:00 | Q&A Break                 | Short break for questions; use an online quiz (e.g., Kahoot) to recap key facts from the previous session                                                                                           |
| 10:00 - 10:35 | Experimental Design for lrRNA-seq                      | <u>Satrio</u>: Library preparation strategies for long-reads RNA-seq experiments, cDNA and RNA based, and basecalling. (General transcriptomics, Native RNA sequencing, mRNA (comment on size selection in commercial libprep), tRNA, Long non-coding RNA, Improving representation (methods to enhance RNA diversity and coverage), Single-cell transcriptomics. Basecalling: General stuff from ONT (squiggles, segmentation etc) and PacBio (deepconsensus))                                                                                                                                                                   |
| 10:35 - 11:00 | Coffee Break & Poll                    | Refreshment break paired with a fun poll question (e.g., "Which factor impacts transcript discovery the most: read length or read depth?")                                                                                           |
| 11:00 - 11:30 | Data Quality and QC Metrics                  | <u>Tian</u>: Overview of QC metrics: Phred quality scores, error profiles, and tools like NanoPlot. Introduce SQANTI-reads for assessing transcript quality, explain its categories, and show an example using the WTC11 dataset. Learning outcomes include understanding data quality and interpreting QC reports.                                                                      |
| 11:30 - 12:15 | Read Mapping and Reference Alignment                  | <u>Sami</u>: Introduce challenges in long-read mapping(how to tolerate errors). Cover strategies (seed-chain-extend, minimizer, de Bruijn graph) for mapping long-reads to reference genomes/transcriptomes, discussing alignment techniques and tools                                                                                                                                                                    |
| 12:15 - 12:30 | Discussion & Prep for Hands-on      | Open Q&A on lecture content, recap main takeaways (e.g., differences in technologies and mapping strategies), and ensure participants are set up for the afternoon practical session with server access and data locations confirmed |
| 12:30 - 13:30 | Lunch Break | Lunch and informal networking                                                                                                       |
| 13:30 - 13:45 | Practical Setup & Dataset Overview | <u>Sami & Tian</u>: Re-introduction post-lunch. Outline the tasks for the practical session and provide an overview of the two datasets from LRGASP: WTC11 (human) and Mouse ES (mouse). Explain the rationale for using representative 10,000-read subsets and point out file locations and reference materials on the shared server                                                                                                                     |
| 13:45 - 14:45 | Task 1: Map WTC11 & ES Reads (Human Data)                      |<u>Sami & Tian</u>: Hands-on session mapping WTC11 long-reads using minimap2. Includes job setup via SLURM, monitoring job progress, and post-mapping steps (sorting, indexing, and reviewing mapping statistics). Learning outcomes: practical experience in running alignments and interpreting basic mapping metrics                                                                                                                                                                   |
| 14:45 - 15:15 | Task 2: Map WTC 11 reads with alternative mappers      | <u>Sami & Tian</u>: Map the WTC 11 reads using an alternative mapper (ulTRA) to compare performance with minimap2        |
| 15:15 - 15:45 | Coffee Break & Group Discussion    | Short break combined with a group discussion on mapping challenges (e.g., handling large files, parameter choices) and sharing insights on mapper performance |
| 15:45 - 16:45 | Task 3: QC Analysis with SQANTI-reads                           | <u>Tian & Sami</u>: Perform quality control analysis using SQANTI-reads on the alignment results from both datasets. This session includes running the analysis, reviewing output (e.g., classification of splice patterns, PCA plots), and interpreting differences between the human datasets with different library preparation protocols and sequencing platforms. Learning outcomes: understanding QC workflows and identifying technology or biological biases                                                                                                                                                         |
| 16:45 - 17:05 | Results Discussion and Interpretation                           | <u>Tian & Sami</u>: Group discussion to review mapping results and SQANTI-reads findings. Participants compare mapping rates and splice junction classifications, linking practical outcomes back to theoretical concepts and experimental design choices                                                                                                                                                         |
| 17:05 - 17:15 | Wrap-up & Next Steps                           | <u>Tian, Sami, Satrio & Carolina</u>: Conclude the day with a recap of key takeaways: long-read platform comparison, experimental design strategies, mapping techniques, and QC interpretation. Discuss next steps, provide further resources, and possibly close with a final poll or quiz to reinforce learning                                                                                                                                                         |

## Learning Objectives
* Understand the fundamental principles, advantages, and limitations of PacBio and Nanopore long-read sequencing technologies.
* Evaluate the trade-offs between different long-read platforms, read lengths, and sequencing depths for specific experimental goals.
* Design appropriate long-read RNA-seq experiments, considering factors like sample replication, library preparation strategy (cDNA vs. direct RNA), and multiplexing.
* Describe various library preparation strategies tailored for different transcript types (mRNA, tRNA, lncRNA) and applications (e.g., single-cell).
* Assess the quality of long-read sequencing data using standard QC metrics and tools (e.g., NanoPlot).
* Understand the challenges associated with mapping long, error-prone reads and explain common mapping strategies.
* Perform long-read mapping using standard tools (e.g., `minimap2`, `ulTRA`) in a high-performance computing environment.
* Execute post-mapping processing steps, including sorting and indexing alignment files.
* Utilize `SQANTI-reads` to perform quality control on transcript alignments, interpret its output, and identify potential biases.
* Compare mapping and QC results obtained from different datasets, library preparation methods, and mapping tools, linking practical outcomes to experimental design choices.

## Materials
* [Introduction and experimental design slides](../theory/day1/LongTREC_presentation_Day1_Carol.pdf) - Theory presentation covering introduction to sequencing technologies and experimental design checkin points.
* [Library preparation slides](../theory/day1/LongTREC_presentation_Day1_Satrio.pdf) - Theory presentation covering library preparation and basecalling.
* [Mapping slides](../theory/day1/Mapping.pptx) - Theory presentation on mapping algorithms.
* [SQANTI-reads Concept Slides](../theory/day1/tian/slide/sqanti_reads_concept.pdf) - Theory presentation covering SQANTI-reads inputs, outputs, and key features.
* [Day 1 Practical Session](../practicals/day1/day1_practical.pdf) - Hands-on session slides covering experiment design, alignment comparison (minimap2 vs uLTRA), and SQANTI-reads applications.

## Data
* [LRGASP H1 & H1-DE Chr8 Dataset](https://longtrec-summer-school.s3.us-east-1.amazonaws.com/lrgasp_h1_h1de_chr8_1_60000000.zip) - Subset of LRGASP Challenge 2 data focusing on chromosome 8 (positions 1-60,000,000) for H1 and H1-DE cell lines

## Recommended Bibliography
* Monzó, C., Liu, T. & Conesa, A. Transcriptomics in the era of long-read sequencing. Nature Reviews Genetics (2025). [https://doi.org/10.1038/s41576-025-00828-z](https://doi.org/10.1038/s41576-025-00828-z)
* Li, H. Minimap2: pairwise alignment for nucleotide sequences. Bioinformatics (2018). https://doi.org/10.1093/bioinformatics/bty191
* Sahlin, K., Makinen, V. Accurate spliced alignment of long RNA sequencing reads. Bioinformatics (2021). [https://doi.org/10.1093/bioinformatics/btab540](https://doi.org/10.1093/bioinformatics/btab540)
* Pardo-Palacios, F.J., Arzalluz-Luque, A., Kondratova, L. et al. SQANTI3: curation of long-read transcriptomes for accurate identification of known and novel isoforms. Nature Methods (2024). [https://doi.org/10.1038/s41592-024-02229-2](https://doi.org/10.1038/s41592-024-02229-2)
* Keil, N., Monzo, C., McIntyre, L., Conesa, A. Quality assessment of long read data in multisample lrRNA-seq experiments using SQANTI-reads. Genome Research (2025). [https://doi.org/10.1101/gr.280021.124](https://doi.org/10.1101/gr.280021.124)

### Back

Back to [main page](../index.md).
