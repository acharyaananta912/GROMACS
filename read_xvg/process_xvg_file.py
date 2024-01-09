# function to extract required data from .xvg file
import os
import sys
import numpy as np


def process_xvg_file(filename):  # takes .xvg file
    data = []
    filename = os.path.abspath(os.path.join('input', filename))
    with open(filename, 'r') as f:  # opens .xvg file as f
        data = [line.split() for line in f if not line.startswith(('#', '@'))]
    return np.array(data)
