#!/bin/bash

# Input source list and parameters
file_name='diffuse.simput'
src_name='diffuse'
ra='266.417'
dec='-29.008'
flux='1.4e-10'
elow='0.1'
eup='15'
nbins='1490'
emin='0.5'
emax='8'
xspec='sed_diffuse.xcm'
img='sgra_200-8000_eV_diffuse.fits'

# Run the simputfile command
simputfile \
    Simput=${file_name} \
    Src_Name=${src_name} \
    RA=${ra} \
    Dec=${dec} \
    srcFlux=${flux} \
    Elow=${elow} \
    Eup=${eup} \
    NBins=${nbins} \
    Emin=${emin} \
    Emax=${emax} \
    XSPECFile=${xspec} \
    ImageFile=${img} \
    clobber=yes