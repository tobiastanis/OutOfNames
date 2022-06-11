"""
This script contains the initialinzing of the full model. Thi sis based on MJD time which is conferted for
"""
#Own libraries
from Initials import initial_states_obtainer
#General libraries
import numpy as np
import math
#tudatpy libraries
from tudatpy.kernel import constants

# Simulation Settings
#########################################ADJUSTABLES####################################################################
t0_mjd = 60390.00                                           #Modified Julian Date
simulation_duration = 10                                    #Days
fixed_time_step = 1                                         #Fixed Time Step [s]

DIRECTORY_NAME = "Saved_Data\\EML2_ELO_60390_10days"
OVERWRITE = 0 # OFF = 0, ON = 1
########################################################################################################################
"""
Simulation start and end epoch in ephemeris time. Also simulation spans from 0 and from ephemeris time are provided
"""
"""
These values are used for the Nominal Trajectory Obtainer, which provides the trajectory of both satellites in 
"""
simulation_start_epoch = initial_states_obtainer.simulation_start_epoch(t0_mjd)
simulation_end_epoch = simulation_start_epoch + simulation_duration*constants.JULIAN_DAY
n_steps_nomdym = math.floor((simulation_end_epoch-simulation_start_epoch)/fixed_time_step)+1
simulation_span = np.linspace(0, simulation_duration, n_steps_nomdym)
simulation_span_ephemeris = np.linspace(simulation_start_epoch, simulation_end_epoch, n_steps_nomdym)

"""
The following values are used for the measurements. Measurements cannot take place every 1 second, so another 
measurement interval is used, e.g., 5 min or more. Measurement interval will be provided in whole seconds.
"""
measurement_interval = 60
measurement_time_step = measurement_interval*fixed_time_step
measurement_start_epoch = simulation_start_epoch
measurement_end_epoch = simulation_end_epoch
n_steps_measure = math.floor((measurement_end_epoch-measurement_start_epoch)/measurement_time_step)+1
measurement_span_ephemeris = np.linspace(measurement_start_epoch, measurement_end_epoch, n_steps_measure)
measurement_span_t = np.linspace(0, simulation_duration, n_steps_measure)

sigma_noise = 50
bias = 0
noise_dot = 0
bias_dot = 0

"""
Estimation Model Setup
"""

estimated_initial_error = np.array([500, 500, 500, 1e-3, 1e-3, 1e-3, 500, 500, 500, 1e-3, 1e-3, 1e-3])
#estimated_initial_error = np.array([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
#Initial Covariance Matrix
P0 = 10*np.diag((estimated_initial_error))
#State Compensation matrix Qc (tunable)
#Qc = np.eye(6)*[0.033, 0.033, 0.033, 6.5, 6.5, 6.5]*5e-12                   # This one is bes6 until now
Qc = np.eye(6)*[0.033, 0.035, 0.033, 4, 2, 3]*5e-12

CONFIGURATION = 1
if CONFIGURATION == 0:
    filename = "estimation_data_CONF_0.json"
if CONFIGURATION == 1:
    filename = "estimation_data_CONF_1.json"
if CONFIGURATION == 2:
    filename = "estimation_data_CONF_2.json"
if CONFIGURATION == 3:
    filename = "estimation_data_CONF_3.json"
if CONFIGURATION == 4:
    filename = "estimation_data_CONF_4.json"

