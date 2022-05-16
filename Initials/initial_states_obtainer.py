"""
Functions using the Milano data to obtain the initial states. Initial states of ELO are provided Earth centered using
the position of the Moon at an epoch plus the initial Moon centered
"""
#Importing
# General
import numpy as np
#tudatpy
from tudatpy.kernel.astro import element_conversion
from tudatpy.kernel.interface import spice_interface
spice_interface.load_standard_kernels()
# ELO Moon centered
# ESA's pathfinder like
initial_states_ELO_Moon = element_conversion.keplerian_to_cartesian_elementwise(
    gravitational_parameter=spice_interface.get_body_gravitational_parameter("Moon"),
    semi_major_axis=5737.4E3,
    eccentricity=0.61,
    inclination=np.deg2rad(57.82),
    argument_of_periapsis=np.deg2rad(90),
    longitude_of_ascending_node=np.rad2deg(61.552),
    true_anomaly=np.deg2rad(0)
)