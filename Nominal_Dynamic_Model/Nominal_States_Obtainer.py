import numpy as np

from Initials import Simulation_Time_Setup
from Satellites_list.EML2O import EML2O
from Satellites_list.ELO import ELO
from Nominal_Dynamic_Model.Integrator import integrator

name = "Three_Body_system_PM_NO_SRP"

t0 = Simulation_Time_Setup.simulation_start_epoch
dt = Simulation_Time_Setup.fixed_time_step
tend = Simulation_Time_Setup.simulation_end_epoch

# Initializing states
EML2O_initial = EML2O.initial_states; ELO_initial = ELO.initial_states

[states_eml2o_dict, states_elo_dict] = integrator(
    t0, dt, tend, EML2O_initial, ELO_initial, name
)

states_eml2o = np.vstack(list(states_eml2o_dict.values()))
states_elo = np.vstack(list(states_elo_dict.values()))

