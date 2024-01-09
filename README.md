# GROMACS
*** Working directory should be GROMACS ***

Ramachandran angle analysis is important in structural study of proteins. This code helps in Ramachandran analysis from the output of "gmx rama" command in GROMACS. A protein has several amino-acids in a single frame of protein structure, and gmx rama outputs changing angles in tragectory of Molecular Dynamics Simulations.

The code takes several inputs from the user:

filename: ("rama.xvg: sample file) it requires to input .xvg file we want to analyze. .xvg file should be present in GROMACS/input folder.

csv_generate: this command takes boolean input as 0/1. 1 outputs .csv file in GROMACS/output folder which can be useful later.

frame_selection: Not all frames of the trajectory are important. This input allows to select the range of trajactory. Start_frame allows to select the frame of trajectory from where we need to analyze. Input can be 0 or any other integer less than total frames present in the trajactory. End_frame allows to select the end of the trajactory. It takes -1 or other specific frame number in the trajactory. And Skip_frame allows to select the number of frames to skip between trajactory.

Plot individual or all amino acids in a plot: Plot individual allows to plot individual amino-acid angles. A protein of 10 amino-acids outputs 10 different figures with each amino-acids. However plot all amino-acids in a single figure outputs a figure which includes all the amino-acids.

Amino-acids range: User can be interested in certain section of protein instead of whole protein. This selection helps to select certain section using three letter code and position, example "ALA-1". And plot all selected amino-acids in a single figure or multiple figure

## run run_file.py to run the program
### required modules: numpy, pandas and matplotlib

