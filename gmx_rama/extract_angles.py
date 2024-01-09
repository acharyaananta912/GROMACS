import os
import numpy as np
import pandas as pd
from read_xvg.process_xvg_file import process_xvg_file
from read_xvg.remove_file_extension import remove_extension_name
from read_xvg.remove_file_extension import add_file_extension


# generates from xvg in the form of phi, psi and residues
def rama(filename, csv=False):
    data: ndarray = process_xvg_file(filename)
    phi = data[:, 0].astype(np.float64)
    psi = data[:, 1].astype(np.float64)
    res = data[:, 2].astype(str)
    df = pd.DataFrame({'phi': phi, 'psi': psi, 'res': res})

    if csv:
        new_file_name = os.path.join(os.getcwd(), "output", "gmx_rama",
                                     add_file_extension(remove_extension_name(filename), "csv"))
        df.to_csv(new_file_name, index=False)
    return df
