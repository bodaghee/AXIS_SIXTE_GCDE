""" make_attitude.py """


### IMPORT PACKAGES ###

import subprocess


### LOAD INPUT DATA ###

import config           # load all parameter values set in config.py enabling them to be called:
                        # e.g., config.inst (='AXIS'), config.target (='GC'), etc.


# FUNCTION TO CREATE ATTITUDE FILE

def make_attitude_file():
    """ Generate dithering attitude file using the SIXTE command attgen_dither """
    # Create command string for attgen_dither using paramater values from config.py
    cmd = [
        'attgen_dither',
        f'Attitude={str(config.att_file_name)}',            # attitude input file (overwrites RA and Dec)
        f'SrcRA={str(config.fov_ra)}',                      # center of the Lissajous pattern in RA (degree)
        f'SrcDec={str(config.fov_dec)}',                    # center of the Lissajous pattern in Dec (degree)
        f'Amplitude={str(config.amp)}',                     # amplitude of the dithering (degree)
        f'Exposure={str(config.t_exp)}',                    # regarded time interval (s); nbins=1000 by default
        f'clobber={str(config.clobber)}',                   # overwrite output files if exist?
    ]
    # Run attgen_dither in the terminal using the full command line
    result = subprocess.run(cmd, capture_output=True, text=True, check=True)
    print(f"stdout: {result.stdout}")
    print(f"stderr: {result.stderr}")
    result.check_returncode()


def main():

    make_attitude_file()

if __name__ == "__main__":
    main()