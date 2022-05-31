"""
Integrator class
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
from Satellites_list.ELO import ELO
from Satellites_list.EML2O import EML2O

class EstimationClass:
    def __init__(self, name, mass, Aref, Cr, occulting_bodies):
        self.name = name
        self.mass = mass
        self.Aref = Aref
        self.Cr = Cr
        self.occulting_bodies = occulting_bodies
        spice.load_standard_kernels()

    def create_bodies(self, SRP_settings):
        bodies_to_create = ["Earth", "Moon", "Sun", "Jupiter"]
        body_settings = environment_setup.get_default_body_settings(bodies_to_create, "Earth", "J2000")
        bodies = environment_setup.create_system_of_bodies(body_settings)
        central_bodies = ["Earth"]
        body_to_propagate = name

        bodies.create_empty_body(name)
        bodies.get(name).mass = mass

