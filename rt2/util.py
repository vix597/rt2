'''
Helpful utilities for rt2
'''

import os
import sys
import random


def generate_secret_key_file(path):
    '''
    Generate the secret key/file
    '''
    k = ''.join(random.SystemRandom().choice('abcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*(-_=+)') for i in range(50))
    try:
        with open(path, 'w') as outfile:
            outfile.write(k)
    except BaseException as ex:  # pragma: no cover
        print("Unable to create secret key file: ", str(ex))
        sys.exit(-1)

    return k


def read_secret_key(path):
    '''
    Load the secret key from a file
    '''
    try:
        with open(path, 'r') as infile:
            return infile.read()
    except BaseException as ex:  # pragma: no cover
        print("Unable to load secret key from file: ", str(ex))
        sys.exit(-1)


def get_secret_key(path):
    '''
    Handles getting the secret key in production/debug mode
    '''

    if not os.path.exists(path):
        print("Secret key file {} not found. Creating...".format(path))
        return generate_secret_key_file(path)

    print("Loading secret key from file {}.".format(path))
    return read_secret_key(path)
