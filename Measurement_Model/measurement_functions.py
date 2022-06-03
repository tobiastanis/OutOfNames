"""
function file for ranging and range rate functions
"""
import numpy as np

def h(states, x_moon):
    a = np.subtract(states[0:3], x_moon[0:3])
    b = np.subtract(states[0:3], states[6:9])
    a_abs = np.linalg.norm(a)
    b_abs = np.linalg.norm(b)
    theta = np.arccos(np.dot(a,b)/(a_abs*b_abs))
    h = a_abs*np.sin(theta)
    return h


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

def intersatellite_distances(X):
    array_to_fill = []
    for i in range(len(X)):
        row = intersatellite_distance(X[i, :])
        array_to_fill.append(row)
    return np.array(array_to_fill)

def range_observation_row(X, bias, sigma_noise):
    x1 = X[0]; y1 = X[1]; z1 = X[2]; x2 = X[6]; y2 = X[7]; z2 = X[8]
    R = ((x1 - x2) ** 2 + (y1 - y2) ** 2 + (z1 - z2) ** 2) ** 0.5
    noise = np.random.normal(0, sigma_noise)
    return R + bias + noise

def nominal_range_observation(X, X_moon, bias, sigma_noise):
    array_to_fill = []
    for i in range(len(X)):
        states = X[i, :]
        x_moon = X_moon[i, :]
        a = np.subtract(states[0:3], x_moon[0:3])
        b = np.subtract(states[0:3], states[6:9])
        a_abs = np.linalg.norm(a)
        b_abs = np.linalg.norm(b)
        theta = np.arccos(np.dot(a, b) / (a_abs * b_abs))
        h = a_abs * np.sin(theta)
        if h <= 1800e3:
            array_to_fill.append(0)
        else:
            row = range_observation_row(states, bias, sigma_noise)
            array_to_fill.append(row)
    return np.array(array_to_fill)

def nominal_rangerate_observations(X, X_moon, bias_dot, noise_dot):
    array_to_fill = []
    for i in range(len(X)):
        states = X[i, :]
        x_moon = X_moon[i, :]
        a = np.subtract(states[0:3], x_moon[0:3])
        b = np.subtract(states[0:3], states[6:9])
        a_abs = np.linalg.norm(a)
        b_abs = np.linalg.norm(b)
        theta = np.arccos(np.dot(a, b) / (a_abs * b_abs))
        h = a_abs * np.sin(theta)
        if h <= 1800e3:
            array_to_fill.append(0)
        else:
            row = rangerate_observation_row(states, bias_dot, noise_dot)
            array_to_fill.append(row)
    return np.array(array_to_fill)


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


