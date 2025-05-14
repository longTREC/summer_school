#!/bin/bash

# Check for input arguments
if [ "$#" -ne 2 ]; then
    echo "Usage: $0 <gff_file> <fasta_file/genome_size_in_bp>"
    exit 1
fi

# Input arguments
gff_file="$1"
genome="$2"

# Determine if the second argument is a file or a number
if [ -f "$genome" ]; then
    # Remove headers, count characters, subtract newline count
    genome_size_bp=$(awk '{print $2 - $1}' < <(grep -v '^>' "$genome" | wc -l -c))
elif [[ "$genome" =~ ^[0-9]+$ ]]; then
    genome_size_bp="$genome"
else
    echo "Error: Second argument must be a FASTA file or a genome size in base pairs."
    exit 1
fi


# Function to calculate feature stats
calculate_feature_stats() {
    awk -F'\t' -v genome_size="$genome_size_bp" '!/^#/ {
        feature_type = $3
        start = $4
        end = $5
        feature_length = end - start + 1

        count[feature_type]++
        total_length[feature_type] += feature_length
    } END {
        print "Feature\tFeatures_Count\tTotal_Feature_Length\tAverage_Feature_Length\tGenome_Percentage"

        for (feature in count) {
            avg_length = total_length[feature] / count[feature]
            feature_density = (total_length[feature] / genome_size) * 100
            printf "%s\t%d\t%d\t%.2f\t%.2f\n", feature, count[feature], total_length[feature], avg_length, feature_density
        }
    }'
}

# Check if the input file is gzipped
if [[ "$gff_file" == *.gz ]]; then
    gunzip -c "$gff_file" | calculate_feature_stats
else
    calculate_feature_stats < "$gff_file"
fi
