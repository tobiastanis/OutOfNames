#general
import numpy as np
#own
from Initials import Simulation_Time_Setup
from Satellites_list.EML2O import EML2O
from Satellites_list.ELO import ELO
#tudatpy
from tudatpy.kernel import numerical_simulation
from tudatpy.kernel.numerical_simulation import propagation_setup
from tudatpy.kernel.numerical_simulation import estimation_setup

def integrator(t0, dt, tend, X0_eml2o, X0_elo, NAME):

    if NAME == "Three_Body_system_PM":
        from Nominal_Dynamic_Model.Environments.Three_Body_System_PM import three_body_system_pm
        for_eml2o = three_body_system_pm(
            name=EML2O.name,
            mass=EML2O.mass,
            Aref=EML2O.reference_area,
            Cr=EML2O.radiation_pressure_coefficient,
            occulting_bodies=EML2O.occulting_bodies,
            t0=t0,
            tend=tend,
            dt=dt
        )
        for_elo = three_body_system_pm(
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

    if NAME == "Three_Body_system_PM_NO_SRP":
        from Nominal_Dynamic_Model.Environments.Three_Body_system_PM_NO_SRP import three_body_system_pm_no_srp
        for_eml2o = three_body_system_pm_no_srp(
            name=EML2O.name,
            mass=EML2O.mass,
            t0=t0,
            tend=tend,
            dt=dt
        )
        for_elo = three_body_system_pm_no_srp(
            name=ELO.name,
            mass=ELO.mass,
            t0=t0,
            tend=tend,
            dt=dt
        )
        eml2o_variables = for_eml2o.create_variables()
        elo_variables = for_elo.create_variables()

    simulation_start_epoch = t0
    simulation_end_epoch = tend
    fixed_time_step = dt

    termination_condition = propagation_setup.propagator.time_termination(tend)
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




