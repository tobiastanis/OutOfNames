"""
Obtains the Nominal trajectory in a very high fidelity model
"""

#own libraries
from Initials import Simulation_Time_Setup
from Satellites_list.EML2O import EML2O
from Satellites_list.ELO import ELO
from Nominal_Dynamic_Model import NOMINAL_dynamic_model_function
#general libraries
import numpy as np
import csv
#tudatpy libraries

# Initializing states
EML2O_initial = EML2O.initial_states; ELO_initial = ELO.initial_states
initial_states = np.vstack([EML2O_initial.reshape(-1,1), ELO_initial.reshape(-1,1)])

[states, output] = NOMINAL_dynamic_model_function.NOMINAL_dynamic_model(
    t0=Simulation_Time_Setup.simulation_start_epoch,
    dt=Simulation_Time_Setup.fixed_time_step,
    tend=Simulation_Time_Setup.simulation_end_epoch,
    X=initial_states
)

#print(states)
#print(output)
