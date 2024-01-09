import numpy as np
import pandas as pd

def frame_selection(amino_acids_dict,  total_frames, frame_start=0, frame_end=-1, skip_frames = 0):
    if frame_start==0:
        if frame_end==-1:
            if skip_frames==0:
                modified_dict = amino_acids_dict.copy()
                return modified_dict
            else:
                if skip_frames > total_frames:
                    raise IndexError("Skipping more frames than total frame is not allowed.")

                modified_dict = {}
                for key, values in amino_acids_dict.items():
                    modified_values = values[::skip_frames]
                    modified_dict[key] = modified_values
                return modified_dict
        else:
            if frame_end+1 <= 0 or frame_end > total_frames:
                raise IndexError("No of frames cannot be 0 or negative or more than total frame.")
            values_to_keep = frame_end+1
            modified_dict = {}
            for key,values in amino_acids_dict.items():
                modified_values = values[:values_to_keep]
                modified_dict[key] = modified_values
            if skip_frames==0:
                return modified_dict
            else:
                if skip_frames > values_to_keep:
                    raise IndexError("Skipping more frames than total frame is not allowed.")
                modified_dict2 = {}
                for key, values in modified_dict.items():
                    modified_values2 = values[:frame_end:skip_frames]
                    modified_dict2[key] = modified_values2
                return modified_dict2

    else:
        if frame_start > total_frames:
            raise IndexError("Less than zero frames are called")
        values_to_keep = frame_start
        modified_dict = {}
        for key, values in amino_acids_dict.items():
            modified_values = values[values_to_keep:]
            modified_dict[key] = modified_values
        if frame_end==-1:
            if skip_frames == 0:
                return modified_dict
            else:
                if skip_frames > (total_frames-frame_start+1):
                    raise IndexError("Skipping more frames than total frame is not allowed.")
                modified_dict2 = {}
                for key, values in modified_dict.items():
                    modified_values2 = values[::skip_frames]
                    modified_dict2[key] = modified_values2
                return modified_dict2
        else:
            if frame_end > (total_frames - frame_start):
                raise IndexError("Little amount of frames called.")
            values_to_keep = frame_end+1-frame_start
            modified_dict2 = {}
            for key,values in modified_dict.items():
                modified_values = values[:values_to_keep]
                modified_dict2[key] = modified_values
            if skip_frames==0:
                return modified_dict2
            else:
                if skip_frames > values_to_keep:
                    raise IndexError("Skipping more frames than total frame is not allowed.")
                modified_dict3 = {}
                for key, values in modified_dict.items():
                    modified_values2 = values[:values_to_keep:skip_frames]
                    modified_dict3[key] = modified_values2
                return modified_dict3


