"""
Setup for the estimation model
"""
#general
import numpy as np
#own
from Initials import Simulation_Time_Setup
from Measurement_Model import Nominal_Observations_Cooker
from Estimation_Model import estimator_functions
#tudatpy

switch = Simulation_Time_Setup.SWITCH

#Time Setup
dt = Simulation_Time_Setup.measurement_interval
ephemeris_span = Simulation_Time_Setup.measurement_span_ephemeris

#States Setup
TRUE_states = Nominal_Observations_Cooker.states
TRUE_initial_states = TRUE_states[0, :]
estimated_initial_error = Simulation_Time_Setup.estimated_initial_error
# X_k_1 = Nominal states + initial states error
X0 = np.transpose([np.add(TRUE_initial_states, estimated_initial_error)])

#Measurements Setup
nominal_range_array = np.transpose([Nominal_Observations_Cooker.range_observations])
nominal_rangerate_array = np.transpose([Nominal_Observations_Cooker.rangerate_observations])

Y_nominal = estimator_functions.observations(nominal_range_array, nominal_rangerate_array, switch)

