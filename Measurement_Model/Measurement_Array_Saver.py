"""
This is the Nominal Measurement Model.
"""
#general
import numpy as np
import json
from pathlib import Path
import os
#own
from Initials import Simulation_Time_Setup
from Saved_Data import Data_Loader
from Measurement_Model import measurement_functions


#Loading Nominal Trajectory
nominal_states = Data_Loader.json_states_reader("EML2_ELO_60390_10days")
#Obtaining the measurement array
measurement_array = measurement_functions.measurement_array(nominal_states, Simulation_Time_Setup.measurement_interval)

measurement_dict = {"dict": measurement_array}
measurement_dict = {key: value.tolist() for key,value in measurement_dict.items()}
############################################CHECK DIRECTORY NAME WITH Nominal_Trajectory_Saver##########################
dir_name = Simulation_Time_Setup.DIRECTORY_NAME
file_name = "nominal_measurement_array.json"

this_path = Path(__file__)
parent_dir = this_path.parent.parent

working_dir = Path.joinpath(parent_dir, dir_name)
file_path = Path.joinpath(working_dir, file_name)

def write_json(dictionary, file_path):
    with open(file_path, 'w') as json_file:
        dump = json.dump(dictionary, json_file)

write_json(measurement_dict, file_path)
quit()







"""
bias = Simulation_Time_Setup.bias
sigma_noise = Simulation_Time_Setup.sigma_noise
bias_dot = Simulation_Time_Setup.bias_dot
noise_dot = Simulation_Time_Setup.noise_dot

range_observations = measurement_functions.range_observations(measurement_array, bias, sigma_noise)
rangerate_observations = measurement_functions.rangerate_observations(measurement_array, bias_dot, noise_dot)
"""