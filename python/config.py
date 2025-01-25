""" config.py """
""" All parameter values are set here. """


### IMPORT PACKAGES ###

import numpy as np


### INSTRUMENT SETTINGS ###

inst = 'AXIS'                                               # short name of instrument
elow = 0.1                                                  # from RMF: minimum energy (keV)
eup = 15                                                    # from RMF: maximum energy (keV)
nbins = 1490                                                # from RMF: number of energy bins
NAXIS1 = 2880                                               # from XML: pixels per x-axis
NAXIS2 = 2880                                               # from XML: pixels per y-axis
CRPIX1 = 1440.5                                             # from XML: pixel value of x=0
CRPIX2 = 1440.5                                             # from XML: pixel value of y=0
CUNIT1 = 'deg'                                              # coordinate units of x axis
CUNIT2 = 'deg'                                              # coordinate units of y axis
CDELT1 = -2.4e-04                                           # from XML: pixel size (deg)
CDELT2 = 2.4e-04                                            # from XML: pixel size (deg)
projection = 'TAN'                                          # projection for the simulation
coord_system = 0                                            # coordinate system: 0 = equatorial; 1 = galactic
clobber = 'yes'                                             # overwrite output files


### TARGET/OBSERVATION SETTINGS ###

target = 'GC'	                                            # target (used as a prefix for file naming)
fov_ra = 266.417                                            # center of FoV (deg)
fov_dec = -29.008                                           # center of FoV (deg)
fov_roll = 75.306                                           # roll-angle of telescope (deg)
t_exp = 100000                                              # exposure time (sec)
dt = 1000                                                   # time step for the exposure map calculation (sec) 
amp = 0.035                                                 # amplitude of the dithering pattern (deg)


### FILE-NAMING SCHEME ###

sixte_loc = '/Users/arash/astro/heasoft/sixte/share/sixte/instruments/axis/'        # location of instrument-specific SIXTE files
xml_file_name = sixte_loc+'axis_baseline_all_chips.xml'     # location and name of XML file
vig_file_name = sixte_loc+'sixte_calibration_files/axis_vignetting_20230821.fits'   # from XML: location and name of vignetting file
att_file_name = target+'_'+inst+'_'+str(t_exp)+'_att.fits' 	# name of output attitude file to be written
evt_file_name = target+'_'+inst+'_'+str(t_exp)+'_evt.fits' 	# name of output events file to be written
img_file_name = target+'_'+inst+'_'+str(t_exp)+'_img.fits'	# name of output image file to be written
exp_file_name = target+'_'+inst+'_'+str(t_exp)+'_exp.fits'	# name of output exposure map file to be written
all_src_simput_file_name = target+'.simput'                 # name of output SIMPUT file to be written for all sources


### PARAMETERS FOR THE DIFFUSE EMISSION ###

diffuse_src_name = 'diffuse'                                # name of the diffuse emission
diffuse_src_img = 'sgra_200-8000_eV_diffuse.fits'           # file name of the diffuse emission image
diffuse_src_ra = fov_ra                                     # R.A. of the emission (deg)
diffuse_src_dec = fov_dec                                   # Dec. of the emission (deg)
diffuse_src_xspec = 'sed_diffuse.xcm'                       # name of the XSPEC file for the diffuse emission
diffuse_src_emin = 0.5                                      # (keV) from the SED in the XSPEC file
diffuse_src_emax = 8                                        # (keV) from the SED in the XSPEC file
diffuse_src_flux = 1.4E-10                                  # (erg/cm2/s) from Muno et al. (2004) 
diffuse_src_simput_file_name = diffuse_src_name+'.simput'   # name of output SIMPUT file for diffuse sources


### PARAMETERS FOR THE POINT SOURCES ###

point_src_list = 'src_list_temp.txt'                 # name of the point source catalog
point_src_head = 14                             # number of header lines in the point source catalog that should be ignored
point_src_dtype = [                             # column names and corresponding data types
    ('name', 'U15'),
    ('ra', 'f8'),
    ('dec', 'f8'),
    ('S', 'f8'),
    ('H', 'f8'),
]
point_src_data = np.genfromtxt(                 # store the point source catalog as a numpy array
    point_src_list,                             # the point source catalog to be stored
    delimiter=None,                             # the catalog is space delimited (or the delimiter will be found automatically)
    skip_header=point_src_head,                 # skip the header rows as defined by point_src_head parameter of config.py
    dtype=point_src_dtype,                      # assign custom column names and data types as defined by point_src_dtype parameter of config.py
    encoding=None                               # handle string data correctly
) 
point_src_name = point_src_data['name']         # the following lines store the point source array into individual columns for ease of use
point_src_ra = point_src_data['ra']             # ibid
point_src_dec = point_src_data['dec']           # ibid
point_src_S = point_src_data['S'].clip(min=0)   # ibid; plus, negative flux values are reset to 0 so they don't interfere with the summed flux
point_src_H = point_src_data['H'].clip(min=0)   # ibid
point_src_flux_conv = 8.7E-9                    # 1 ph/cm2/s = 8.7E-9 erg/cm2/s (0.5-8 keV) from Muno et al. (2009)
point_src_flux = (point_src_S + point_src_H) * point_src_flux_conv # add photon fluxes to obtain full E-band value then convert to erg/cm2/s   
point_src_xspec = 'sed_point.xcm'               # name of the XSPEC file for the point sources
point_src_emin = 0.5                            # (keV) from the SED in the XSPEC file
point_src_emax = 8                              # (keV) from the SED in the XSPEC file
point_src_simput_file_name = 'point.simput'     # name of output SIMPUT file for point sources
point_src_region_file_name = 'src_list_RADEC.reg'   # name of output DS9 region file for point sources (equatorial coordinates)
point_src_regionXY_file_name = 'src_list_XY.reg'    # name of output DS9 region file for point sources (Chandra detector physical coordinates)