""" merge_simput.py """


### IMPORT PACKAGES ###

import subprocess


### LOAD INPUT DATA ###

import config           # load all parameter values set in config.py enabling them to be called:
                        # e.g., config.inst (='AXIS'), config.target (='GC'), etc.


### FUNCTION TO MERGE SIMPUT FILES ###

def merge_simput_files():
    """ Merge SIMPUT files of diffuse and point sources using SIMPUTMERGE """
    # Create a list of all source SIMPUT file names
    all_src_simput_list = []
    # Append the diffuse source to this list
    all_src_simput_list.append(config.diffuse_src_simput_file_name)
    # Iterate through all point sources
    for i in range(len(config.point_src_name)):
        # Name of the SIMPUT file of this specific source
        point_src_simput = config.point_src_name[i]+'.simput'  
        # Append this SIMPUT file to the end of the list      
        all_src_simput_list.append(point_src_simput)
    # Convert list of all source SIMPUT files to a CSV string
    all_src_simput_list_csv = ','.join(all_src_simput_list)
    # Create command string for SIMPUTMERGE
    cmd = [
        'simputmerge',
        f'Infiles={str(all_src_simput_list_csv)}',              # comma separated list of input SIMPUT files
        f'Outfile={str(config.all_src_simput_file_name)}',      # output SIMPUT file
        f'clobber={str(config.clobber)}',                       # overwrite output files if exist?
    ]
    # Run SIMPUTMERGE in the terminal using the full command line
    result = subprocess.run(cmd, capture_output=True, text=True, check=True)
    print(f"stdout: {result.stdout}")
    print(f"stderr: {result.stderr}")
    result.check_returncode()


def main():

    merge_simput_files()

if __name__ == "__main__":
    main()