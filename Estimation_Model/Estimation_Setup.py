"""
Setup for the estimation model
"""
#general
import numpy as np
#own
from Initials import Simulation_Time_Setup
from Measurement_Model import Nominal_Observations_Cooker
#tudatpy

#Time Setup
dt = Simulation_Time_Setup.measurement_interval
ephemeris_span = Simulation_Time_Setup.measurement_span_ephemeris

print('hoi', len(ephemeris_span))