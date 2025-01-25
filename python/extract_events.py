""" extract_events.py """


### IMPORT PACKAGES ###

import subprocess


### LOAD INPUT DATA ###

import config           # load all parameter values set in config.py enabling them to be called:
                        # e.g., config.inst (='AXIS'), config.target (='GC'), etc.


### FUNCTION TO EXTRACT EVENTS FILE FOR DIFFERENT BANDS ###

def extract_events_per_band(pha_min,pha_max):
    """ Uses FTCOPY to create a new events file restricted to input values of PHA channel pha_min and pha_max. """
    # Create command string for FTCOPY using input values
    cmd = [
        'ftcopy',
        f'infile={config.evt_file_name}[EVENTS][PHA >= {pha_min} && PHA < {pha_max}]',              # input events file and PHA channels
        f'outfile={config.target}_{config.inst}_{config.t_exp}_evt_PHA_{pha_min}_{pha_max}.fits',   # output events file
        f'clobber={str(config.clobber)}',                                                           # overwrite output files if exist?
    ]
    # Run FTCOPY in the terminal using the full command line
    result = subprocess.run(cmd, capture_output=True, text=True, check=True)
    print(f"stdout: {result.stdout}")
    print(f"stderr: {result.stderr}")
    result.check_returncode()


def main():

    # Using values from the RMF, extract events from: 
    #   0.5-3.3 keV (PHA: 40-320), 
    #   3.3-4.7 keV (PHA: 320-460),
    #   4.7-8 keV (PHA: 460-790)

    extract_events_per_band(40,320)

    extract_events_per_band(320,460)

    extract_events_per_band(460,790)

if __name__ == '__main__':
    main()
