#own
from Satellites_list.EML2O import EML2O
from Satellites_list.ELO import ELO
#tudatpy
from tudatpy.kernel import numerical_simulation
from tudatpy.kernel.numerical_simulation import propagation_setup

def integrator(t0, dt, tend, X0_eml2o, X0_elo, NAME):
    if NAME != "Three_Body_System_PM" and NAME != "Three_Body_System_PM_NO_SRP" and NAME != "Solar_System"\
            and NAME != "Solar_System_200_200":
        quit("Integrator name is ill-defined, Check Initial/Simulation_Time_Setup line 18")

    if NAME == "Three_Body_System_PM_NO_SRP":
        from Nominal_Dynamic_Model.Environments.Three_Body_System_PM_NO_SRP import int_environment
    if NAME == "Three_Body_System_PM":
        from Nominal_Dynamic_Model.Environments.Three_Body_System_PM import int_environment
    if NAME == "Solar_System":
        from Nominal_Dynamic_Model.Environments.Solar_System import int_environment
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

    termination_condition = propagation_setup.propagator.time_termination(simulation_end_epoch)
    propagation_settings_eml2o = propagation_setup.propagator.translational(
        for_eml2o.central_bodies,
        for_eml2o.acceleration_models,
        for_eml2o.body_to_propagate,
        X0_eml2o,
        termination_condition,
    )
    propagation_settings_elo = propagation_setup.propagator.translational(
        for_elo.central_bodies,
        for_elo.acceleration_models,
        for_elo.body_to_propagate,
        X0_elo,
        termination_condition
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

    return [states_eml2o_dict, states_elo_dict]




