"""
Extended Kalman Filter Function
"""
#general
import numpy as np
#own
from Initials import Simulation_Time_Setup
from Measurement_Model import measurement_functions
from Estimation_Model import Estimation_Setup
from Estimation_Model import estimator_functions
from Satellites_list.EML2O import EML2O
from Satellites_list.ELO import ELO
from Estimation_Model.integrator_class import EstimationClass
from Nominal_Dynamic_Model.Environments.Solar_System import solar_system
from Nominal_Dynamic_Model.Environments.Three_Body_System_PM import three_body_system_pm
#tudatpy
from tudatpy.kernel import numerical_simulation
from tudatpy.kernel.numerical_simulation import propagation_setup
from tudatpy.kernel.numerical_simulation import estimation_setup

eph_time = Estimation_Setup.ephemeris_span
dt = Estimation_Setup.dt
#Loading in environment and accelerations
for_eml2 = solar_system(
    name=EML2O.name,
    mass=EML2O.mass,
    Aref=EML2O.reference_area,
    Cr=EML2O.radiation_pressure_coefficient,
    occulting_bodies=EML2O.occulting_bodies,
    t0=min(eph_time),
    tend=max(eph_time),
    dt=dt
)
for_elo = solar_system(
    name=ELO.name,
    mass=ELO.mass,
    Aref=ELO.reference_area,
    Cr=ELO.radiation_pressure_coefficient,
    occulting_bodies=ELO.occulting_bodies,
    t0=min(eph_time),
    tend=max(eph_time),
    dt=dt
)
elo_variables = for_elo.create_variables()
eml2_variables = for_eml2.create_variables()

#errors
sigma_noise = Simulation_Time_Setup.sigma_noise
bias = Simulation_Time_Setup.bias
noise_dot = Simulation_Time_Setup.noise_dot
bias_dot = Simulation_Time_Setup.bias_dot

def aekf(X0, P0, Y, t_span):
    print("Start estimation process")
    #Initialzing
    Xhat_k = X0
    Pk = P0
    Q = Estimation_Setup.Qdt
    alpha = 0.3
    #arrays to fill
    X_ekf = []
    std_Pk = []
    visibility = []
    visibility.append(0)
    X_ekf.append(np.transpose(Xhat_k)[0])
    std_Pk.append(np.sqrt(np.diag(Pk)))


    for i in range(len(t_span)-1):
        #print(i) #Counter
        t_k_1 = t_span[i]
        t_k = t_span[i+1]
        #Initialiing X, P, Y
        Xstar_k_1 = Xhat_k  # States in previous timestep
        P_k_1 = Pk          # Covariance matrix in previous timestep
        Yk = Y[:,i+1]

        # Xstar_k_1 -------> Xstar_k (timestep integration)
        termination_condition = propagation_setup.propagator.time_termination(t_k)
        propagation_settings_eml2 = propagation_setup.propagator.translational(
            for_eml2.central_bodies, for_eml2.acceleration_models, for_eml2.body_to_propagate, Xstar_k_1[0:6],
            termination_condition)
        propagation_settings_elo = propagation_setup.propagator.translational(
            for_elo.central_bodies, for_elo.acceleration_models, for_elo.body_to_propagate, Xstar_k_1[6:12],
            termination_condition)

        integrator_settings = numerical_simulation.propagation_setup.integrator.runge_kutta_4(t_k_1, 1/6*(t_k - t_k_1))

        parameter_settings_eml2 = estimation_setup.parameter.initial_states(propagation_settings_eml2, for_eml2.bodies)
        parameter_settings_elo = estimation_setup.parameter.initial_states(propagation_settings_elo, for_elo.bodies)

        variational_eqn_solver_eml2 = numerical_simulation.SingleArcVariationalSimulator(
            for_eml2.bodies, integrator_settings, propagation_settings_eml2,
            estimation_setup.create_parameter_set(parameter_settings_eml2, for_eml2.bodies), integrate_on_creation=1
        )

        variational_eqn_solver_elo = numerical_simulation.SingleArcVariationalSimulator(
            for_elo.bodies, integrator_settings, propagation_settings_elo,
            estimation_setup.create_parameter_set(parameter_settings_elo, for_elo.bodies), integrate_on_creation=1
        )

        X_eml2o = variational_eqn_solver_eml2.state_history[t_k]
        X_elo = variational_eqn_solver_elo.state_history[t_k]

        ##### Time updated states #####
        Xstar_k = np.vstack([X_eml2o.reshape(-1,1), X_elo.reshape(-1,1)])
        ##### Time updated Phi #####
        Phi_eml2 = variational_eqn_solver_eml2.state_transition_matrix_history[t_k]
        Phi_elo = variational_eqn_solver_elo.state_transition_matrix_history[t_k]
        Phi = estimator_functions.Phi(Phi_eml2, Phi_elo)

        # Time update covariance matrix
        P_flat_k = np.add(np.matmul(np.matmul(Phi, P_k_1), np.transpose(Phi)), Q)


        if Yk[1] == 0:
            Xhat_k = Xstar_k
            Pk = P_flat_k
            visibility.append(0)
        else:
            # Y_ref from Xstar_k
            if Yk[0] == 1:
                Y_ref = measurement_functions.range_observation_row(Xstar_k, 0, 0)
            #est_range_observ = measurement_functions.range_observation_row(Xstar_k, 0, 0)
            if Yk[0] == 2:
                Y_ref = measurement_functions.rangerate_observation_row(Xstar_k, 0, 0)
            if Yk[0] != 1 and Yk[0] != 2:
                quit("Error: ID-value is incorrect")
            # Observation difference
            y = Yk[1] - Y_ref[0]

            # H
            H = estimator_functions.H(np.transpose(Xstar_k)[0], Yk[0])

            R = estimator_functions.weightobservations(sigma_noise, noise_dot, Yk[0])

            # Kalman gain K
            K = np.matmul(P_flat_k, np.transpose([H])) * (np.matmul(np.matmul(H, P_flat_k), np.transpose([H])) + R) ** -1

            # Measurement update Covariance Matrix
            Pk = np.matmul(np.subtract(np.eye(12, dtype=int), (K * H)), P_flat_k)
            # Measurement update X
            Xhat_k = np.add(Xstar_k, (K * y))
            visibility.append(1)

            #Describe QQQQQ
            Q = alpha*Q + (1-alpha)*K*y*y*np.transpose(K)

        # Savings
        X_ekf.append(np.transpose(Xhat_k)[0])
        std_Pk.append(np.sqrt(np.diag(Pk)))

    print("Finished estimation process")
    return [X_ekf, std_Pk, visibility]

