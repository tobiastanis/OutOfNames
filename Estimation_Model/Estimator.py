"""
Extended Kalman Filter Function
"""
import numpy as np
from Initials.Simulation_Time_Setup import SWITCH
from Initials import  Simulation_Time_Setup
from Measurement_Model import measurement_functions
from Estimation_Model import Estimation_Setup
from Estimation_Model import estimator_functions
from Estimation_Model import integrators

dt = Estimation_Setup.dt
sigma_noise = Simulation_Time_Setup.sigma_noise
bias = Simulation_Time_Setup.bias
noise_dot = Simulation_Time_Setup.noise_dot
bias_dot = Simulation_Time_Setup.bias_dot

def ekf(X0, P0, R, Y, t_span):
    "Initializing"
    Xhat_k = X0
    Pk = P0

    for i in range(len(t_span)):
        print(i) #Counter
        t_k_1 = t_span[i]
        #Initialiing X, P, Y
        Xstar_k_1 = Xhat_k  # States in previous timestep
        P_k_1 = Pk          # Covariance matrix in previous timestep
        Yk = Y[i+1]         # Nominal observations in current timestep

        # Xstar_k_1 -------> Xstar_k (timestep integration)
        [Xstar_k, Phi] = integrators.dynamic_integrator1(t_k_1, dt, t_k_1+dt, Xstar_k_1)

        # Y_ref from Xstar_k
        est_range_observ = measurement_functions.range_observations(Xstar_k, bias, sigma_noise)
        est_rangerate_observ = measurement_functions.rangerate_observation_row(Xstar_k, bias_dot, noise_dot)

        Y_ref = estimator_functions.observations(est_range_observ, est_rangerate_observ, SWITCH)

        # Time updating P_k_1 to P_flat_k
        P_flat_k = np.add(np.matmul(np.matmul(Phi, P_k_1), np.transpose(Phi)), Estimation_Setup.Qdt)

        # Observation difference
        y = Yk - Y_ref
        

