#!usr/bin/python3
#extract_max_interactions.py

from glob import glob
from re import compile
from sys import argv
from os import path, chdir

# For Debugging
from pprint import pprint

def main():
    sec_header_str = 'SECOND ORDER PERTURBATION'
    sec_end_srt = 'NATURAL BOND ORBITALS'
    outfiles = glob('*.out')
    text_dict = {}
    for filename in outfiles:
        section_flag = False
        with open(filename,'r') as f:
            for line in f.readlines():
                if flag:
                    if 'from' in line:
                        

def get_single_dir_arg():
    num_args = len(argv)
    target_dir = '.'
    if len == 1: 
        pass
    elif len == 2: 
        target_dir = argv[1]
        if not os.path.isdir(target_dir):
            errmsg = ('{} '
                      'is not a directory.').format(target_dir)
            raise NotADirectoryError(errmsg)
    else: 
        raise TypeError('Too many arguments passed; '
                        'only one expected.')
    return target_dir

if __name__ == "__main__":
    directory = get_single_dir_arg()
    os.chdir(directory)
    main()
