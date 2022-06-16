"""
Integrator class
"""
#general
import numpy as np

#tudatpy
from tudatpy.kernel.interface import spice
from tudatpy.kernel.numerical_simulation import environment, environment_setup
from tudatpy.kernel.numerical_simulation import propagation, propagation_setup


class three_body_system_pm_no_srp:
    def __init__(self, name, mass, t0, tend, dt):
        self.name = name
        self.mass = mass
        self.body_to_propagate = [self.name]
        self.t0 = t0
        self.tend = tend
        self.dt = dt
        self.bodies = None
        self.acceleration_models = None
        self.central_bodies = None

        spice.load_standard_kernels()

    def create_variables(self):
        bodies_to_create = ["Earth", "Moon", "Sun"]
        global_frame_origin = "Earth"
        global_frame_orientation = "J2000"
        body_settings = environment_setup.get_default_body_settings(
            bodies_to_create, global_frame_origin, global_frame_orientation)

        self.bodies = environment_setup.create_system_of_bodies(body_settings)
        self.central_bodies = ["Earth"]

        self.bodies.create_empty_body(self.name)
        self.bodies.get(self.name).mass = self.mass

        accelerations = dict(
            Earth=[propagation_setup.acceleration.point_mass_gravity()],
            Moon=[propagation_setup.acceleration.point_mass_gravity()],
            Sun=[propagation_setup.acceleration.point_mass_gravity()]
        )

        acceleration_settings = {
            self.name: accelerations
        }

        self.acceleration_models = propagation_setup.create_acceleration_models(
            self.bodies, acceleration_settings, self.body_to_propagate, self.central_bodies)