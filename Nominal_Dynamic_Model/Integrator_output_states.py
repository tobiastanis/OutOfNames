#own
from Satellites_list.EML2O import EML2O
from Satellites_list.ELO import ELO
#tudatpy
from tudatpy.kernel import numerical_simulation
from tudatpy.kernel.numerical_simulation import propagation_setup

def integrator(t0, dt, tend, X0_eml2o, X0_elo, NAME):
    if NAME != "Solar_System_200_200":
        quit("Integrator name is ill-defined, Check Initial/Simulation_Time_Setup line 18")
    if NAME == "Solar_System_200_200":
        from Nominal_Dynamic_Model.Environments.Solar_System_200_200 import int_environment

    for_eml2o = int_environment(
        name=EML2O.name,
        mass=EML2O.mass,
        Aref=EML2O.reference_area,
        Cr=EML2O.radiation_pressure_coefficient,
        occulting_bodies=EML2O.occulting_bodies,
        t0=t0,
        tend=tend,
        dt=dt
    )
    for_elo = int_environment(
        name=ELO.name,
        mass=ELO.mass,
        Aref=ELO.reference_area,
        Cr=ELO.radiation_pressure_coefficient,
        occulting_bodies=ELO.occulting_bodies,
        t0=t0,
        tend=tend,
        dt=dt
    )
    eml2o_variables = for_eml2o.create_variables()
    elo_variables = for_elo.create_variables()

    simulation_start_epoch = t0
    simulation_end_epoch = tend
    fixed_time_step = dt

    dependent_variables_to_save_eml2o = [
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
        propagation_setup.dependent_variable.central_body_fixed_cartesian_position("EML2O", "Moon")
    ]

    dependent_variables_to_save_elo = [
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
        propagation_setup.dependent_variable.central_body_fixed_cartesian_position("ELO", "Moon")
    ]

    termination_condition = propagation_setup.propagator.time_termination(simulation_end_epoch)
    propagation_settings_eml2o = propagation_setup.propagator.translational(
        for_eml2o.central_bodies,
        for_eml2o.acceleration_models,
        for_eml2o.body_to_propagate,
        X0_eml2o,
        termination_condition,
        output_variables=dependent_variables_to_save_eml2o
    )
    propagation_settings_elo = propagation_setup.propagator.translational(
        for_elo.central_bodies,
        for_elo.acceleration_models,
        for_elo.body_to_propagate,
        X0_elo,
        termination_condition,
        output_variables=dependent_variables_to_save_elo
    )

    ### Integrating ###
    integrator_settings = numerical_simulation.propagation_setup.integrator.runge_kutta_4(
        simulation_start_epoch, fixed_time_step
    )

    dynamic_simulator_eml2o = numerical_simulation.SingleArcSimulator(
        for_eml2o.bodies, integrator_settings, propagation_settings_eml2o
    )

    dynamic_simulator_elo = numerical_simulation.SingleArcSimulator(
        for_elo.bodies, integrator_settings, propagation_settings_elo
    )

    states_eml2o_dict = dynamic_simulator_eml2o.state_history
    states_elo_dict = dynamic_simulator_elo.state_history

    output_eml2o_dict = dynamic_simulator_eml2o.dependent_variable_history
    output_elo_dict = dynamic_simulator_elo.dependent_variable_history

    return [states_eml2o_dict, states_elo_dict, output_eml2o_dict, output_elo_dict]




