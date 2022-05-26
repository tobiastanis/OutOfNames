"""
High fidelity simulation model
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
from tudatpy.kernel.numerical_simulation import estimation_setup
spice_interface.load_standard_kernels()

#Satellites
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



def dynamic_integrator1(t0, dt, tend, X):

    #Environment
    bodies_to_create = ["Earth", "Moon", "Sun", "Jupiter"]
    global_frame_origin = "Earth"
    global_frame_orientation = "J2000"
    body_settings = environment_setup.get_default_body_settings_time_limited(
        bodies_to_create, t0, tend, global_frame_origin, global_frame_orientation, dt
    )
    body_system = environment_setup.create_system_of_bodies(body_settings)

    X_EML20 = X[0:6]; X_ELO = X[6:12]

    def L2(X_EML2):
        # Earth-Moon L2 Orbiter
        body_system.create_empty_body("EML2O")
        body_system.get("EML2O").mass = EML2O.mass
        body_to_propagate = ["EML2O"]
        central_body = ["Earth"]

        environment_setup.add_radiation_pressure_interface(body_system, "EML2O", radiation_pressure_settings_eml2o)

        acceleration_settings_eml2o = dict(
            Earth=[propagation_setup.acceleration.point_mass_gravity()],
            Moon=[propagation_setup.acceleration.point_mass_gravity()],
            Sun=[propagation_setup.acceleration.point_mass_gravity(),
                 propagation_setup.acceleration.cannonball_radiation_pressure()],
            Jupiter=[propagation_setup.acceleration.point_mass_gravity()]
        )
        acceleration_settings = {
            "EML2O": acceleration_settings_eml2o
        }
        acceleration_models = propagation_setup.create_acceleration_models(
            body_system, acceleration_settings, body_to_propagate, central_body)

        termination_condition = propagation_setup.propagator.time_termination(tend)
        propagation_settings = propagation_setup.propagator.translational(
            central_body,
            acceleration_models,
            body_to_propagate,
            X_EML2,
            termination_condition
        )

        integrator_settings = numerical_simulation.propagation_setup.integrator.runge_kutta_4(
            t0, dt)
        parameter_settings = estimation_setup.parameter.initial_states(
            propagation_settings, body_system)

        variational_equations_solver = numerical_simulation.SingleArcVariationalSimulator(
        body_system, integrator_settings, propagation_settings,
        estimation_setup.create_parameter_set(parameter_settings, body_system), integrate_on_creation=1
        )


        states_EML2O = variational_equations_solver.state_history
        Phi_EML2O = variational_equations_solver.state_transition_matrix_history
        print(states_EML2O, '\n', Phi_EML2O)
        return [states_EML2O, Phi_EML2O]
    a = L2(X_EML20)



print(dynamic_integrator1(1, 1, 2, np.array([1, 2, 3, 4, 5, 6])))

