"""
Function file, which reads the required json file. Opens, reads and returns the nominal states in the right format.
dirname must be given in the from of the directory name of the save nominal trajectory, e.g., "EML2_ELO_60390_10days"
"""
import json
import numpy as np
from pathlib import Path
"All file names are states of output, but the directory they are saved in differ"
file_name_states = "states.json"
file_name_output = "output.json"
file_name_measurement_array = "nominal_states_dt_60.json"

this_path = Path(__file__)
parent_dir = this_path.parent.parent

def json_states_reader(dirname):
    dir_name = dirname
    working_dir = Path.joinpath(parent_dir, dir_name)
    file_path = Path.joinpath(working_dir, file_name_states)
    with open(file_path) as json_file:
        states_dict = json.load(json_file)
    print("nominal states loaded successfully")
    return np.vstack(list(states_dict.values()))

def json_output_reader(dirname):
    dir_name = dirname
    working_dir = Path.joinpath(parent_dir, dir_name)
    file_path = Path.joinpath(working_dir, file_name_output)
    with open(file_path) as json_file:
        output_dict = json.load(json_file)
    print("nominal output loaded successfully")
    return np.vstack(list(output_dict.values()))

def json_measurementarray_reader(dirname):
    dir_name = dirname
    working_dir = Path.joinpath(parent_dir, dir_name)
    file_path = Path.joinpath(working_dir, file_name_measurement_array)
    with open(file_path) as json_file:
        measurement_dict = json.load(json_file)
    print("nominal measurement array loaded successfully")
    a = list(list(measurement_dict.items())[0])[1]
    measurements = np.array(a)
    return measurements

