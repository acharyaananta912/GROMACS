import sys
import os
from gmx_rama.extract_angles import rama
from gmx_rama.frame_selection.all_frame import frame_selection
from gmx_rama.frame_selection.separating_residues_and_frames import res_frames_separate
from gmx_rama.plot_rama import plot_ramachandran_all
from gmx_rama.plot_rama import plot_ramachandran_individual_all
from gmx_rama.plot_rama import plot_ramachandran_range_all
from gmx_rama.plot_rama import plot_ramachandran_range_individual

filename = str(input("Please enter filename. Filename is expected to be .xvg file inside /GROMACS/input folder: "))
csv_generate = bool(int(input("Generate .csv file from .xvg file? Type 1 for YES and 0 for NO: " )))
print("Please Wait! Processing file.....")
df = rama(filename,csv_generate)
print("csv generated, check output/gmx_rama folder. Not applicable if no csv command was given.")
amino_acid_dictionary, unique_amino_acids, total_amino_acids, total_frames = res_frames_separate(df)
print("Loaded file consists", total_frames, "frames with", total_amino_acids, "in each frame")
frame_start = int(input("Enter initial frame to extract. For example: 0 for 1st frame 6 for 6th frame: "))
frame_end = int(input("Enter the final frame to extract. For example:-1 to extract upto last frame 10 to extract upto "
                      "10th frame: "))
skip_frames = int(input("Number of frame to skip after a frame. 0 = no skipping, 1 = jumps from 1st frame to 3rd, "
                        "2 = jumps from 1st frame to 4th.: "))
print("Please wait! Loading... ")
modified_dictionary = frame_selection(amino_acid_dictionary, total_frames, frame_start, frame_end, skip_frames)
plot_all = bool(int(input("Plot ramachandran angles for whole protein or section? for whole protein type 1 for section "
                      "type 0: " )))
transparency = float(input("Enter transparency of dots. For example: 0.5: "))
size_of_dots = float(input("Enter size of dots. For example: 0.5: "))
color = str(input("Enter color of dots. For example: red, blue, green: "))
print(plot_all)
if plot_all:
    all_or_indv_plot = bool(int(input("Plot all protein in a single plot or plot each amino acid individually? Type 1 for "
                                  "all protein type 0 for individual amino acids.: ")))
    print(all_or_indv_plot)

    if all_or_indv_plot:
        print("Please Wait! Generating figures....")
        plot_ramachandran_all(modified_dictionary, unique_amino_acids, transparency, size_of_dots, color)
        print("Figure generated. CHeck output/gmx_rama folder")
    else:
        print("Please Wait! Generating figures....")
        plot_ramachandran_individual_all(modified_dictionary, unique_amino_acids,transparency, size_of_dots, color)
        print("Figures generated. CHeck output/gmx_rama/individual_plots folder")

else:
    print("These are the amino-acids with position present in protein",unique_amino_acids)
    start_range = str(input("Enter starting residue: "))
    end_range = str(input("Enter ending residue: "))
    all_or_indv_plot = bool(int(input("Plot all in range in a single plot or plot each amino acid in range "
                                      "individually?"
                                  "Type 1 for all in range type 0 for individual amino acids.")))
    if all_or_indv_plot:
        print("Please Wait! Generating figures....")
        plot_ramachandran_range_all(modified_dictionary, unique_amino_acids, start_range,end_range, transparency, size_of_dots, color)
        print("Figure generated. CHeck output/gmx_rama/range_plots folder")
    else:
        print("Please Wait! Generating figures....")
        plot_ramachandran_range_individual(modified_dictionary, unique_amino_acids, start_range, end_range, transparency, size_of_dots, color)
        print("Figure generated. CHeck output/gmx_rama/range_plots/individual_plots folder")
