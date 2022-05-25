"""
This file provides the Nominal observations using the measurement array and the range and range rate functions
"""
#General
import numpy as np

#Own
from Initials import Simulation_Time_Setup
from Measurement_Model import measurement_functions
from Saved_Data import Data_Loader

states = Data_Loader.json_measurementarray_reader(Simulation_Time_Setup.DIRECTORY_NAME)
print(len(states))
bias = Simulation_Time_Setup.bias
sigma_noise = Simulation_Time_Setup.sigma_noise
bias_dot = Simulation_Time_Setup.bias_dot
noise_dot = Simulation_Time_Setup.noise_dot

range_observations = measurement_functions.range_observations(states, bias, sigma_noise)
rangerate_observations = measurement_functions.rangerate_observations(states, bias_dot, noise_dot)
