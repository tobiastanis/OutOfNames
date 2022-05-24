"""
This is the Nominal Measurement Model.
"""
import numpy as np

from Initials import Simulation_Time_Setup

add_noise = 0
add_bias = 0

if add_noise == 1:
    noise = 20  # This value will differ
else:
    noise = 0

if add_bias == 1:
    bias = 20 # This value will differ
else:
    bias = 0




