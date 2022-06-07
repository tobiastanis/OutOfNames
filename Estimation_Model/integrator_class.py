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

class EstimationClass_eml2o:
    def __init__(self, name, mass, Aref, Cr, t0, tend, dt):
        self.name = name
        self.mass = mass
        self.Aref = Aref
        self.Cr = Cr
        self.body_to_propagate = [self.name]
        self.t0 = t0
        self.tend = tend
        self.dt = dt
        self.bodies = None
        self.acceleration_models = None

        spice.load_standard_kernels()

    def create_variables(self):
        bodies_to_create = ["Earth", "Moon", "Sun", "Jupiter"]
        #body_settings = environment_setup.get_default_body_settings(bodies_to_create, "Earth", "J2000")
        body_settings = environment_setup.get_default_body_settings_time_limited(
            bodies_to_create, self.t0, self.tend, "Earth", "J2000", self.dt
        )
        self.bodies = environment_setup.create_system_of_bodies(body_settings)
        self.central_bodies = ["Earth"]

        self.bodies.create_empty_body(self.name)
        self.bodies.get(self.name).mass = self.mass

        radiation_pressure_settings = environment_setup.radiation_pressure.cannonball(
            "Sun", self.Aref, self.Cr
        )

        environment_setup.add_radiation_pressure_interface(self.bodies, self.name, radiation_pressure_settings)

        acceleration_settings = dict(
            Earth=[propagation_setup.acceleration.point_mass_gravity()],
            Moon=[propagation_setup.acceleration.point_mass_gravity()],
            Sun=[propagation_setup.acceleration.point_mass_gravity(),
                 propagation_setup.acceleration.cannonball_radiation_pressure()],
            Jupiter=[propagation_setup.acceleration.point_mass_gravity()],
        )

        acceleration_settings = {
            self.name: acceleration_settings
        }

        self.acceleration_models = propagation_setup.create_acceleration_models(
            self.bodies, acceleration_settings, self.body_to_propagate, self.central_bodies)

class EstimationClass_elo:
    def __init__(self, name, mass, Aref, Cr, occulting_bodies, t0, tend, dt):
        self.name = name
        self.mass = mass
        self.Aref = Aref
        self.Cr = Cr
        self.occulting_bodies = occulting_bodies
        self.body_to_propagate = [self.name]
        self.t0 = t0
        self.tend = tend
        self.dt = dt
        self.bodies = None
        self.acceleration_models = None

        spice.load_standard_kernels()

    def create_variables(self):
        bodies_to_create = ["Earth", "Moon", "Sun", "Jupiter", "Venus", "Mercury", "Saturn" , "Mars", "Uranus", "Neptune"]
        #body_settings = environment_setup.get_default_body_settings(bodies_to_create, "Earth", "J2000")
        body_settings = environment_setup.get_default_body_settings_time_limited(
            bodies_to_create, self.t0, self.tend, "Earth", "J2000", self.dt
        )
        self.bodies = environment_setup.create_system_of_bodies(body_settings)
        self.central_bodies = ["Earth"]

        self.bodies.create_empty_body(self.name)
        self.bodies.get(self.name).mass = self.mass

        radiation_pressure_settings = environment_setup.radiation_pressure.cannonball(
            "Sun", self.Aref, self.Cr, self.occulting_bodies
        )

        environment_setup.add_radiation_pressure_interface(self.bodies, self.name, radiation_pressure_settings)

        acceleration_settings = dict(
            Earth=[propagation_setup.acceleration.spherical_harmonic_gravity(5, 5)],
            Moon=[propagation_setup.acceleration.spherical_harmonic_gravity(30, 30)],
            Sun=[propagation_setup.acceleration.point_mass_gravity(),
                 propagation_setup.acceleration.cannonball_radiation_pressure()],
            Jupiter=[propagation_setup.acceleration.point_mass_gravity()],
            Venus=[propagation_setup.acceleration.point_mass_gravity()],
            Mars=[propagation_setup.acceleration.point_mass_gravity()],
            Mercury=[propagation_setup.acceleration.point_mass_gravity()],
            Saturn=[propagation_setup.acceleration.point_mass_gravity()],
            Uranus=[propagation_setup.acceleration.point_mass_gravity()],
            Neptune=[propagation_setup.acceleration.point_mass_gravity()]
        )

        acceleration_settings = {
            self.name: acceleration_settings
        }

        self.acceleration_models = propagation_setup.create_acceleration_models(
            self.bodies, acceleration_settings, self.body_to_propagate, self.central_bodies)


