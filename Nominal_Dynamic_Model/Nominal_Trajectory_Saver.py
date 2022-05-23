"""
This file makes is able to save the output and states of the nominal simulator. This can later be used for
measurement model and estimation model.
"""
#General
import os
import csv
from pathlib import Path
import json
import pandas as pd
#Own
from Nominal_Dynamic_Model.Nominal_Trajectory_Obtainer import states_dict
from Nominal_Dynamic_Model.Nominal_Trajectory_Obtainer import output_dict
print("start json writing")
#nparray items to list item
states_dict = {key: value.tolist() for key,value in states_dict.items()}
output_dict = {key: value.tolist() for key,value in output_dict.items()}

#####################################Change the last directory everytime ###############################################
dir_name = "Saved_Data\\Nominal_Trajectory_Data\\EML2_ELO_60390_10days"
########################################################################################################################
file_name1 = "states.json"
file_name2 = "output.json"

this_path = Path(__file__)
parent_dir = this_path.parent.parent

working_dir = Path.joinpath(parent_dir, dir_name)
if not os.path.exists(working_dir):
    os.makedirs(working_dir)

overwrite_path = 1
if os.path.exists(working_dir) and overwrite_path == 0:
    quit("Path already exists and overwrite is not allowed (turn overwrite_path=1 to overwrite data)")

file_path_states = Path.joinpath(working_dir, file_name1)
file_path_output = Path.joinpath(working_dir, file_name2)

def write_json(dictionary, file_path):
    with open(file_path, 'w') as json_file:
        dump = json.dump(dictionary, json_file)

write_json(states_dict, file_path_states)
write_json(output_dict, file_path_output)

print("Files written")

