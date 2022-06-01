"""
This function file describes the simulation of both satellites over the defined simulation time. The output of this
model is the reference trajectory used for the estimation.
"""

#general
import numpy as np
#own
from Satellites_list.EML2O import EML2O
from Satellites_list.ELO import ELO
#tudatpy
from tudatpy.kernel import numerical_simulation
from tudatpy.kernel.interface import spice_interface
from tudatpy.kernel.numerical_simulation import environment_setup
from tudatpy.kernel.numerical_simulation import propagation_setup

## Loading SPICE kernels
spice_interface.load_standard_kernels()

def NOMINAL_dynamic_model(t0, dt, tend, X):
    simulation_start_epoch = t0
    simulation_end_epoch = tend
    fixed_time_step = dt

    initial_states = X

    ### Environment Setup ###
    # The creation of bodies
    bodies_to_create = [
        "Earth", "Moon", "Sun", "Mercury", "Venus", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"
    ]
    global_frame_origin = "Earth"
    global_frame_orientation = "J2000"
    initial_time = simulation_start_epoch
    final_time = simulation_end_epoch
    body_settings = environment_setup.get_default_body_settings(
        bodies_to_create, global_frame_origin, global_frame_orientation)

    body_system = environment_setup.create_system_of_bodies(body_settings)

    # Adding satellites in the environment
    # Earth-Moon L2 Orbiter
    body_system.create_empty_body("EML2O")
    body_system.get("EML2O").mass = EML2O.mass
    # Elliptic Lunar Orbiter
    body_system.create_empty_body("ELO")
    body_system.get("ELO").mass = EML2O.mass

    bodies_to_propagate = ["EML2O", "ELO"]
    central_bodies = ["Earth", "Earth"]

    ### Acceleration Setup ###
    # SRP
    reference_area_radiation_eml2o = EML2O.reference_area
    radiation_pressure_coefficient_eml2o = EML2O.radiation_pressure_coefficient
    occulting_bodies_eml2o = EML2O.occulting_bodies
    radiation_pressure_settings_eml2o = environment_setup.radiation_pressure.cannonball(
        "Sun", reference_area_radiation_eml2o, radiation_pressure_coefficient_eml2o, occulting_bodies_eml2o
    )
    reference_area_radiation_elo = ELO.reference_area
    radiation_pressure_coefficient_elo = ELO.radiation_pressure_coefficient
    occulting_bodies_elo = ELO.occulting_bodies
    radiation_pressure_settings_elo = environment_setup.radiation_pressure.cannonball(
        "Sun", reference_area_radiation_elo, radiation_pressure_coefficient_elo, occulting_bodies_elo
    )

    environment_setup.add_radiation_pressure_interface(body_system, "EML2O", radiation_pressure_settings_eml2o)
    environment_setup.add_radiation_pressure_interface(body_system, "ELO", radiation_pressure_settings_elo)

    acceleration_settings_eml2o = dict(
        Earth=[propagation_setup.acceleration.spherical_harmonic_gravity(200, 200)],
        Moon=[propagation_setup.acceleration.spherical_harmonic_gravity(200, 200)],
        Sun=[propagation_setup.acceleration.point_mass_gravity(),
             propagation_setup.acceleration.cannonball_radiation_pressure()],
        Mercury=[propagation_setup.acceleration.point_mass_gravity()],
        Venus=[propagation_setup.acceleration.point_mass_gravity()],
        Mars=[propagation_setup.acceleration.point_mass_gravity()],
        Jupiter=[propagation_setup.acceleration.point_mass_gravity()],
        Saturn=[propagation_setup.acceleration.point_mass_gravity()],
        Uranus=[propagation_setup.acceleration.point_mass_gravity()],
        Neptune=[propagation_setup.acceleration.point_mass_gravity()]
    )

    acceleration_settings_elo = dict(
        Earth=[propagation_setup.acceleration.spherical_harmonic_gravity(200, 200)],
        Moon=[propagation_setup.acceleration.spherical_harmonic_gravity(200, 200)],
        Sun=[propagation_setup.acceleration.point_mass_gravity(),
             propagation_setup.acceleration.cannonball_radiation_pressure()],
        Mercury=[propagation_setup.acceleration.point_mass_gravity()],
        Venus=[propagation_setup.acceleration.point_mass_gravity()],
        Mars=[propagation_setup.acceleration.point_mass_gravity()],
        Jupiter=[propagation_setup.acceleration.point_mass_gravity()],
        Saturn=[propagation_setup.acceleration.point_mass_gravity()],
        Uranus=[propagation_setup.acceleration.point_mass_gravity()],
        Neptune=[propagation_setup.acceleration.point_mass_gravity()]
    )

    acceleration_settings = {
        "EML2O": acceleration_settings_eml2o,
        "ELO": acceleration_settings_elo
    }

    acceleration_models = propagation_setup.create_acceleration_models(
        body_system, acceleration_settings, bodies_to_propagate, central_bodies)

    ### Savings ###
    # Is adjustable
    dependent_variables_to_save = [
        propagation_setup.dependent_variable.total_acceleration("EML2O"),
        propagation_setup.dependent_variable.single_acceleration_norm(
            propagation_setup.acceleration.cannonball_radiation_pressure_type, "EML2O", "Sun"
        ),
        propagation_setup.dependent_variable.single_acceleration_norm(
            propagation_setup.acceleration.spherical_harmonic_gravity_type, "EML2O", "Earth"
        ),
        propagation_setup.dependent_variable.single_acceleration_norm(
            propagation_setup.acceleration.spherical_harmonic_gravity_type, "EML2O", "Moon"
        ),
        propagation_setup.dependent_variable.single_acceleration_norm(
            propagation_setup.acceleration.point_mass_gravity_type, "EML2O", "Sun"
        ),
        propagation_setup.dependent_variable.single_acceleration_norm(
            propagation_setup.acceleration.point_mass_gravity_type, "EML2O", "Mercury"
        ),
        propagation_setup.dependent_variable.single_acceleration_norm(
            propagation_setup.acceleration.point_mass_gravity_type, "EML2O", "Venus"
        ),
        propagation_setup.dependent_variable.single_acceleration_norm(
            propagation_setup.acceleration.point_mass_gravity_type, "EML2O", "Mars"
        ),
        propagation_setup.dependent_variable.single_acceleration_norm(
            propagation_setup.acceleration.point_mass_gravity_type, "EML2O", "Jupiter"
        ),
        propagation_setup.dependent_variable.single_acceleration_norm(
            propagation_setup.acceleration.point_mass_gravity_type, "EML2O", "Saturn"
        ),
        propagation_setup.dependent_variable.single_acceleration_norm(
            propagation_setup.acceleration.point_mass_gravity_type, "EML2O", "Uranus"
        ),
        propagation_setup.dependent_variable.single_acceleration_norm(
            propagation_setup.acceleration.point_mass_gravity_type, "EML2O", "Neptune"
        ),
        propagation_setup.dependent_variable.total_acceleration("ELO"),
        propagation_setup.dependent_variable.single_acceleration_norm(
            propagation_setup.acceleration.cannonball_radiation_pressure_type, "ELO", "Sun"
        ),
        propagation_setup.dependent_variable.single_acceleration_norm(
            propagation_setup.acceleration.spherical_harmonic_gravity_type, "ELO", "Earth"
        ),
        propagation_setup.dependent_variable.single_acceleration_norm(
            propagation_setup.acceleration.spherical_harmonic_gravity_type, "ELO", "Moon"
        ),
        propagation_setup.dependent_variable.single_acceleration_norm(
            propagation_setup.acceleration.point_mass_gravity_type, "ELO", "Sun"
        ),
        propagation_setup.dependent_variable.single_acceleration_norm(
            propagation_setup.acceleration.point_mass_gravity_type, "ELO", "Mercury"
        ),
        propagation_setup.dependent_variable.single_acceleration_norm(
            propagation_setup.acceleration.point_mass_gravity_type, "ELO", "Venus"
        ),
        propagation_setup.dependent_variable.single_acceleration_norm(
            propagation_setup.acceleration.point_mass_gravity_type, "ELO", "Mars"
        ),
        propagation_setup.dependent_variable.single_acceleration_norm(
            propagation_setup.acceleration.point_mass_gravity_type, "ELO", "Jupiter"
        ),
        propagation_setup.dependent_variable.single_acceleration_norm(
            propagation_setup.acceleration.point_mass_gravity_type, "ELO", "Saturn"
        ),
        propagation_setup.dependent_variable.single_acceleration_norm(
            propagation_setup.acceleration.point_mass_gravity_type, "ELO", "Uranus"
        ),
        propagation_setup.dependent_variable.single_acceleration_norm(
            propagation_setup.acceleration.point_mass_gravity_type, "ELO", "Neptune"
        ),
        propagation_setup.dependent_variable.central_body_fixed_cartesian_position("EML2O", "Moon"),
        propagation_setup.dependent_variable.central_body_fixed_cartesian_position("ELO", "Moon"),
        propagation_setup.dependent_variable.relative_velocity("EML2O", "ELO"),
        propagation_setup.dependent_variable.relative_position("EML2O", "ELO"),
    ]

    termination_condition = propagation_setup.propagator.time_termination(simulation_end_epoch)
    propagation_settings = propagation_setup.propagator.translational(
        central_bodies,
        acceleration_models,
        bodies_to_propagate,
        initial_states,
        termination_condition,
        output_variables=dependent_variables_to_save
    )

    ### Integrating ###
    integrator_settings = numerical_simulation.propagation_setup.integrator.runge_kutta_4(
        simulation_start_epoch, fixed_time_step
    )

    ### Dynamic Simulator ###
    dynamic_simulator = numerical_simulation.SingleArcSimulator(
        body_system, integrator_settings, propagation_settings
    )

    states_dict = dynamic_simulator.state_history
    output_dict = dynamic_simulator.dependent_variable_history

    return [states_dict, output_dict]


