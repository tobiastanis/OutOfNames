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
file_name_measurement_array = "nominal_states_dt_5min.json"

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

def json_2states_reader(dirname):
    dirname = dirname
    working_dir = Path.joinpath(parent_dir, dirname)
    file_path1 = Path.joinpath(working_dir, "states_eml2o.json")
    file_path2 = Path.joinpath(working_dir, "states_elo.json")
    with open(file_path1) as json_file:
        states_eml2o_dict = json.load(json_file)
    with open(file_path2) as json_file:
        states_elo_dict = json.load(json_file)
    states_eml2o = np.vstack(list(states_eml2o_dict.values()))
    states_elo = np.vstack(list(states_elo_dict.values()))
    states = np.concatenate((states_eml2o, states_elo), axis=1)
    return states

def json_output_reader(dirname):
    dir_name = dirname
    working_dir = Path.joinpath(parent_dir, dir_name)
    file_path1 = Path.joinpath(working_dir, "output_eml2o.json")
    file_path2 = Path.joinpath(working_dir, "output_elo.json")
    with open(file_path1) as json_file:
        output_eml2o_dict = json.load(json_file)
    with open(file_path2) as json_file:
        output_elo_dict = json.load(json_file)
    output_eml2o = np.vstack(list(output_eml2o_dict.values()))
    output_elo = np.vstack(list(output_elo_dict.values()))
    output = np.concatenate((output_eml2o, output_elo), axis=1)
    return output

def json_eml2o_output_reader(dirname):
    dir_name = dirname
    working_dir = Path.joinpath(parent_dir, dir_name)
    file_path = Path.joinpath(working_dir, "output_eml2o.json")
    with open(file_path) as json_file:
        output_eml2o_dict = json.load(json_file)
    output_eml2o = np.vstack(list(output_eml2o_dict.values()))
    return output_eml2o
def json_elo_output_reader(dirname):
    dir_name = dirname
    working_dir = Path.joinpath(parent_dir, dir_name)
    file_path = Path.joinpath(working_dir, "output_elo.json")
    with open(file_path) as json_file:
        output_elo_dict = json.load(json_file)
    output_eml2o = np.vstack(list(output_elo_dict.values()))
    return output_eml2o

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


def json_estimation_data_reader(dirname, name):
    dirname = dirname
    working_dir = Path.joinpath(parent_dir, dirname)
    file_path = Path.joinpath(working_dir, name)
    with open(file_path) as json_file:
        estimation_data_dict = json.load(json_file)
    a = list(list(estimation_data_dict.items())[0])[1]
    estimation_data = np.array(a)
    return estimation_data


