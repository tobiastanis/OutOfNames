"""
Characteristics of the Earth-Moon L2 Orbiter
"""
from Initials import Simulation_Time_Setup
from Initials.initial_states_obtainer import initial_states_eml2
from Satellites_list.satellite import satellite

initial_states = initial_states_eml2(Simulation_Time_Setup.t0_mjd)

EML2O = satellite(name="EML2O",
                  mass=22.8,
                  reference_area=0.410644,
                  radiation_pressure_coefficient=1.08,
                  occulting_bodies=["Moon", "Earth"],
                  initial_states=initial_states)