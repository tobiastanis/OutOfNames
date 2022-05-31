"""
Characteristics of the Elliptic Lunar Orbiter
"""
from Initials import Simulation_Time_Setup
from Initials.initial_states_obtainer import initial_states_elo
from Satellites_list.satellite import satellite

initial_states = initial_states_elo(Simulation_Time_Setup.t0_mjd)

ELO = satellite(name="ELO",
                mass=280,
                reference_area=3.0,
                radiation_pressure_coefficient=1.8,
                occulting_bodies=["Moon", "Earth"],
                initial_states=initial_states)

