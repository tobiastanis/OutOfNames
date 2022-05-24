"""
Function file, which reads the required json file. Opens, reads and returns the nominal states in the right format.
dirname must be given in the from of the directory name of the save nominal trajectory, e.g., "EML2_ELO_60390_10days"
"""
import json
import numpy as np
from pathlib import Path

def json_reader(dirname):
    dir_name = dirname
    file_name = "states.json"
    nom_trajectory_data = "Saved_Data\\Nominal_Trajectory_Data"

    this_path = Path(__file__)
    parent_dir = this_path.parent.parent

    nom_trajectory_dir = Path.joinpath(parent_dir, nom_trajectory_data)
    working_dir = Path.joinpath(nom_trajectory_dir, dir_name)

    file_path = Path.joinpath(working_dir, file_name)


