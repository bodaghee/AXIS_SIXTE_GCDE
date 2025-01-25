#!/bin/bash

# Input source list and parameters
src_list="src_list.txt"
start_row="15"
xspec="sed_point.xcm"
elow="0.1"
eup="15"
nbins="1490"
emin="0.5"
emax="8"
fluxconv="8.7e-9"

# Read file starting from row number "start_row"
tail -n +${start_row} "${src_list}" | while IFS=' ' read -r id ra dec soft hard
do
    
    # Apply clipping: set soft and hard to 0 if they are less than 0
    if (( $(echo "$soft < 0" | bc -l) )); then
        soft=0
    fi

    if (( $(echo "$hard < 0" | bc -l) )); then
        hard=0
    fi
    
    # Calculate total photon flux (flux) as the sum of soft and hard
    flux=$(echo "$soft + $hard" | bc -l)
    
    # Multiply photon flux by the flux conversion factor to get cgs units
    converted_flux=$(echo "$flux * $fluxconv" | bc -l)
    
    # Format output for scientific notation with 3 decimal places
    formatted_flux=$(printf "%1.3e" $converted_flux)
    
    # Debugging: print the variables for verification
    #echo "ID: $id, RA: $ra, Dec: $dec, soft: $soft, hard: $hard, Flux: $formatted_flux"

    # Run the simputfile command
    simputfile \
        Simput=${id}.simput \
        Src_Name=${id} \
        RA=${ra} \
        Dec=${dec} \
        srcFlux=${formatted_flux} \
        Elow=${elow} \
        Eup=${eup} \
        NBins=${nbins} \
        Emin=${emin} \
        Emax=${emax} \
        XSPECFile=${xspec} \
        clobber=yes
    
done
