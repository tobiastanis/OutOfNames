"""
Function file for estimation functions
"""
import numpy as np

def observations(range, rangerate, switch):
    if switch == 0:
        observation_array = range
    if switch == 1:
        observation_array = np.concatenate((range, rangerate), axis=1)
    if switch == 2:
        observation_array = rangerate
    return observation_array

def R_function(R_element, switch):
    if switch == 1:
        output = np.eye(2)*R_element
    else:
        output = R_element
    return output