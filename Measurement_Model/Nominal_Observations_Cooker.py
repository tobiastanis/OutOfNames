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

range_observations = measurement_functions.nominal_range_observation(states, x_moon, bias, sigma_noise)
rangerate_observations = measurement_functions.nominal_rangerate_observations(states, x_moon, bias_dot, noise_dot)

CONFIGURATION_NAME = Simulation_Time_Setup.CONFIGURATION

if CONFIGURATION_NAME == 1:
    ID_array = np.ones((1, len(range_observations)))[0]
    measurement_array = np.concatenate(([ID_array], [range_observations]), axis=0)
if CONFIGURATION_NAME == 2:
    ID_array = np.full((1, len(rangerate_observations)), 2)[0]
    measurement_array = np.concatenate(([ID_array], [rangerate_observations]), axis=0)
if CONFIGURATION_NAME == 3:
    ID_array= []
    measurement_row = []
    for i in range(len(range_observations)):
        if (i % 2 == 0):
            ID_array.append(1)
            measurement_row.append(range_observations[i])
        else:
            ID_array.append(2)
            measurement_row.append(rangerate_observations[i])
    measurement_array = np.concatenate(([ID_array], [measurement_row]), axis=0)

if CONFIGURATION_NAME == 4:
    ID_array = []
    measurement_row = []
    for i in range(len(range_observations)):
        if i == 0:
            ID_array.append(1)
            measurement_row.append(range_observations[i])
        if (i % 3 == 0):
            ID_array.append(2)
            measurement_row.append(rangerate_observations[i])
        else:
            ID_array.append(1)
            measurement_row.append(range_observations[i])
    ID_array.pop(1)
    measurement_row.pop(1)
    measurement_array = np.concatenate(([ID_array], [measurement_row]), axis=0)

