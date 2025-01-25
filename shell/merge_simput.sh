#!/bin/bash

# Input list of point sources and starting row
src_list="src_list.txt"
start_row="15"

# Input SIMPUT file of diffuse source
diffuse_file='diffuse.simput'

# Output SIMPUT file
output_file="GC.simput"

# Initialize an empty csv_string starting with the diffuse source
csv_string="${diffuse_file}"

# Read the source list starting from the specified row
tail -n +${start_row} "${src_list}" | while IFS=' ' read -r id ra dec soft hard
do
    # Append the current ID with ".simput" to the csv_string
    csv_string="${csv_string},${id}.simput"
done

# Run the command
simputmerge \
    Infiles=${csv_string} \
    Outfile=${output_file} \
    FetchExtensions=yes \
    clobber=yes