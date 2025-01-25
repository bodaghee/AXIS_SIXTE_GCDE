#!/bin/bash

# Input parameters
att_file='GC_AXIS_100000_att.fits'
amp='0.035'
ra='266.417'
dec='-29.008'
t_exp='100000'

# Run the command
attgen_dither \
    Attitude=${att_file} \
    Amplitude=${amp} \
    SrcRA=${ra} \
    SrcDec=${dec} \
    Exposure=${t_exp}