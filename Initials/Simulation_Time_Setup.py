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
simulation_duration = 14                                    #Days
fixed_time_step = 10                                        #Fixed Time Step [s]

"For NAME, choose from Three_Body_System_PM(_NO_SRP), Solar_System(_200_200)"
NAME = "Solar_System_200_200"
DIRECTORY_NAME = "Saved_Data\\Solar_System_200_200"

OVERWRITE = 1 # OFF = 0, ON = 1
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
measurement_interval = 6
measurement_time_step = measurement_interval*fixed_time_step
measurement_start_epoch = simulation_start_epoch
measurement_end_epoch = simulation_end_epoch
n_steps_measure = math.floor((measurement_end_epoch-measurement_start_epoch)/measurement_time_step)+1
measurement_span_ephemeris = np.linspace(measurement_start_epoch, measurement_end_epoch, n_steps_measure)
measurement_span_t = np.linspace(0, simulation_duration, n_steps_measure)

sigma_noise = 10
bias = 0
noise_dot = 5e-4   #1e-3, 1e-4, 5e-4
bias_dot = 0

"""
Estimation Model Setup
"""

estimated_initial_error = np.array([500, 500, 500, 1e-3, 1e-3, 1e-3, 500, 500, 500, 1e-3, 1e-3, 1e-3])
#estimated_initial_error = np.array([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
#Initial Covariance Matrix
#P0 = np.diag((estimated_initial_error))
P0 = np.diag([25e4, 25e4, 25e4, 1e-2, 1e-2, 1e-2, 25e4, 25e4, 25e4, 1e-2, 1e-2, 1e-2])
#P0 = np.diag(np.square(estimated_initial_error))
#P0 = np.diag([15e4, 15e4, 15e4, 1e-2, 1e-2, 1e-2, 15e4, 15e4, 15e4, 1e-2, 1e-2, 1e-2])
#State Compensation matrix Qc
Qc = np.eye(6)*[1, 1, 1, 0.1, 0.1, 0.1]*5e-10

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

