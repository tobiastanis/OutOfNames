"""
function file for ranging and range rate functions
"""
import numpy as np


def measurement_array(states, timestep):
    from Initials import Simulation_Time_Setup
    array_to_fill = []
    for i in range(Simulation_Time_Setup.n_steps_measure):
        row = states[i*timestep, :]
        array_to_fill.append(row)
    return np.array(array_to_fill)

def intersatellite_distance(X):
    x1 = X[0]; y1 = X[1]; z1 = X[2]; x2 = X[6]; y2 = X[7]; z2 = X[8]
    return ((x1 - x2) ** 2 + (y1 - y2) ** 2 + (z1 - z2) ** 2) ** 0.5

def range_observation_row(X, bias, sigma_noise):
    x1 = X[0]; y1 = X[1]; z1 = X[2]; x2 = X[6]; y2 = X[7]; z2 = X[8]
    R = ((x1 - x2) ** 2 + (y1 - y2) ** 2 + (z1 - z2) ** 2) ** 0.5
    noise = np.random.normal(0, sigma_noise)
    return R + bias + noise

def range_observations(X, bias, sigma_noise):
    array_to_fill = []
    for i in range(len(X)):
        Y = range_observation_row(X[i, :], bias, sigma_noise)
        array_to_fill.append(Y)
    ranging_array = np.array(array_to_fill)
    return ranging_array

def rangerate_observation_row(X, bias_dot, noise_dot):
    x1 = X[0]; y1 = X[1]; z1 = X[2]; vx1 = X[3]; vy1 = X[4]; vz1 = X[5]
    x2 = X[6]; y2 = X[7]; z2 = X[8]; vx2 = X[9]; vy2 = X[10]; vz2 = X[11]
    R_dot = ((x1-x2)*(vx1-vx2) + (y1-y2)*(vy1-vy2) + (z1-z2)*(vz1-vz2)) / np.sqrt((x1-x2)**2 + (y1-y2)**2 + (z1-z2)**2)
    return R_dot + bias_dot + noise_dot

def rangerate_observations(X, bias_dot, noise_dot):
    array_to_fill = []
    for i in range(len(X)):
        Y = rangerate_observation_row(X[i, :], bias_dot, noise_dot)
        array_to_fill.append(Y)
    rangerate_array = np.array(array_to_fill)
    return rangerate_array
