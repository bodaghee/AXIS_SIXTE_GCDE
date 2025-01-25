#!/bin/bash

# Input parameters
evt_file='GC_AXIS_100000_evt.fits'
xml_file='/Users/arash/astro/heasoft/sixte/share/sixte/instruments/axis/axis_baseline_all_chips.xml'
att_file='GC_AXIS_100000_att.fits'
roll='75.306'
sim_file='GC.simput'
t_exp='100000'

# Run the command
sixtesim \
    EvtFile=${evt_file} \
    XMLFile=${xml_file} \
    Attitude=${att_file} \
    rollangle=${roll} \
    Simput=${sim_file} \
    Exposure=${t_exp} \
    clobber=yes