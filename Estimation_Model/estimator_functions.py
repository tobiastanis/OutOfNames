"""
Function file for estimation functions
"""
import numpy as np

def observations(range, rangerate, switch):
    if switch == 0:
        observation_array = range
    if switch == 1:
        observation_array = np.concatenate(([range], [rangerate]), axis=0)
    if switch == 2:
        observation_array = rangerate
    return observation_array

def R_function(R_element, switch):
    if switch == 1:
        output = np.eye(2)*R_element
    else:
        output = R_element
    return output

def H(X, ID):
    x1 = X[0]; y1 = X[1]; z1 = X[2]; vx1 = X[3]; vy1 = X[4]; vz1 = X[5]
    x2 = X[6]; y2 = X[7]; z2 = X[8]; vx2 = X[9]; vy2 = X[10]; vz2 = X[11]
    rho_abs = ((x1 - x2) ** 2 + (y1 - y2) ** 2 + (z1 - z2) ** 2) ** 0.5
    if ID == 1:
        H = np.array([(x1-x2)/rho_abs, (y1-y2)/rho_abs, (z1-z2)/rho_abs, 0, 0, 0,
                        (-x1+x2)/rho_abs, (-y1+y2)/rho_abs, (-z1+z2)/rho_abs, 0, 0, 0])
    if ID == 2:
        H = np.array([(vx1 - vx2) / rho_abs, (vy1 - vy2) / rho_abs, (vz1 - vz2) / rho_abs,
                            (x1 - x2) / rho_abs, (y1 - y2) / rho_abs, (z1 - z2) / rho_abs,
                            (-vx1 + vx2) / rho_abs, (-vy1 + vy2) / rho_abs, (-vz1 + vz2) / rho_abs,
                            (-x1 + x2) / rho_abs, (-y1 + y2) / rho_abs, (-z1 + z2) / rho_abs])
    return H

# Phi
def Phi(Phi_EML2, Phi_ELO):
    Phi_top = np.concatenate((Phi_EML2, np.zeros((6, 6))), axis=1)
    Phi_bot = np.concatenate((np.zeros((6, 6)), Phi_ELO), axis=1)
    Phi = np.concatenate((Phi_top, Phi_bot), axis=0)
    return Phi

