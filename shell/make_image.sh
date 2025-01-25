#!/bin/bash

# Input parameters
evt_file='GC_AXIS_100000_evt.fits'
img_file='GC_AXIS_100000_img.fits'
coord='0'
projection='TAN'
naxis='2880'
cunit='deg'
ra='266.417'
dec='-29.008'
crpix='1440.5'
cdelt='2.4e-04'

# Run the command
imgev \
    EvtFile=${evt_file} \
    Image=${img_file} \
    CoordinateSystem=${coord} Projection=${projection} \
    NAXIS1=${naxis} NAXIS2=${naxis} \
    CUNIT1=${cunit} CUNIT2=${cunit} \
    CRVAL1=${ra} CRVAL2=${dec} \
    CRPIX1=${crpix} CRPIX2=${crpix} \
    CDELT1=-${cdelt} CDELT2=${cdelt} \
    clobber=yes