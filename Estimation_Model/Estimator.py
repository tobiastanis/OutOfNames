"""
Extended Kalman Filter Function
"""
import os
import numpy as np
from pathlib import Path
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

"""
dir_name = Simulation_Time_Setup.DIRECTORY_NAME
parent_dir = Path(__file__).parent.parent
working_dir = Path.joinpath(parent_dir, dir_name)
overwrite_path = 0
if os.path.exists(working_dir) and overwrite_path == Simulation_Time_Setup.OVERWRITE:
    quit("Path already exists and overwrite is not allowed (turn overwrite_path=1 to overwrite data)")
if not os.path.exists(working_dir):
    os.makedirs(working_dir)
quit()
"""
def ekf(X0, P0, R, Y, t_span):
    #Initialzing
    Xhat_k = X0

    Pk = P0

    #arrays to fill
    X_ekf = []
    std_Pk = []
    X_ekf.append(Xhat_k)
    std_Pk.append(np.sqrt(np.diag(Pk)))

    for i in range(len(t_span)):
        print(i) #Counter
        t_k_1 = t_span[i]
        #Initialiing X, P, Y
        Xstar_k_1 = Xhat_k  # States in previous timestep
        P_k_1 = Pk          # Covariance matrix in previous timestep
        if SWITCH == 1:
            Yk = np.transpose([Y[:, i+1]])         # Nominal observations in current timestep
        else:
            Yk = Y[i+1]

        # Xstar_k_1 -------> Xstar_k (timestep integration)
        [Xstar_k, Phi] = integrators.dynamic_integrator1(t_k_1, dt, t_k_1+dt, Xstar_k_1)

        # Y_ref from Xstar_k
        est_range_observ = measurement_functions.range_observation_row(Xstar_k, 0, 0)
        est_rangerate_observ = measurement_functions.rangerate_observation_row(Xstar_k, 0, 0)

        # Y_ref = G(X,t)
        Y_ref = estimator_functions.observations(est_range_observ, est_rangerate_observ, SWITCH)

        # Time updating P_k_1 to P_flat_k
        P_flat_k = np.add(np.matmul(np.matmul(Phi, P_k_1), np.transpose(Phi)), Estimation_Setup.Qdt)
        # Observation difference
        y = Yk - Y_ref

        # H
        H = estimator_functions.H(np.transpose(Xstar_k)[0], SWITCH)

        if SWITCH == 1:
            # Kalman Gain K
            K_left = np.matmul(P_flat_k, np.transpose(H))
            K_right = (np.matmul(np.matmul(H, P_flat_k), np.transpose(H)) + R) ** -1
            K = np.matmul(K_left, K_right)
            # Measurement update Covariance Matrix
            Pk = np.matmul(np.subtract(np.eye(12, dtype=int), (np.matmul(K,H))), P_flat_k)
            #Measurement update X
            Xhat_k = np.add(Xstar_k, np.matmul(K, y))

        else:
            # Kalman gain K
            K = np.matmul(P_flat_k, np.transpose([H])) * (np.matmul(np.matmul(H, P_flat_k), np.transpose([H])) + R) ** -1
            # Measurement update Covariance Matrix
            Pk = np.matmul(np.subtract(np.eye(12, dtype=int), (K * H)), P_flat_k)
            # Measurement update X
            Xhat_k = np.add(Xstar_k, (K * y))

        # Savings
        X_ekf.append(Xhat_k)
        std_Pk.append(np.sqrt(np.diag(Pk)))

    return [X_ekf, std_Pk]


[X, stdP] = ekf(Estimation_Setup.X0,
                Estimation_Setup.P0,
                Estimation_Setup.R,
                Estimation_Setup.Y_nominal,
                Estimation_Setup.ephemeris_span)




