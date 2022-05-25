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
bias = 0
sigma_noise = 0

range_obser = measurement_functions.range_observations(measurement_array, bias, sigma_noise)
print(range_obser)

"""
############################################CHECK DIRECTORY NAME WITH Nominal_Trajectory_Saver##########################
dir_name = Simulation_Time_Setup.DIRECTORY_NAME
file_name = "nominal_measurement_array.json"

this_path = Path(__file__)
parent_dir = this_path.parent.parent

working_dir = Path.joinpath(parent_dir, dir_name)
file_path = Path.joinpath(working_dir, file_name)

def write_json(data, file_path):
    with open(file_path, 'w'):
        dump = json.dumps(data)


write_json(measurement_array, file_path)



add_noise = 1
add_bias = 0

if add_noise == 1:
    noise = 20  # This value will differ
else:
    noise = 0

if add_bias == 1:
    bias = 20 # This value will differ
else:
    bias = 0
"""



