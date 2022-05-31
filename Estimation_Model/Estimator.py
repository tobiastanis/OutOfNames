"""
Extended Kalman Filter Function
"""
#general
import numpy as np
#own
from Initials.Simulation_Time_Setup import SWITCH
from Initials import  Simulation_Time_Setup
from Measurement_Model import measurement_functions
from Measurement_Model.Nominal_Observations_Cooker import states
from Estimation_Model import Estimation_Setup
from Estimation_Model import estimator_functions
from Satellites_list.EML2O import EML2O
from Satellites_list.ELO import ELO
from Estimation_Model.integrator_class import EstimationClass
#tudatpy
from tudatpy.kernel import numerical_simulation
from tudatpy.kernel.numerical_simulation import propagation_setup
from tudatpy.kernel.numerical_simulation import estimation_setup

eph_time = Estimation_Setup.ephemeris_span
dt = Estimation_Setup.dt
#Loading in environment and accelerations
for_eml2 = EstimationClass(name=EML2O.name,
                           mass=EML2O.mass,
                           Aref=EML2O.reference_area,
                           Cr=EML2O.radiation_pressure_coefficient,
                           occulting_bodies=EML2O.occulting_bodies,
                           t0=min(eph_time),
                           tend=max(eph_time),
                           dt=dt
                           )
for_elo = EstimationClass(name=ELO.name,
                          mass=ELO.mass,
                          Aref=ELO.reference_area,
                          Cr=ELO.radiation_pressure_coefficient,
                          occulting_bodies=ELO.occulting_bodies,
                          t0=min(eph_time),
                          tend=max(eph_time),
                          dt=dt
                          )
eml2_variables = for_eml2.create_variables()
elo_variables = for_elo.create_variables()

#errors
sigma_noise = Simulation_Time_Setup.sigma_noise
bias = Simulation_Time_Setup.bias
noise_dot = Simulation_Time_Setup.noise_dot
bias_dot = Simulation_Time_Setup.bias_dot

def ekf(X0, P0, R, Y, t_span):
    #Initialzing
    Xhat_k = X0

    Pk = P0

    #arrays to fill
    X_ekf = []
    std_Pk = []
    X_ekf.append(np.transpose(Xhat_k)[0])
    std_Pk.append(np.sqrt(np.diag(Pk)))

    for i in range(len(t_span)-1):
        print(i) #Counter
        t_k_1 = t_span[i]
        #Initialiing X, P, Y
        Xstar_k_1 = Xhat_k  # States in previous timestep
        P_k_1 = Pk          # Covariance matrix in previous timestep
        Yk = Y[i+1]

        # Xstar_k_1 -------> Xstar_k (timestep integration)
        #[Xstar_k, Phi] = integrators.dynamic_integrator1(t_k_1, dt, t_k_1+dt, Xstar_k_1)

        termination_condition = propagation_setup.propagator.time_termination(t_k_1+dt)
        propagation_settings_eml2 = propagation_setup.propagator.translational(
            for_eml2.central_bodies, for_eml2.acceleration_models, for_eml2.body_to_propagate, Xstar_k_1[0:6],
            termination_condition)
        propagation_settings_elo = propagation_setup.propagator.translational(
            for_elo.central_bodies, for_elo.acceleration_models, for_elo.body_to_propagate, Xstar_k_1[6:12],
            termination_condition)

        integrator_settings = numerical_simulation.propagation_setup.integrator.runge_kutta_4(t_k_1, 1/3*dt)

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
        X_eml2o = variational_eqn_solver_eml2.state_history[t_k_1+dt]
        X_elo = variational_eqn_solver_elo.state_history[t_k_1+dt]
        ##### Time updated states #####
        Xstar_k = np.vstack([X_eml2o.reshape(-1,1), X_elo.reshape(-1,1)])
        ##### Time updated Phi #####
        Phi_eml2 = variational_eqn_solver_eml2.state_transition_matrix_history[t_k_1+dt]
        Phi_elo = variational_eqn_solver_elo.state_transition_matrix_history[t_k_1+dt]
        Phi = estimator_functions.Phi(Phi_eml2, Phi_elo)

        # Time update covariance matrix
        P_flat_k = np.add(np.matmul(np.matmul(Phi, P_k_1), np.transpose(Phi)), Estimation_Setup.Qdt)


        if Yk == 0:
            Xhat_k = Xstar_k
            Pk = P_flat_k
        else:
            # Y_ref from Xstar_k
            est_range_observ = measurement_functions.range_observation_row(Xstar_k, 0, 0)
            est_rangerate_observ = measurement_functions.rangerate_observation_row(Xstar_k, 0, 0)

            # Y_ref = G(X,t)
            Y_ref = estimator_functions.observations(est_range_observ, est_rangerate_observ, SWITCH)

            # Observation difference
            y = Yk - Y_ref

            # H
            H = estimator_functions.H(np.transpose(Xstar_k)[0], SWITCH)

            # Kalman gain K
            K = np.matmul(P_flat_k, np.transpose([H])) * (np.matmul(np.matmul(H, P_flat_k), np.transpose([H])) + R) ** -1
            # Measurement update Covariance Matrix
            Pk = np.matmul(np.subtract(np.eye(12, dtype=int), (K * H)), P_flat_k)
            # Measurement update X
            Xhat_k = np.add(Xstar_k, (K * y))

        # Savings
        X_ekf.append(np.transpose(Xhat_k)[0])
        std_Pk.append(np.sqrt(np.diag(Pk)))
    return [X_ekf, std_Pk]

[X, stdP] = ekf(Estimation_Setup.X0,
                Estimation_Setup.P0,
                Estimation_Setup.R,
                Estimation_Setup.Y_nominal,
                Estimation_Setup.ephemeris_span)
X = np.array(X)
stdP = np.array(stdP)

t = Simulation_Time_Setup.measurement_span_t

x_error = np.subtract(states, X)

import matplotlib.pyplot as plt
std_Pk_up = 3*stdP
std_Pk_down =-3*stdP

plt.figure()
plt.plot(t, x_error[:, 0], color='red', label='x')
plt.plot(t, x_error[:, 1], color='blue', label='y')
plt.plot(t, x_error[:, 2], color='green', label='z')
plt.plot(t, std_Pk_up[:, 0], color='orange', linestyle='--' , label='3$\sigma_{x}$')
plt.plot(t, std_Pk_down[:, 0], color='orange', linestyle='--')
plt.plot(t, std_Pk_up[:, 1], color='cyan', linestyle='--', label='3$\sigma_{y}$')
plt.plot(t, std_Pk_down[:, 1], color='cyan', linestyle='--')
plt.plot(t, std_Pk_up[:, 2], color='yellow', linestyle='--', label='3$\sigma_{z}$')
plt.plot(t, std_Pk_down[:, 2], color='yellow', linestyle='--')
plt.legend()
plt.xlim(0, 6)
plt.grid(True, which="both", ls="-")
plt.xlabel('Time since epoch [days]')
plt.ylabel('Estimated position error [m]')
plt.title('EML2 position error')

plt.figure()
plt.plot(t, x_error[:, 3], color='red', label='$\dot{x}$')
plt.plot(t, x_error[:, 4], color='blue', label='$\dot{y}$')
plt.plot(t, x_error[:, 5], color='green', label='$\dot{z}$')
plt.plot(t, std_Pk_up[:, 3], color='orange', linestyle='--', label='3$\sigma_{\dot{x}}$')
plt.plot(t, std_Pk_down[:, 3], color='orange', linestyle='--')
plt.plot(t, std_Pk_up[:, 4], color='cyan', linestyle='--', label='3$\sigma_{\dot{y}}$')
plt.plot(t, std_Pk_down[:, 4], color='cyan', linestyle='--')
plt.plot(t, std_Pk_up[:, 5], color='yellow', linestyle='--', label='3$\sigma_{\dot{z}}$')
plt.plot(t, std_Pk_down[:, 5], color='yellow', linestyle='--')
plt.legend()
plt.xlim(0, 6)
plt.grid(True, which="both", ls="-")
plt.xlabel('Time since epoch [days]')
plt.ylabel('Estimated velocity error [m/s]')
plt.title('EML2 velocity error')

plt.figure()
plt.plot(t, x_error[:, 6], color='red', label='x')
plt.plot(t, x_error[:, 7], color='blue', label='y')
plt.plot(t, x_error[:, 8], color='green', label='z')
plt.plot(t, std_Pk_up[:, 6], color='orange', linestyle='--', label='3$\sigma_{x}$')
plt.plot(t, std_Pk_down[:, 6], color='orange', linestyle='--')
plt.plot(t, std_Pk_up[:, 7], color='cyan', linestyle='--', label='3$\sigma_{y}$')
plt.plot(t, std_Pk_down[:, 7], color='cyan', linestyle='--')
plt.plot(t, std_Pk_up[:, 8], color='yellow', linestyle='--', label='3$\sigma_{z}$')
plt.plot(t, std_Pk_down[:, 8], color='yellow', linestyle='--')
plt.legend()
plt.xlim(0, 6)
plt.grid(True, which="both", ls="-")
plt.xlabel('Time since epoch [days]')
plt.ylabel('Estimated position error [m]')
plt.title('ELO position error')

plt.figure()
plt.plot(t, x_error[:, 9], color='red', label='$\dot{x}$')
plt.plot(t, x_error[:, 10], color='blue', label='$\dot{y}$')
plt.plot(t, x_error[:, 11], color='green', label='$\dot{z}$')
plt.plot(t, std_Pk_up[:, 9], color='orange', linestyle='--', label='3$\sigma_{\dot{x}}$')
plt.plot(t, std_Pk_down[:, 9], color='orange', linestyle='--')
plt.plot(t, std_Pk_up[:, 10], color='cyan', linestyle='--', label='3$\sigma_{\dot{y}}$')
plt.plot(t, std_Pk_down[:, 10], color='cyan', linestyle='--')
plt.plot(t, std_Pk_up[:, 11], color='yellow', linestyle='--', label='3$\sigma_{\dot{z}}$')
plt.plot(t, std_Pk_down[:, 11], color='yellow', linestyle='--')
plt.legend()
plt.xlim(0, 6)
plt.grid(True, which="both", ls="-")
plt.xlabel('Time since epoch [days]')
plt.ylabel('Estimated velocity error [m/s]')
plt.title('ELO velocity error')


plt.show()



