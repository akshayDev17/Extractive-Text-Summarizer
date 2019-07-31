""" As the name suggests, it tries to read the file, and
throws errors if unable to do the same"""

import sys
import os

def read_file():

    """Return the contents of the file, provided that the file exists
    and is readable """

    num_arg = len(sys.argv)
    if num_arg != 3:
        print("please enter a valid file name and desired summary length")
        return None
    else:
        file_name = sys.argv[1]
        if not os.path.exists(file_name):
            print("Please enter a valid path, current path does not contain a file")
            return None
        elif not os.access(file_name, os.R_OK):
            print("Please provide read permissions for the desired file")
            return None
        else:
            with open(file_name) as file_pointer:
                return file_pointer.read()
