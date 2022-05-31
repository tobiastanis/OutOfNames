"""
Defined class satellite
"""
#general
import numpy as np
#tudatpy
from tudatpy.kernel import numerical_simulation
from tudatpy.kernel.astro import element_conversion
from tudatpy.kernel.interface import spice
from tudatpy.kernel.numerical_simulation import environment, environment_setup
from tudatpy.kernel.numerical_simulation import propagation, propagation_setup
#own

class satellite:
    def __init__(self, name, mass, reference_area, radiation_pressure_coefficient, occulting_bodies, initial_states):
        self.name = name
        self.mass = mass
        self.reference_area = reference_area
        self.radiation_pressure_coefficient = radiation_pressure_coefficient
        self.occulting_bodies = occulting_bodies
        self.initial_states = initial_states
