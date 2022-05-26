"""
Extended Kalman Filter Function
"""
import numpy as np

from Estimation_Model import Estimation_Setup
from Estimation_Model import estimator_functions

def ekf(X0, P0, R, Y, t_span):
    "Initializing"
    Xhat_k = X0
    Pk = P0

    for i in range(len(t_span)):
        print(i) #Counter
        t_k_1 = t_span[i]
        #Initialiing iteration
        Xstar_k_1 = Xhat_k  # States in previous timestep
        P_k_1 = Pk          # Covariance matrix in previous timestep
        Yk = Y[i+1]         # Nominal observations in current timestep
        # Xstar_k_1 -------> Xstar_k (timestep integration)


