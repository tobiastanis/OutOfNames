"""
This file provides the Nominal observations using the measurement array and the range and range rate functions
"""
#General
import numpy as np

#Own
from Initials import Simulation_Time_Setup
from Initials.initial_states_obtainer import moon_ephemeris
from Measurement_Model import measurement_functions
from Saved_Data import Data_Loader

x_moon = moon_ephemeris(Simulation_Time_Setup.measurement_span_ephemeris)

# States per measurement interval
states = Data_Loader.json_measurementarray_reader(Simulation_Time_Setup.DIRECTORY_NAME)

bias = Simulation_Time_Setup.bias
sigma_noise = Simulation_Time_Setup.sigma_noise
bias_dot = Simulation_Time_Setup.bias_dot
noise_dot = Simulation_Time_Setup.noise_dot

range_observations = measurement_functions.range_observations(states, bias, sigma_noise)
range_observations_test = measurement_functions.range_observation_test(states, x_moon, bias, sigma_noise)

print(range_observations)
print(range_observations_test)
#rangerate_observations = measurement_functions.rangerate_observations(states, bias_dot, noise_dot)


