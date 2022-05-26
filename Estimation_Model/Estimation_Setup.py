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
print("Preparing Estimation Setup")
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
nominal_range_array = Nominal_Observations_Cooker.range_observations
nominal_rangerate_array = Nominal_Observations_Cooker.rangerate_observations
print(nominal_range_array[1])
print(nominal_rangerate_array[1])
Y_nominal = estimator_functions.observations(nominal_range_array, nominal_rangerate_array, switch)

#Initial Covariance Matrix
P0 = Simulation_Time_Setup.P0

#Gamma [RR]
RR1 = np.concatenate((dt**2/2*np.eye(3), np.zeros((3,3))), axis=1)
RR2 = np.concatenate((dt*np.eye(3), np.zeros((3,3))), axis=1)
RR3 = np.concatenate((np.zeros((3,3)), dt**2/2*np.eye(3)), axis=1)
RR4 = np.concatenate((np.zeros((3,3)), dt*np.eye(3)), axis=1)
RR = np.concatenate((np.concatenate((np.concatenate((RR1, RR2), axis=0), RR3), axis=0), RR4), axis=0)
Qc = Simulation_Time_Setup.Qc

Qdt = np.matmul(np.matmul(RR,Qc), np.transpose(RR))

#R
R_element = Simulation_Time_Setup.sigma_noise**2
R = estimator_functions.R_function(R_element, switch)

print("Estimation Setup ready for use")

# Initializing
Pk = P0
Xhat_k = X0
std_Pk = np.sqrt(np.diag(Pk))
