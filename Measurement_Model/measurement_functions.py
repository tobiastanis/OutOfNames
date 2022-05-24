"""
function file for ranging and range rate functions
"""



def measurement_array(states, timestep):
    from Initials import Simulation_Time_Setup
    array_to_fill = []
    for i in range(len(Simulation_Time_Setup.n_steps_measure)):
        row = states[i]



def intersatellite_distance(X):
    x1 = X[0]; y1 = X[1]; z1 = X[2]; x2 = X[6]; y2 = X[7]; z2 = X[8]
    return ((x1 - x2) ** 2 + (y1 - y2) ** 2 + (z1 - z2) ** 2) ** 0.5
