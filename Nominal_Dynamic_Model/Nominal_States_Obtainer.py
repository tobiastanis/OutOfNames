import numpy as np

from Initials import Simulation_Time_Setup
from Satellites_list.EML2O import EML2O
from Satellites_list.ELO import ELO
from Nominal_Dynamic_Model.Integrator_output_states import integrator

name = Simulation_Time_Setup.NAME

t0 = Simulation_Time_Setup.simulation_start_epoch
dt = Simulation_Time_Setup.fixed_time_step
tend = Simulation_Time_Setup.simulation_end_epoch

# Initializing states
EML2O_initial = EML2O.initial_states; ELO_initial = ELO.initial_states

[states_eml2o_dict, states_elo_dict, output_eml2o_dict, output_elo_dict] = integrator(
    t0, dt, tend, EML2O_initial, ELO_initial, name
)

states_eml2o = np.vstack(list(states_eml2o_dict.values()))
states_elo = np.vstack(list(states_elo_dict.values()))

output_eml2o = np.vstack(list(output_eml2o_dict()))
output_elo = np.vstack(list(output_elo_dict()))

