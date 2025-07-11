# 🚇 How to run a subset of the data

This is a walkthrough on how to run AMaNITA on a subset of your data. 

> [!NOTE]
> _**Why**_: AMaNITA is designed to perform all pairwise comparison possible per comp_variable defined. But sometimes we don't want that; sometimes we just need an overview of our whole dataset but comparisons between specific subsets of the data. Other times we just want to ignore some samples and perform additional comparisons but without rerunning everything. 
>
> _**How**_: See below

In some way or another, the following approaches are interchangeable and alternative to each other; depending on the context, however, one might be more or less easy:
- [1. 🚇 Creating subset-ing comparison variables](#1--creating-subset-ing-comparison-variables)
- [2. 🍄 Using the Pairwise Custom Module](#2--using-the-pairwise-custom-module)
- [3. 👽 Using another AMaNITA project as basis](#3--using-another-amanita-project-as-basis)

---

## 1. 🚇 Creating subset-ing comparison variables

Let's imagine that we are starting from a dataset somewhat like the one below

```
comp_Diet       comp_Tissue
GreekSalad      Spleen
GreekSalad      Spleen
GreekSalad      Spleen
Souvlaki        Spleen
Souvlaki        Spleen
Souvlaki        Spleen
GreekSalad      Liver
GreekSalad      Liver
GreekSalad      Liver
Souvlaki        Liver
Souvlaki        Liver
Souvlaki        Liver
```

The automated settings of AMaNITA will perform two pairwise comparisons: 1) GreekSalad vs Souvlaki and, 2) Liver vs Spleen. Instead, we might be more interested in the effects of each diet in each tissue specifically, or in the differences between the tissues under the same diet. In this case, we can restructure our metadata likeso:

```
comp_Diet_Spleen    comp_Diet_Liver    comp_Tissue_Souvlaki
GreekSalad          -                  -
GreekSalad          -                  -
GreekSalad          -                  -
Souvlaki            -                  Spleen
Souvlaki            -                  Spleen
Souvlaki            -                  Spleen
-                   GreekSalad         -
-                   GreekSalad         -
-                   GreekSalad         -
-                   Souvlaki           Liver
-                   Souvlaki           Liver
-                   Souvlaki           Liver
```

By introducing the "-", we instruct AMaNITA to ignore those samples and perform the available pairwise comparisons for the rest of the samples. In this case, AMaNITA will perform three pairwise comparisons: 1) GreekSalad vs Souvlaki for the Spleen samples, 2) GreekSalad vs Souvlaki for the Liver samples, 3) Liver vs Spleen for the Souvlaki diet.

## 2. 🍄 Using the Pairwise Custom Module

In the case where we have multiple groups but we are interested in specific pairwise comparisons, we can skip the pairwise module and enable the pairwise_custom module of AMaNITA; for more details on how this module works please check [this walkthrough](./wiki/how_to_pairwise_custom.md). For example, assuming we are starting with the following groups (with enough replicates each)

```
comp_Diet
GreekSalad
Souvlaki
Pastitsio
Mousaka
Mpiftekia
Paidakia
```

but we only want to run the comparisons of the meat-based diets vs the vegetarian diet, we can define the `custom_models.tsv` file likeso:

```
model_number    comparison_var  group1      group2        covariates
custom_1        comp_Diet       Souvlaki    GreekSalad    ;
custom_2        comp_Diet       Pastitsio   GreekSalad    ;
custom_3        comp_Diet       Mousaka     GreekSalad    ;
custom_4        comp_Diet       Mpiftekia   GreekSalad    ;
custom_5        comp_Diet       Paidakia    GreekSalad    ;
```

## 3. 👽 Using another AMaNITA project as basis

Imagine we have an extensive cancer cohort dataset with hundreds of samples (highly possible real-life scenario) with some accompanying normal/healthy samples as well. At first, we might be interested in comparing tumour vs healthy in search for a pan-cancer tRNA signature; but then, we might want to compare between tumor types or subtypes. The following is a feasible workaround to reanalyzing parts of an analysis (assuming the appropriate metadata tables are provided):

```
# 1. analysis of the big cohort, tumour vs normal
bash ~/AMaNITA/src/AMaNITA.sh \
--amanita_dir ~/AMaNITA \
--project_id "CancerCohort" \
--wrk_dir ~/Projects/ \
--data_dir ~/nano-tRNAseq_data/ \
--organism "hg38" \
-1234 \
--mode_rnas "cyto"

# 2. analysis only of the tumor subset, without re-running computationally expensive parts
bash ~/AMaNITA/src/AMaNITA.sh \
--amanita_dir ~/AMaNITA \
--project_id "CancerCohort_subsetTumor" \
--wrk_dir ~/Projects/ \
--data_dir ~/Projects/CancerCohort/cyto/ftbp/filtering/filtered_bam/ \
--organism "hg38" \
-34 \
--mode_rnas "cyto"
```

💡 The trick here is that we can utilize the already filtered data as input, cutting down on modules (i.e. filtering or technical) that would produce results we already have from another analysis. 

