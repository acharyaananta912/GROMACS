import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from read_xvg.remove_file_extension import add_file_extension


def plot_ramachandran_all(dictionary, unique_amino_acids, transparency, size_of_dots, color):
    for item in unique_amino_acids:
        plt.scatter(dictionary[item].values[:, 0], dictionary[item].values[:, 1], alpha=transparency,
                    s=size_of_dots, color=color)
    plt.xlim(-180, 180)
    plt.ylim(-180, 180)
    plt.xlabel("$\phi$")
    plt.ylabel("$\psi$")
    plt.title("Ramachandran Plot")
    plt.savefig(os.path.join(os.getcwd(), "output", "gmx_rama",
                             "Ramachandran_plot.png"))


def plot_ramachandran_individual_all(dictionary, unique_amino_acids, transparency, size_of_dots, color):
    for item in unique_amino_acids:
        plt.scatter(dictionary[item].values[:, 0], dictionary[item].values[:, 1], alpha=transparency,
                    s=size_of_dots, color=color)
        plt.xlim(-180, 180)
        plt.ylim(-180, 180)
        plt.xlabel("$\phi$")
        plt.ylabel("$\psi$")
        plt.title(item)
        plt.savefig(os.path.join(os.getcwd(), "output", "gmx_rama", "individual_plots",
                                 add_file_extension(item, "png")))
        plt.close()


def plot_ramachandran_range_all(dictionary, unique_amino_acids, start_range, end_range, transparency, size_of_dots,color):
    for item in unique_amino_acids[np.where(unique_amino_acids == start_range)[0][0]:np.where(unique_amino_acids == end_range)[0][0]+1]:
        plt.scatter(dictionary[item].values[:, 0], dictionary[item].values[:, 1], alpha=transparency,
                    s=size_of_dots, color=color)
    plt.xlim(-180, 180)
    plt.ylim(-180, 180)
    plt.xlabel("$\phi$")
    plt.ylabel("$\psi$")
    plt.title("Ramachandran Plot")
    plt.savefig(os.path.join(os.getcwd(), "output", "gmx_rama", "range_plots",
                             "Ramachandran_plot_range.png"))
    plt.close()


def plot_ramachandran_range_individual(dictionary, unique_amino_acids, start_range, end_range, transparency, size_of_dots,color):
    for item in unique_amino_acids[np.where(unique_amino_acids == start_range)[0][0]:np.where(unique_amino_acids == end_range)[0][0]+1]:
        plt.scatter(dictionary[item].values[:, 0], dictionary[item].values[:, 1], alpha=transparency,
                    s=size_of_dots, color=color)
        plt.xlim(-180, 180)
        plt.ylim(-180, 180)
        plt.xlabel("$\phi$")
        plt.ylabel("$\psi$")
        plt.title("Ramachandran Plot")
        plt.savefig(os.path.join(os.getcwd(), "output", "gmx_rama", "range_plots", "individual_plots",
                                 add_file_extension(item, "png")))
        plt.close()
