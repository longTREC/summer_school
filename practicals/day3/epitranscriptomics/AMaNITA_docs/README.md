# 🍄 AMaNITA 🍄

**A**bundance, **M**odifications, **a**nd **N**anopore **I**ntensity **T**oolbox/**A**pplication

<img src="https://github.com/novoalab/AMaNITA/blob/master/aes/amanita.gif">

A pipeline for the combined analysis of tRNA abundance and modification information from Nanopore data; raw nanopore intensity signal to be integrated soon.

> [!NOTE]
> **Input**: Nano-tRNAseq-app-processed data, with accompanying metadata table
> 
> **Output**: AMaNITA Report

## 📚 Table of Contents 

- [🏃 Quick Start](#-quick-start)
	- [1. 📜 Software Requirements](#1--software-requirements)
	- [2. 💻 Cloning the Repository](#2--cloning-the-repository)
 	- [3. 🗒️ Creating the Metadata File](#3-%EF%B8%8F-creating-the-metadata-file)
  	- [4. 👟 Running the Pipeline](#4--running-the-pipeline)
  	- [5. 🐳 Advanced Options](#5--advanced-options)
  		- [🍄 AMaNITA Modules](#-amanita-modules)
  		- [🔮 Full List of Arguments](#-full-list-of-arguments)
  	   	- [🦄 Supported Organisms](#-supported-organisms)
- [❔ Got questions?](#-got-questions)
- [🎮 _How well have you read the docs_: A game](#-how-well-have-you-read-the-docs-a-game)

---

## 🏃 Quick Start

### 1. 📜 Software Requirements

- [Singularity](https://apptainer.org/user-docs/3.0/installation.html)
- (optional but ✨cute✨) [ansi](https://github.com/fidian/ansi)

### 2. 💻 Cloning the Repository

To gain access to the scripts in your local machine or server, the pipeline can be installed as follows to a desired location:

```bash
git clone https://github.com/novoalab/AMaNITA.git
```

✏️ For the purposes of this walkthrough, it is assumed that the repository is cloned in the home directory of the user.

### 3. 🗒️ Creating the Metadata File

One metadata file is required per project. Learn more about how to build your metadata file properly [here](./wiki/metadata.md).

> [!IMPORTANT]
> The metadata file is a tab-separated file, expected to be named `{project_id}.metadata.tsv`.
> 
> The metadata file is expected to be under the project directory, e.g. `{wrk_dir}/{project_id}/{project_id}.metadata.tsv`. 
> 
> Each **line** contains information on **one** sample.
>
> ⚠️ When creating the metadata table, make sure that the newline character is Unix-based (i.e. not Windows- or MacOS-based)

<details>
<summary>🔮 Details:</summary>
	
- The first 5 columns are fixed across all projects; details:
	- 1: `Project`,  2: `Run`, and 3: `BAMID` - they are used to construct the paths from where the input BAM files can be retrieved. Once the data directory is specified (`{data_dir}`), AMaNITA will search for the BAM files following this convention: `{data_dir}/{Project}/{Run}/reads.{BAMID}.bam`
	- 4: `BarcodeID` - is one of the Sample identifiers; ⚠️ if your input is BAM files, you can set this to be the same as `SampleID`; if you provide your own, AMaNITA-independent-generated abundance and modification files as input, `BarcodeID` are the column names in those input files; to learn more about the differences in input files, check [this guide](./wiki/input.md). Novoa Lab app users please refer [to this guide](./wiki/metadata.md#for-novoa-lab-app-users).
	- 5: `SampleID` - user-defined Sample identifier; ⚠️ SampleIDs have to be **unique** per project/metadata file
	- 6: (optional) `ReplicateID` - user-defined Replicate identifier, utilized for replicability analysis in quality control ; ⚠️ ReplicateIDs have to be **unique** per project/metadata file and are expected to follow this convention: `{Group_of_replicates}_Rep{number}` so that all replicates from the same group of interest are compared to each other, e.g. `Spleen_SFD_Rep1` will be compared to `Spleen_SFD_Rep2`
- ⚠️ These columns require the column names to be as shown above (`Project`, `Run`, `BAMID`, `BarcodeID`, `SampleID`, `ReplicateID`)

> 💡 For simplicity, it is suggested that `BAMID`, `BarcodeID`, `SampleID`, and `ReplicateID` are **unique and the same**, but of course this also depends on the experimental design of each project. Novoa Lab app users please refer [to this guide](./wiki/metadata.md#for-novoa-lab-app-users).
 
- Following columns can be occupied by variables of interest. 3 types of variables are accounted for:
	- `comp_` - variables for which AMaNITA can run pairwise comparisons; examples: "Treatment", "Tissue", "Diet", etc.
	- `batch_` - variables potential introducing batch effects; AMaNITA will confirm whether batch effects are introduced and will proceed to adjust for
	- `extra_` - additional variables of interest, for example clinical metadata
	- ⚠️ It is advised that `comp_` and `batch_` variables are _not_ numerical; `extra_` can be numerical
	
</details>

Example metadata file for the test dataset can be found in [demo1.metadata.tsv](./data/demo1/demo1.metadata.tsv), and is also presented below:

```
Project  	Run  	BAMID  			BarcodeID  		SampleID  		ReplicateID		comp_KO
demo1  		/  	DUS1_D16_17_Rep1  	DUS1_D16_17_Rep1_5k  	DUS1_D16_17_Rep1  	DUS1_D16_17_Rep1  	KO
demo1  		/  	DUS1_D16_17_Rep2  	DUS1_D16_17_Rep2_5k  	DUS1_D16_17_Rep2 	DUS1_D16_17_Rep2  	KO
demo1  		/  	WT_Rep1  		WT_Rep1_5k  		WT_Rep1  		WT_Rep1  		WT
demo1  		/  	WT_Rep2  		WT_Rep2_5k  		WT_Rep2  		WT_Rep2  		WT
```

### 4. 👟 Running the Pipeline

The pipeline is designed to run A-to-Z automatically for each project.

```bash
bash ~/AMaNITA/src/AMaNITA.sh \
     --amanita_dir ~/AMaNITA \
     --project_id {project_id} \
     --wrk_dir {wrk_dir} \
     --data_dir {data_dir} \
     --organism {organism} \
     --mode_rnas {mode_rnas} \
     -1234
```

<details>
<summary>🔮 Argument details:</summary>
	
* `--amanita_dir`: path to directory of AMaNITA, containing the pipeline scripts and auxiliary files
* `--project_id`: user-defined project ID; expected to match a directory under the `wrk_dir` directory, as well as the metadata file
* `--wrk_dir`: path to the working directory = the `analysis` directory; flexible argument, i.e. the user can specify any directory, and its structure will automatically be adjusted to the conventions <!--([see below](#the-analysis-directory))-->
* `--data_dir`: path to the `data` directory; flexible argument, i.e. the user can specify any directory, **as long as its structure and the metadata table match** <!--([see below](#the-data-directory))-->
* `--organism`: organism, in abbreviated synonym format, e.g. "hg38", "mm39", etc; see [the aux directory](./aux/ref_v0.9) for availale organism references; <!--([see below](#the-data-directory) how to generate the required reference for a custom organism)-->
* `--mode_rnas`: ["cyto"/"mito"/"all"]; tRNA mode/ whether to utilize only cytoplasmic, only mitochrondrial, or all tRNAs for the analysis
* `-1/2/3/4`: [see below](#4--running-the-pipeline-advanced)
* ⚠️ please make sure to provide all paths as absolute ⚠️
 
</details>

### 5. 🐳 Advanced Options

#### 🍄 AMaNITA Modules

With the settings above, AMaNITA executes 4 modules:

| Module | Explanation |
| --- | --- |
| Filtering | Fitlering of bad quality reads and/or mismaps; 3 filters are applied (see details about the filters below) |
| Technical | Quality control statistics and metrics; if filtering is carried out, QC metrics and plotsd will be generated for both before (pre-) and after (post-) filtering |
| Batch | Batch effect investigations; batch effect removal and suggestion of optimal linear models for downstream differential analyses |
| Pairwise | Pairwise comparisons between 2 groups of interest; differential abundance and differential modification analyses |

🔮 Details about the filters:

<img src="https://github.com/novoalab/AMaNITA/blob/master/aes/filtering_module.filters.png">

> [!TIP]
> Users can select which modules to run, as follows:

| Module | Abbrev | Arg (short) | Arg (long) |
| --- | --- | --- | --- |
| Filtering | f | -1 | --run_filtering |
| Technical | t | -2 | --run_technical |
| Batch | b | -3 | --run_batch |
| Pairwise | p | -4 | --run_pairwise |
| Pairwise Custom | c | -5 | --run_pairwise_custom |

> [!IMPORTANT]
> Different module settings will produce different (individual) reports.
>
> For example, when all modules are selected an `ftbp` report will be created with quality control statistics and plots before _and_ after filtering, performing batch effect investigations on the filtered data, and performing pairwise comparisons on the filtered data while accounting for batch effects.
>
> On the other hand, when one is interested in performing pairwise comparisons, a `p` report will be created containing only the pairwise comparison results on the unfiltered data and without accounting for any batch effects.

Example command for creating an `fbp` report:

```bash
bash ~/AMaNITA/src/AMaNITA.sh \
     --amanita_dir ~/AMaNITA \
     --project_id {project_id} \
     --wrk_dir {wrk_dir} \
     --data_dir {data_dir} \
     --organism {organism} \
     --mode_rnas {mode_rnas} \
     -234	
```

🎯 For running the pairwise custom module please check [this walkthrough](./wiki/how_to_pairwise_custom.md).

#### 🔮 Full List of Arguments

```
Usage:

bash AMaNITA.sh
              [ -h | --help                                 Prints this help message ]
              [ -a | --amanita_dir AMANITA_DIR              Setting the AMaNITA directory; defaults to ~/AMaNITA ]
              [ -p | --project_id PROJECT_ID                Project name/unique identifier ]
              [ -w | --wrk_dir WRK_DIR                      Working/projects directory ]
              [ -d | --data_dir DATA_DIR                    Data directory ]
              [ -o | --organism ORGANISM                    Organism abbreviation; currently suporting 'hg38', 'mm39', 'sacCer3' ]
 	      [ -c | --concat_report (true/false)           Concatenate results to report; defaults to true ]
              [ -l | --light_report (true/false)            Produce light report version (PDF) instead of interactive HTML; defaults to false ]
              [ -0 | --run_preprocessing                    Preprocess data not processed by the app ]
              [ -1 | --run_filtering                        Option to run prefiltering module ]
              [ -2 | --run_technical                        Option to run Technical and Quality Control analysis ]
              [ -3 | --run_batch                            Option to Run Batch Effect Investigation analysis ]
              [ -4 | --run_pairwise                         Option to run Pairwise comparisons between groups of interest ]
              [ -5 | --run_pairwise_custom                  Option to run Pairwise comparisons between groups of interest by setting custom models ]
              [ -6 | --run_igv                              Option to produce IGV tracks (in development) ]
              [ -m | --mode_rnas MODE_RNAS                  RNA groups to utilize; currently supports 'cyto', 'mito' (for tRNAs) ]
              [ -s | --singularity_dir SINGULARITY_DIR      Singularity container directory; defaults to ~/singularity ]
              [ -v | --appv APP_VERSION                     App version; defaults to v0.9 (for debugging and dev purposes mainly) ]
              [ -q | --quiet                                Quiet mode, prints messages to err file; defaults to verbose mode, printing messages to console ]
              [ -r | --overwrite                            Overwrite existing results; defaults to false ]

```

#### 🦄 Supported Organisms

| Organism | Abbrev | Supported |
| --- | --- | --- |
| Human (_Homo sapiens_) | hg38 | ✅ |
| Mouse (_Mus musculus_) | mm39 | ✅ |
| Yeast (_Saccharomyces cerevisiae_) | sacCer3 | ✅ |

For creating custom annotations please check [this walkthrough](./aux_src/README.md).

---

## ❔ Got questions?

For questions or issues please reach out to [Leda](https://github.com/LedaKatopodi) or open a ticket~!

---

## 🎮 _How well have you read the docs_: A game

Try answering the following questions to test how carefully you went through AMaNITA's documentation. Feel free use the hints below if you get stuck!

- 😼 What are the names of Leda's future cat babies?
- 🍝 What greek foods are in AMaNITA's menu?
- 💀 Which of the greek foods is quite macabre if not written with proper punctuation (in greek)?
- 🧙‍♀️ Can you spot 5 bruja items in the documentation?

<details>
<summary>💡 Hints:</summary>
	
- 😼: In the documentation you will find that they caused a big mess when they prepared some libraries for sequencing, leading to a worrying batch effect
- 🍝: There are 6 different plates for you to choose from!
- 💀: There are only two dots separating ribs from children
- 🧙‍♀️: Don't only look for emojis
 
</details>
