#!/bin/bash

# Input parameters
ra='266.417'
dec='-29.008'
roll='75.306'
vig_file='/Users/arash/astro/heasoft/sixte/share/sixte/instruments/axis/sixte_calibration_files/axis_vignetting_20230821.fits'
xml_file='/Users/arash/astro/heasoft/sixte/share/sixte/instruments/axis/axis_baseline_all_chips.xml'
att_file='GC_AXIS_100000_att.fits'
exp_file='GC_AXIS_100000_exp.fits'
t_exp='100000'
t_start='0'
dt='1000'
coord='0'
projection='TAN'
naxis='2880'
cunit='deg'
crpix='1440.5'
cdelt='2.4e-04'

# Run the command
exposure_map \
    RA=${ra} Dec=${dec} rollangle=${roll} \
    Vignetting=${vig_file} \
    XMLFile=${xml_file} \
    Attitude=${att_file} \
    Exposuremap=${exp_file} \
    TSTART=${t_start} timespan=${t_exp} dt=${dt} \
    CoordinateSystem=${coord} projection_type=${projection} \
    NAXIS1=${naxis} NAXIS2=${naxis} \
    CUNIT1=${cunit} CUNIT2=${cunit} \
    CRVAL1=${ra} CRVAL2=${dec} \
    CRPIX1=${crpix} CRPIX2=${crpix} \
    CDELT1=-${cdelt} CDELT2=${cdelt} \
    clobber=yes
