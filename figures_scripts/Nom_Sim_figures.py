"""
First rerun the nom sinulation and add and save the output of 200_200
make figures again:)
figuren in overleaf smijten
"""
#general
import matplotlib.pyplot as plt
import numpy as np
#own
from Initials import Simulation_Time_Setup
from Initials.initial_states_obtainer import moon_ephemeris
from Saved_Data import Data_Loader
#tudatpy


#States wrt Earth in km
states = Data_Loader.json_2states_reader(Simulation_Time_Setup.DIRECTORY_NAME)
x_moon = moon_ephemeris(Simulation_Time_Setup.simulation_span_ephemeris) * 10 ** -3
x_eml2o = states[:, 0:6] * 10 ** -3
x_elo = states[:, 6:12] * 10 ** -3

#States wrt Moon in km
x_eml2o_moon = np.subtract(x_eml2o, x_moon)
x_elo_moon = np.subtract(x_elo, x_moon)


"3D-figure of the Earth-Moon satellites system"
plt.figure()
plot = plt.axes(projection='3d')
plot.plot(x_eml2o[:, 0], x_eml2o[:, 1], x_eml2o[:, 2], color='orange')
plot.plot(x_elo[:, 0], x_elo[:, 1], x_elo[:, 2], color='red')
plot.plot(x_moon[:, 0], x_moon[:, 1], x_moon[:, 2], color='grey')
plot.plot(0, 0, 0, marker='o', markersize=10, color='blue')
plot.plot(x_eml2o[0, 0], x_eml2o[0, 1], x_eml2o[0, 2], marker='o', markersize=3,  color='orange')
plot.plot(x_elo[0, 0], x_elo[0, 1], x_elo[0, 2], marker='o', markersize=3, color='red')
plot.plot(x_moon[0, 0], x_moon[0, 1], x_moon[0, 2], marker='o', markersize=3, color='grey')
plt.title('Earth-Moon-Satellites System')
plt.legend(['EML2O', 'ELO', 'Moon', 'Earth'])
plot.set_xlabel('x-direction [km]')
plot.set_ylabel('y-direction [km]')
plot.set_zlabel('z-direction [km]')

"Trajectories wrt Moon, WRONG"
fig1, (ax1, ax2, ax3) = plt.subplots(3, 1, constrained_layout=True)
ax1.plot(x_eml2o_moon[:, 0], x_eml2o_moon[:, 1], color='orange')
ax1.plot(x_elo_moon[:, 0], x_elo_moon[:, 1], color='green')
ax1.plot(0, 0, marker='o', markersize=8, color='grey')
ax1.plot(x_eml2o_moon[0, 0], x_eml2o_moon[0, 1], marker='o', markersize=8, color='orange')
ax1.plot(x_elo_moon[0, 0], x_elo_moon[0, 1], marker='o', markersize=8, color='green')



plt.show()