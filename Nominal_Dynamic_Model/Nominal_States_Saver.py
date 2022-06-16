"""
This file makes is able to save the output and states of the nominal simulator. This can later be used for
measurement model and estimation model.
"""
#General
import os
from pathlib import Path
import json
#Own
from Nominal_Dynamic_Model.Nominal_States_Obtainer import states_eml2o_dict
from Nominal_Dynamic_Model.Nominal_States_Obtainer import states_elo_dict
from Initials.Simulation_Time_Setup import DIRECTORY_NAME
from Initials.Simulation_Time_Setup import OVERWRITE
print("start json writing")
#nparray items to list item

states_eml2o = {key: value.tolist() for key,value in states_eml2o_dict.items()}
states_elo = {key: value.tolist() for key,value in states_elo_dict.items()}

#########################Check the last directory everytime to prevent unwanted overwriting#############################
dir_name = DIRECTORY_NAME # In Initials in Simulation_Time_Setup
########################################################################################################################
file_name1 = "states_eml2o.json"
file_name2 = "states_elo.json"

this_path = Path(__file__)
parent_dir = this_path.parent.parent

working_dir = Path.joinpath(parent_dir, dir_name)
overwrite_path = 0
if os.path.exists(working_dir) and overwrite_path == OVERWRITE:
    quit("Path already exists and overwrite is not allowed (turn overwrite_path=1 to overwrite data)")
if not os.path.exists(working_dir):
    os.makedirs(working_dir)

file_path_states = Path.joinpath(working_dir, file_name1)
file_path_output = Path.joinpath(working_dir, file_name2)

def write_json(dictionary, file_path):
    with open(file_path, 'w') as json_file:
        dump = json.dump(dictionary, json_file)

write_json(states_eml2o, file_path_states)
write_json(states_elo, file_path_output)

print("Files written")

