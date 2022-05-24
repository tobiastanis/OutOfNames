"""
This is the Nominal Measurement Model.
"""
#general
import numpy as np
#own
from Initials import Simulation_Time_Setup
from Saved_Data import Data_Loader

#Loading Nominal Trajectory
nominal_states = Data_Loader.json_states_reader("EML2_ELO_60390_10days")

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




