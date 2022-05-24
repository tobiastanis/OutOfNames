"""
Functions using the Milano data to obtain the initial states. Initial states of ELO are provided Earth centered using
the position of the Moon at an epoch plus the initial Moon centered
"""
#Importing
# General
import numpy as np
# Own libraries
from Milano_Data.Milano_Data_Reader import Moon_dataframe
from Milano_Data.Milano_Data_Reader import LUMIO_dataframe
#tudatpy
from tudatpy.kernel.astro import element_conversion
from tudatpy.kernel.interface import spice_interface
spice_interface.load_standard_kernels()

# ELO Moon centered
"""
The Moon-centered initial states of ELO can be adjusted to propagate different kinds of orbits, e.g., polar orbits
"""
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

#Simulation time in Ephemeris Time for real time propagation
def simulation_start_epoch(t0):
    data = np.asarray(LUMIO_dataframe.loc[(LUMIO_dataframe['MJD'] == t0)])[0]
    return data[1].item()
    #return np.asscalar(data[1])

#Initial states for the Earth-Moon L2 Orbiter
def initial_states_eml2(t0):
    data = np.asarray(LUMIO_dataframe.loc[(LUMIO_dataframe['MJD'] == t0)])[0]
    return data[2: 8]*10**3

#Initial states for the Elliptic Lunar Orbiter
def initial_states_elo(t0):
    ephemeris_start_epoch = (np.asarray(LUMIO_dataframe.loc[(LUMIO_dataframe['MJD'] == t0)])[0])[1]
    moon_initial_states = spice_interface.get_body_cartesian_state_at_epoch("Moon", "Earth", "J2000", "NONE", ephemeris_start_epoch)
    return np.add(initial_states_ELO_Moon, moon_initial_states)

"""
Some extra functions which might be handy
"""
def states_moon_data(t0, tend):
    return np.asarray(Moon_dataframe.loc[(Moon_dataframe['MJD'] >= t0) & (Moon_dataframe['MJD'] <= tend)])[:, 2: 8]*10**3

def states_eml2_data(t0,tend):
    return np.asarray(LUMIO_dataframe.loc[(LUMIO_dataframe['MJD'] >= t0) & (LUMIO_dataframe['MJD'] <= tend)])[:, 2: 8]*10**3

def moon_ephemeris(ephemeris_span):
    x_moon = []
    for i in range(len(ephemeris_span)):
        t_n = ephemeris_span[i]
        state = spice_interface.get_body_cartesian_state_at_epoch("Moon", "Earth", "J2000", "NONE", t_n)
        x_moon.append(state)
    return np.array(x_moon)
