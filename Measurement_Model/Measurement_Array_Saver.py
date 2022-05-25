"""
This is the Nominal Measurement Model.
"""
#general
import json
from pathlib import Path
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
############################################ALWAYS CHECK THIS NAME######################################################
file_name = "nominal_measurements_60s.json" #60s indicates the measurement_interval

this_path = Path(__file__)
parent_dir = this_path.parent.parent

working_dir = Path.joinpath(parent_dir, dir_name)
file_path = Path.joinpath(working_dir, file_name)

def write_json(dictionary, file_path):
    with open(file_path, 'w') as json_file:
        dump = json.dump(dictionary, json_file)

write_json(measurement_dict, file_path)

