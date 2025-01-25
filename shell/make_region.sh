#!/bin/bash

# Input file and starting row
src_list="src_list.txt"
start_row="15"

# Output region file
output_file="src_list_RADEC.reg"

# Write the header to the output file
echo "# Region file format: DS9 version 4.1" > "${output_file}"
echo "global color=green width=1" >> "${output_file}"
echo "fk5" >> "${output_file}"

# Read each row of the source list beginning from start_row
tail -n +${start_row} "${src_list}" | while IFS=' ' read -r id ra dec soft hard
do
    # Append each row to the output file
    echo "circle(${ra},${dec},2\")" >> "${output_file}"
done
