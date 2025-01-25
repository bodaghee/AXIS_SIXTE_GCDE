""" make_events.py """


### IMPORT PACKAGES ###

import subprocess


### LOAD INPUT DATA ###

import config           # load all parameter values set in config.py enabling them to be called:
                        # e.g., config.inst (='AXIS'), config.target (='GC'), etc.


# FUNCTION TO CREATE EVENTS FILE

def make_events_file():
    """ Generate events file (broadband: 0.5-8 keV) from SIMPUT files using the SIXTE command SIXTESIM """
    # Create command string for SIXTESIM using paramater values from config.py
    cmd = [
        'sixtesim',
        f'EvtFile={str(config.evt_file_name)}',             # cleaned event output file
        f'XMLFile={str(config.xml_file_name)}',             # XML input file(s) with instrument definition
        f'Attitude={str(config.att_file_name)}',            # attitude input file (overwrites RA and Dec)
        f'RA={str(config.fov_ra)}',                         # right ascension of telescope pointing (degree)
        f'Dec={str(config.fov_dec)}',                       # declination of telescope pointing (degree)
        f'rollangle={str(config.fov_roll)}',                # roll angle of telescope pointing (degree)
        f'Simput={str(config.all_src_simput_file_name)}',   # SIMPUT catalog(s)
        f'Exposure={str(config.t_exp)}',                    # exposure time (s)
        f'clobber={str(config.clobber)}',                   # overwrite output files if exist?
    ]
    # Run SIXTESIM in the terminal using the full command line
    result = subprocess.run(cmd, capture_output=True, text=True, check=True)
    print(f"stdout: {result.stdout}")
    print(f"stderr: {result.stderr}")
    result.check_returncode()


def main():

    make_events_file()

if __name__ == "__main__":
    main()