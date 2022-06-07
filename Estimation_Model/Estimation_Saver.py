#General
import os
from pathlib import Path
import json
import numpy as np
#Own
from Initials.Simulation_Time_Setup import measurement_span_ephemeris
from Initials.Simulation_Time_Setup import DIRECTORY_NAME
from Initials.Simulation_Time_Setup import OVERWRITE
from Initials.Simulation_Time_Setup import filename
from Estimation_Model.Executor import stdP
from Estimation_Model.Executor import x_error
from Estimation_Model.Executor import visibility

t_et = np.transpose([measurement_span_ephemeris])
visibility = np.transpose([visibility])

first = np.concatenate((t_et, x_error), axis=1)
second = np.concatenate((first, stdP), axis=1)
data_array = np.concatenate((second, visibility), axis=1)

estimation_dict = {"dict": data_array}
estimation_dict = {key: value.tolist() for key,value in estimation_dict.items()}

this_path = Path(__file__)
parent_dir = this_path.parent.parent

dir_name = DIRECTORY_NAME
working_dir = Path.joinpath(parent_dir, dir_name)

file_path = Path.joinpath(working_dir, filename)

overwrite_path = 0
if os.path.exists(file_path) and overwrite_path == OVERWRITE:
    quit("Path already exists and overwrite is not allowed (turn overwrite_path=1 to overwrite data)")

def write_json(dictionary, file_path):
    with open(file_path, 'w') as json_file:
        dump = json.dump(dictionary, json_file)

write_json(estimation_dict, file_path)
