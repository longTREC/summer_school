# 🍄 How to run the Pairwise Custom Module

This is a walkthrough on how to run the pairwise custom module of AMaNITA. 

> [!NOTE]
> _**Why**_: When analysing biological data -especially large and/or complex datasets like clinical cohorts or projects with complex experimental designs- we often find that several covariates/confounding variables are at play; if these covariates substantially explain our data, it is best practices that they are included in our model design. AMaNITA is designed to run very simple models, accounting for up to two batch variables when performing the pairwise differential analyses; the **Pairwise Custom module** was built to accomodate more complex, user-defined models, accounting for additional confounding variables beyond batch effects.
>
> _**Where**_: (aka _where can I find which covariates make sense to be included in my complex model?_) Principal Variance Component Analysis (PVCA) is carried out during the execution of the Batch Module of AMaNITA; this step allows us to investigate to which extent each of the variables "contributes to" and/or "describes" our data. Covariates with substantial contribution can be found in the `Suggested Models > Suggested Effects to Account for in the Model` section of the report; this table is there for you to get inspired.
>
> _**Which**_: (aka _which of the suggested effects should I include in my custom model?_) We suggest that different combinations of covariates are tested, i.e. you can experiment with multiple custom models and combinations of variables; you can also compare between different batches or other biological groups, which the default settings of AMaNITA do not compare; tl/dr: whichever make sense for your analysis.
>
> _**When**_: (aka _when can I run the module?_) You don't have to know which custom models you need to run -on the contrary, AMaNITA is there to help you figure them out; we suggest you run AMaNITA first, enabling the batch module and without defining custom models, and then utilize the results of the PVCA to guide your downstream analyses; if set up properly, AMaNITA will resume the analysis when you define your custom models, without the need to rerun modules or previous analyses.
> 
> _**How**_: See below

## 🏃 Quick Start

### 1. 🗃️ Creating the Custom Models File

One file with the user defined custom models can be used per Project.

> [!IMPORTANT]
> The custom models file is expected to be under the project directory, e.g. under `Projects/{project_id}` or `{wrk_dir}/{project_id}`
> 
> The metadata file is expected to be named `{project_id}.custom_models.tsv`.
> 
> Each **line** contains information on **one** custom model.
>
> 5 columns are expected (header has to be included)
>   - 1: `model_number` - custom model ID, can be whatever as long as different models have different IDs; suggested naming: `custom_{i}` or `model_custom_i`, etc.  
>   - 2: `comparison_var` - variable for which we want to perform the pairwise comparison ⚠️ the comparison variable and the pair of groups to be compared have to be included in the **metadata** file, but they can be any of the `comp_`, `batch_`, or `extra_` variables ⚠️
>   - 3: `group1` - group 1 of 2 for the pairwise comparison
>   - 4: `group2` - group 2 of 2 for the pairwise comparison; acts as the  baseline (control)
>   - 5: `covariates` - list of covariates, separated by `;`; if you want to run a simple model only with the specified comparison variable, simple set this to ";" ⚠️ covariates have to be included in the **metadata** file, i.e. be one of the columns ⚠️
>
> ⚠️ When creating the custom models file, make sure that the newline character is Unix-based (i.e. not Windows- or MacOS-based)

Example of a `custom_models.tsv` file:

| model_number | comparison_var | group1 | group2 | covariates |
| --- | --- | --- | --- | --- |
| custom_1 | batch_RunDate | 2025_04_01 | 2025_03_31 | ; |
| custom_2 | batch_Technician | Bigotin | Saganaki | batch_RunDate |
| custom_3 | comp_Tissue | Brain | Spleen | batch_RunDate;extra_CellType |
| custom_4 | comp_Tissue | Brain | Spleen | batch_RunDate;batch_Technician;extra_CellType |
| custom_5 | comp_Tissue | Brain | Spleen | batch_RunDate;batch_Technician;extra_CellType;comp_Tissue:extra_CellType |

### 2. 👟 Running AMaNITA w/ Pairwise Custom

All you have to do was enable the pairwise custom module when running AMaNITA (argument `-5` or `-run_pairwise_custom`). Here is the general structure to create an `ftbpc` report:

```
bash ~/AMaNITA/src/AMaNITA.sh \
     --amanita_dir ~/AMaNITA \
     --project_id {project_id} \
     --wrk_dir {wrk_dir} \
     --data_dir {data_dir} \
     --organism {organism} \
     --mode_rnas {mode_rnas} \
     -12345
```

If you know you want to run custom models for your project at some point but don't know exactly which yet, you can create the `custom_models.tsv` file, either empty or only with the headers as placeholders, and run AMaNITA with the pairwise custom module enabled.
1. this will run whichever of the main modules you have set (1 to 4), and will generate a report with the results from these modules
2. ff you explore the PVCA (batch module results) you can get inspired about possible custom models and enrich your custom models file
3. then, rerunning the same command will load the results from the previous modules and in addition will run the pairwise custom module
4. a new report will be produced, now including the custom model results as well.

You can also expand the custom models file (after running it properly)
1. if you add a custom model for an existing custom comparison (e.g. another Brain vs Spleen comparison but with a different model), make sure to delete the related `pairwise_custom.Rdata` before rerunning the command
2. otherwise, if you add a completely new comparison (e.g. Liver vs Spleen), you can just rerun the command and only the newly added comparison/model will be carried out.
