from gmx_rama.extract_angles import rama


def res_frames_separate(dataframe): #data frame comes as df from rama
    # Getting unique amino acids from the frame
    unique_amino_acids = dataframe["res"].unique()
    # Creating a dictionary to store DataFrames for each amino acid
    amino_acid_dictionary = {}
    for amino_acid in unique_amino_acids:
        # Creating a DataFrame for the each amino acid
        amino_acid_df = dataframe[dataframe["res"] == amino_acid].copy()
        # Resetting the indices
        amino_acid_df.reset_index(drop=True, inplace=True)
        # Adding DataFrame to a dictionary with the amino acid name as the key
        amino_acid_dictionary[amino_acid] = amino_acid_df
    return amino_acid_dictionary, unique_amino_acids, len(unique_amino_acids), len(amino_acid_df)
