""" make_region.py """


### IMPORT PACKAGES ###

import numpy as np


# FUNCTION TO CREATE REGION FILE

def make_region_file(src_list, reg_file):
    """ 
    Makes a DS9 region file from an input source catalog in the Vizier ASCII/txt format. 
    The parameters src_list_head and src_list_dtype must be edited to reflect 
    the header rows and data structure of the input table.

    Args:   
        src_list (string): input table in Vizier ASCII/txt format (e.g., 'src_list.txt')
            
    Returns: 
        reg_file (string): output region file compatible with DS9  (e.g., 'src_list_RADEC.reg')
    """
    src_list_head = 14                  # number of header lines in the point source catalog that should be ignored
    src_list_dtype = [                  # column names and corresponding data types
        ('name', 'U15'),
        ('ra', 'f8'),
        ('dec', 'f8'),
        ('S', 'f8'),
        ('H', 'f8'),
    ]
    src_data = np.genfromtxt(           # store the point source catalog as a numpy array
        src_list,                       # the input point source catalog 
        delimiter=None,                 # the catalog is space delimited (or the delimiter will be found automatically)
        skip_header=src_list_head,      # skip the header rows as defined by src_list_head
        dtype=src_list_dtype,           # assign custom column names and data types as defined by src_list_dtype
        encoding=None                   # handle string data correctly
    ) 
    # extract the RA and Dec columns into a new numpy array
    reg_array = np.stack((src_data['ra'],src_data['dec']),axis=1)
    # open the region file and write header lines
    with open(reg_file, 'w') as f:
        f.write('# Region file format: DS9 version 4.1\n')
        f.write('global color=green width=1\n')
        f.write('fk5\n')
    # append reg_array to region file and format
    with open(reg_file, 'a') as f:
        np.savetxt(f,reg_array, fmt='circle(%8.5f,%8.5f,2\")')
        f.close()


def main():

    make_region_file('src_list.txt','src_list_RADEC.reg')

if __name__ == '__main__':
    main()