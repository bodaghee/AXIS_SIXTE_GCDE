""" make_exposure.py """


### IMPORT PACKAGES ###

import subprocess


### LOAD INPUT DATA ###

import config           # load all parameter values set in config.py enabling them to be called:
                        # e.g., config.inst (='AXIS'), config.target (='GC'), etc.


### FUNCTION TO CREATE EXPOSURE MAP FILE ###

def make_exposure_map():
    """ Generate an exposure map from an events file using the SIXTE command EXPOSURE_MAP """
    # Create command string for EXPOSURE_MAP using paramater values from config.py
    cmd = [
        'exposure_map',
        f'RA={str(config.fov_ra)}',                     # R.A. of telescope pointing (deg)
        f'Dec={str(config.fov_dec)}',                   # Dec. of telescope pointing (deg)
        f'rollangle={str(config.fov_roll)}',            # roll angle of telescope pointing (deg)
        f'Vignetting={str(config.vig_file_name)}',      # Vignetting data file (FITS input file)
        f'Attitude={str(config.att_file_name)}',        # Attitude input file (overwrites RA and Dec)
        f'XMLFile={str(config.xml_file_name)}',         # XML input file with detector definition
        f'Exposuremap={str(config.exp_file_name)}',     # exposure map file (FITS output file)
        'TSTART=0',                                     # start time (s)
        f'timespan={str(config.t_exp)}',                # time interval for the exposure map calculation (s)
        f'dt={str(config.dt)}',                         # time step for the exposure map calculation (s)
        f'CoordinateSystem={str(config.coord_system)}', # coordinate system (0: equatorial, 1: galactic)
        f'projection_type={str(config.projection)}',    # projection type (TANtop)
        f'NAXIS1={str(config.NAXIS1)}',                 # pixels per x-axis
        f'NAXIS2={str(config.NAXIS2)}',                 # pixels per y-axis
        f'CUNIT1={str(config.CUNIT1)}',                 # coordinate units of x axis
        f'CUNIT2={str(config.CUNIT2)}',                 # coordinate units of y axis
        f'CRVAL1={str(config.fov_ra)}',                 # RA of central pixel
        f'CRVAL2={str(config.fov_dec)}',                # Dec of central pixel 
        f'CRPIX1={str(config.CRPIX1)}',                 # pixel value of x=0
        f'CRPIX2={str(config.CRPIX2)}',                 # pixel value of y=0
        f'CDELT1={str(config.CDELT1)}',                 # pixel size in degs
        f'CDELT2={str(config.CDELT2)}',                 # pixel size in degs
        f'clobber={str(config.clobber)}',               # overwrite output files if exist?
    ]
    # Run EXPOSURE_MAP in the terminal using the full command line
    result = subprocess.run(cmd, capture_output=True, text=True, check=True)
    print(f"stdout: {result.stdout}")
    print(f"stderr: {result.stderr}")
    result.check_returncode()
    #result = subprocess.run(cmd, capture_output=True, text=True, shell=True)
    #print(f"Return Code: {result.returncode}")
    #print(f"Stdout: {result.stdout}")
    #print(f"Stderr: {result.stderr}")


def main():

    make_exposure_map()

if __name__ == '__main__':
    main()