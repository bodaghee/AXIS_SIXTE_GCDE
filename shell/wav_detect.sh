#!/bin/bash

# Input parameters
prefix='GC_AXIS_100000'

# Run the command
punlearn wavdetect
wavdetect \
 infile=${prefix}_img.fits \
 outfile=${prefix}_wavsrc.fits \
 scellfile=${prefix}_scell.fits \
 imagefile=${prefix}_wavimg.fits \
 defnbkgfile=${prefix}_wavnbgd.fits \
 psffile=${prefix}_psf.fits \
 expfile=${prefix}_exp.fits \
 regfile=${prefix}_wavsrc.reg \
 scales="1.0 2.0 4.0 8.0 16.0" \
 clobber=yes
