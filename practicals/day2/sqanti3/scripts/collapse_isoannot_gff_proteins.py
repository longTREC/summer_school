
isoannot_gff = "/mnt/c/Users/jetzi/other_repos/summer_school/practicals/day2/sqanti3/output_solution/sqanti_isoannot/h1_endo_chr8_isotools/h1_endo_chr8_isotools_isoannot.gff3"

# read as pandas dataframe
import pandas as pd

# set pandas to display all columns
pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)

df = pd.read_csv(isoannot_gff, sep="\t", header=None)

# add row_number column to enumerate rows
df['row_number'] = range(len(df))

# create gene_id column by removing everything after the last underscore
df['gene_id'] = df[0].str.rsplit('_', n=1).str[0]

# filter for tappAS and protein rows, then group by gene_id, 4th and 5th columns
filtered_df = df[(df[1] == "tappAS") & (df[2] == "protein")]
grouped_df = filtered_df.groupby(['gene_id', 3, 4])

# for each group, set the 7th column to the first entry's 7th column value
def set_seventh_column(group):
    
    # if "ENSG00000153310.22_0" in group.iloc[0, 6]:
    #     print(group)

    first_ninth_value = group.iloc[0, 6]  # 7th column (index 6) of first row
    group.iloc[:, 6] = first_ninth_value  # set 7th column (index 6) of all rows

    # if "ENSG00000153310.22_0" in group.iloc[0, 6]:
    #     print(group)
    #     exit()

    return group

# Apply the function and keep the grouping columns to maintain original structure
collapsed_proteins_df = grouped_df.apply(set_seventh_column, include_groups=False).reset_index(drop=True)

# create a copy of the original dataframe to modify
result_df = df.copy()

# overwrite rows in the original dataframe where row_number matches
for idx, row in collapsed_proteins_df.iterrows():
    # Find the row in the original dataframe with matching row_number
    original_row_idx = result_df[result_df['row_number'] == row['row_number']].index[0]
    
    # Update all columns except row_number and gene_id (which were added for processing)
    result_df.loc[original_row_idx, 8] = row[8]

# create output filename in same location as input
import os
input_dir = os.path.dirname(isoannot_gff)
input_basename = os.path.basename(isoannot_gff)
output_filename = os.path.join(input_dir, input_basename.replace('.gff3', '_collapsed.gff3'))

# save to new file (now with all rows, but protein rows modified)
# exclude the gene_id and row_number columns when saving
result_df = result_df.drop(['gene_id', 'row_number'], axis=1)
result_df.to_csv(output_filename, sep='\t', header=False, index=False)
print(f"Collapsed data saved to: {output_filename}")


