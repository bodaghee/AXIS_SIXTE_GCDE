""" make_image.py """


### IMPORT PACKAGES ###

import subprocess


### LOAD INPUT DATA ###

import config           # load all parameter values set in config.py enabling them to be called:
                        # e.g., config.inst (='AXIS'), config.target (='GC'), etc.


### FUNCTION TO CREATE IMAGE FILE ###

def make_image_file():
    """ Generate full-band image file from an events file using the SIXTE command IMGEV """
    # Create command string for IMGEV using paramater values from config.py
    cmd = [
        'imgev',
        f'EvtFile={str(config.evt_file_name)}',         # cleaned event output file (equivalent to level 2 or filtered event files)
        f'Image={str(config.img_file_name)}',           # output image file
        f'CoordinateSystem={str(config.coord_system)}', # coordinate system (0: equatorial, 1: galactic)
        f'Projection={str(config.projection)}',         # projection type
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
    # Run IMGEV in the terminal using the full command line
    result = subprocess.run(cmd, capture_output=True, text=True, check=True)
    print(f"stdout: {result.stdout}")
    print(f"stderr: {result.stderr}")
    result.check_returncode()


def main():

    make_image_file()

if __name__ == '__main__':
    main()