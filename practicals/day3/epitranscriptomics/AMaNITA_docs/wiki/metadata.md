# 🗒️ How to properly build your Metadata file

AMaNITA is built around a properly defined metadata table that provides all information required for an end-to-end analysis of the input data. This is a walkthrough on how to build your metadata table, things you should be careful, tips and tricks.

> [!IMPORTANT]
> The metadata file is a tab-separated file, expected to be named `{project_id}.metadata.tsv`.
> 
> The metadata file is expected to be under the project directory, e.g. `{wrk_dir}/{project_id}/{project_id}.metadata.tsv`. 
> 
> Each **line** contains information on **one** sample.
>
> When creating the metadata table, make sure that the newline character is Unix-based (i.e. not Windows- or MacOS-based)
>
> Expected columns:
> - 1: `Project`
> - 2: `Run`
> - 3: `BAMID`
> - 4: `BarcodeID`
> - 5: `SampleID`
> - 6: (optional) `ReplicateID`
> - 6/7+: variables of interest, tagged with either of the following: `comp_`, `batch_`, or `extra_`
>
> ⚠️ Columns 1-6 (when ReplicateID is included) require the column names to be as shown above (`Project`, `Run`, `BAMID`, `BarcodeID`, `SampleID`, `ReplicateID`)

---

## 1. 💣 Input BAM files

> [!NOTE]
> - Columns 1: `Project`,  2: `Run`, and 3: `BAMID` are used to construct the paths from where the input BAM files can be retrieved. Once the data directory is specified (`{data_dir}`), AMaNITA will search for the BAM files following this convention: `{data_dir}/{Project}/{Run}/reads.{BAMID}.bam`
> - Column 4: `BarcodeID` - since the input files are BAM files, you can set `BarcodeID` to be the same as `SampleID`, but if you want to set it to something else make sure the identifier is **unique**
> - Column 5: `SampleID` - user-defined Sample identifier; ⚠️ SampleIDs have to be **unique** per project/metadata file.
> - Column 6: (optional) `ReplicateID` - user-defined Replicate identifier, utilized for replicability analysis in quality control ; ⚠️ ReplicateIDs have to be **unique** per project/metadata file and are expected to follow this convention: `{Group_of_replicates}_Rep{number}` so that all replicates from the same group of interest are compared to each other, e.g. `Spleen_SFD_Rep1` will be compared to `Spleen_SFD_Rep2`
>
> 💡 For simplicity, it is suggested that `BAMID`, `BarcodeID`, `SampleID`, and `ReplicateID` are **unique and the same**, but of course this also depends on the experimental design of each project.
> 
> Following columns can be occupied by variables of interest. 3 types of variables are accounted for:
>   - `comp_` - variables for which AMaNITA can run pairwise comparisons; examples: "Treatment", "Tissue", "Diet", etc.
>   - `batch_` - variables potential introducing batch effects; AMaNITA will confirm whether batch effects are introduced and will proceed to adjust for
>   - `extra_` - additional variables of interest, for example clinical metadata
>   - ⚠️ It is advised that `comp_` and `batch_` variables are _not_ numerical; `extra_` can be numerical

⚠️ If  you are working with BAM files as input, remember to run the **preprocessing module**. For more check [this guide](./input.md#BAM-files).

Example metadata file for the test dataset can be found in [demo1.metadata.tsv](../data/demo1/demo1.metadata.tsv), and is also presented below:

```
Project  	Run  	BAMID  			BarcodeID  		SampleID  		ReplicateID		comp_KO
demo1  		/  	DUS1_D16_17_Rep1  	DUS1_D16_17_Rep1_5k  	DUS1_D16_17_Rep1  	DUS1_D16_17_Rep1  	KO
demo1  		/  	DUS1_D16_17_Rep2  	DUS1_D16_17_Rep2_5k  	DUS1_D16_17_Rep2 	DUS1_D16_17_Rep2  	KO
demo1  		/  	WT_Rep1  		WT_Rep1_5k  		WT_Rep1  		WT_Rep1  		WT
demo1  		/  	WT_Rep2  		WT_Rep2_5k  		WT_Rep2  		WT_Rep2  		WT
```

> [!IMPORTANT]
> In the case above, `BarcodeID` is different to the `SampleID` in order to match the headers of the provided input tables (see [reads.bam.base_count.tsv](../data/demo1/reads.bam.base_count.tsv)). And vice versa, starting from BAM files only with the metadata file above, running the `preprocessing` module will generate input tables (e.g. the reads.bam.base_count.tsv table) with header IDs that match the BarcodeID.
>
> Project and Run can contain `/` in case the BAM files fall directly under the {data_dir}. In the case above, our BAM files are found under `AMaNITA/data/demo1`, so assuming `data_dir={amanita_dir}/data`, then swe can set Project to `demo1` and assign `/` to Run. Long story short, just make sure your BAM files follow this convention: `{data_dir}/{Project}/{Run}/reads.{BAMID}.bam`.

## 3. 🔬 For Novoa Lab App users

> [!NOTE]
> The first 5 columns are fixed across all projects; details:
>   - 1: `Project` - refers to the Project as defined inside the Nano-tRNAseq app
>   - 2: `Run` - refers to the Run ID assigned inside the Nano-tRNAseq app
>   - 3: `BAMID` - refers to the barcode assigned to the sample, whish is also the naming of the BAM file under the convention `reads.{BAMID}.bam`
>   - 4: `BarcodeID` - refers to the barcode assigned to the sample, or, ⚠️ _if the sample was renamed in the app, to the renamed identifier_
>   - 5: `SampleID` - user defined Sample identifier; ⚠️ SampleIDs have to be **unique** per project/metadata file
>   - 6: (optional) `ReplicateID` - user defined Replicate identifier; utilized for replicability analysis in quality control ; ⚠️ ReplicateIDs have to be **unique** per project/metadata file and are expected to follow this convention: `{Group_of_replicates}_Rep{number}` so that all replicates from the same group of interest are compared to each other, e.g. `Spleen_SFD_Rep1` will be compared to `Spleen_SFD_Rep2`
>   - ⚠️ These columns require the column names to be as shown above (`Project`, `Run`, `BAMID`, `BarcodeID`, `SampleID`, `ReplicateID`)
> 
> Following columns can be occupied by variables of interest. 3 types of variables are accounted for:
>   - `comp_` - variables for which AMaNITA can run pairwise comparisons; examples: "Treatment", "Tissue", "Diet", etc.
>   - `batch_` - variables potential introducing batch effects; AMaNITA will confirm whether batch effects are introduced and will proceed to adjust for
>   - `extra_` - additional variables of interest, for example clinical metadata
>   - ⚠️ It is advised that `comp_` and `batch_` variables are _not_ numerical; `extra_` can be numerical

## 💡 Tips and Tricks

💡 The tag `ignore_` can be utilized for any of the variables (in the column names), leading to this variable being ignored during the PVCA analysis and is useful in cases where this particular variable is a confounder.

💡 The pairwise module is automatically performing all available pairwise comparisons with group2 always being the baseline. In each pair of groups to be compared, the assignment of groups to group1 and group2 (=baseline) happens alphanumerically. If you want to always have 1 specific group as the baseline, consider renaming it with a "Z" at the start so that it's alphanumerically "always" ordered last (of course unless you have another group starting with Z... but you get the idea). Suggestion inspired by [#42](https://github.com/novoalab/AMaNITA/issues/42).

Adjusting the metadata file to run the analysis on a subset of the data: check [this walkthrough](./how_to_run_subset.md#1--creating-subset-ing-comparison-variables).
