"""
Executes the Estimation process for ELO and EML2O.

"""
#general
import numpy as np
#own
from Initials import Simulation_Time_Setup
from Measurement_Model.Nominal_Observations_Cooker import states
from Estimation_Model import Estimation_Setup
from Estimation_Model.Estimator import ekf
from Estimation_Model.AEKF import aekf


[X, stdP, visibility] = aekf(Estimation_Setup.X0,
                            Estimation_Setup.P0,
                            Estimation_Setup.Y_nominal,
                            Estimation_Setup.ephemeris_span)

X = np.array(X)
stdP = np.array(stdP)

t = Simulation_Time_Setup.measurement_span_t

x_error = np.subtract(states, X)
