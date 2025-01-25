""" make_simput.py """


### IMPORT PACKAGES ###

import subprocess


### LOAD INPUT DATA ###

import config           # load all parameter values set in config.py enabling them to be called:
                        # e.g., config.inst (='AXIS'), config.target (='GC'), etc.


### FUNCTIONS TO CREATE SIMPUT FILES ###

def make_simput_point():
    """ Create a SIMPUT file for each point source of a catalog using parameter values from config.py. """ 
    for i in range(len(config.point_src_name)):
        # Print status to the terminal
        announcement = str('Working on source '+str(config.point_src_name[i])+' ('+str(i)+'/'+str(len(config.point_src_name)-1))+')'
        print(announcement)
        # Build the full SIMPUTFILE command line for the i-th point source using parameter values from config.py
        cmd = [
            'simputfile',
            f'Simput={str(config.point_src_name[i])}.simput',   # output SIMPUT catalog file
            f'Src_Name={str(config.point_src_name[i])}',        # source name
            f'RA={str(config.point_src_ra[i])}',                # right ascension (deg)
            f'Dec={str(config.point_src_dec[i])}',              # declination (deg)
            f'srcFlux={str(config.point_src_flux[i])}',         # source flux (erg/s/cm^2)
            f'Elow={str(config.elow)}',                         # lower bound of the generated spectrum (keV)
            f'Eup={str(config.eup)}',                           # upper bound of the generated spectrum (keV)
            f'NBins={str(config.nbins)}',                       # number of energy bins created from Elow to Eup
            f'Emin={str(config.point_src_emin)}',               # E_min of reference energy band for fluxes (keV)
            f'Emax={str(config.point_src_emax)}',               # E_max of reference energy band for fluxes (keV)
            f'XSPECFile={str(config.point_src_xspec)}',         # XSpec spectral model file (*.xcm)
            f'clobber={str(config.clobber)}',                   # overwrite output files if exist?
        ]
        # Run SIMPUTFILE in the terminal using the full command line
        result = subprocess.run(cmd, capture_output=True, text=True, check=True)
        print(f"stdout: {result.stdout}")
        print(f"stderr: {result.stderr}")
        result.check_returncode()


def make_simput_diffuse():
    """ Create a SIMPUT file for an input image of diffuse emission using parameter values from config.py. """
    # Build the full SIMPUTFILE command line for the diffuse emission using parameter values from config.py
    cmd = [
        'simputfile',
        f'Simput={str(config.diffuse_src_simput_file_name)}',   # output SIMPUT catalog file
        f'Src_Name={str(config.diffuse_src_name)}',             # source name
        f'RA={str(config.diffuse_src_ra)}',                     # right ascension (deg)
        f'Dec={str(config.diffuse_src_dec)}',                   # declination (deg)
        f'srcFlux={str(config.diffuse_src_flux)}',              # source flux (erg/s/cm^2)
        f'Elow={str(config.elow)}',                             # lower bound of the generated spectrum (keV)
        f'Eup={str(config.eup)}',                               # upper bound of the generated spectrum (keV)
        f'NBins={str(config.nbins)}',                           # number of energy bins created from Elow to Eup
        f'Emin={str(config.diffuse_src_emin)}',                 # E_min of reference energy band for fluxes (keV)
        f'Emax={str(config.diffuse_src_emax)}',                 # E_max of reference energy band for fluxes (keV)
        f'XSPECFile={str(config.diffuse_src_xspec)}',           # XSpec spectral model file (*.xcm)
        f'ImageFile={str(config.diffuse_src_img)}',             # FITS file containing an image of the spatial flux distribution
        f'clobber={str(config.clobber)}',                       # overwrite output files if exist?
    ]
    # Run SIMPUTFILE in the terminal using the full command line
    result = subprocess.run(cmd, capture_output=True, text=True, check=True)
    print(f"stdout: {result.stdout}")
    print(f"stderr: {result.stderr}")
    result.check_returncode()


def main():

    make_simput_point()

    make_simput_diffuse()

if __name__ == "__main__":
    main()