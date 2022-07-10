"""
Figures of Dynamic_Model.py
"""
# import external libraries
import numpy as np
import matplotlib.pyplot as plt
# import own libraries
from Initials import Simulation_Time_Setup
from Initials.initial_states_obtainer import moon_ephemeris
from Measurement_Model.measurement_functions import h_wrt_moon_states
from Saved_Data import Data_Loader

Simulation_Name = Simulation_Time_Setup.DIRECTORY_NAME
output = Data_Loader.json_output_reader(Simulation_Name)
states = Data_Loader.json_states_reader(Simulation_Name)

time = Simulation_Time_Setup.simulation_span
x_moon = moon_ephemeris(Simulation_Time_Setup.simulation_span_ephemeris) * 10 ** -3
x_eml2 = states[:, 0:6] * 10 ** -3
x_elo = states[:, 6:12] * 10 ** -3

plt.figure()
plot = plt.axes(projection='3d')
plot.plot(x_eml2[:, 0], x_eml2[:, 1], x_eml2[:, 2], color='orange')
plot.plot(x_elo[:, 0], x_elo[:, 1], x_elo[:, 2], color='red')
plot.plot(x_moon[:, 0], x_moon[:, 1], x_moon[:, 2], color='grey')
plot.plot(0, 0, 0, marker='o', markersize=10, color='blue')
plot.plot(x_eml2[0, 0], x_eml2[0, 1], x_eml2[0, 2], marker='o', markersize=3,  color='orange')
plot.plot(x_elo[0, 0], x_elo[0, 1], x_elo[0, 2], marker='o', markersize=3, color='red')
plot.plot(x_moon[0, 0], x_moon[0, 1], x_moon[0, 2], marker='o', markersize=3, color='grey')
plt.title('Earth-Moon-Satellites System')
plt.legend(['eml2', 'LLO orbiter', 'Moon', 'Earth'])
plot.set_xlabel('x-direction [km]')
plot.set_ylabel('y-direction [km]')
plot.set_zlabel('z-direction [km]')

plt.figure()
plot = plt.axes(projection='3d')
plot.plot(output[:, 31]*10**-3, output[:, 32]*10**-3, output[:, 33]*10**-3, color='orange')
plot.plot(0, 0, 0, marker='o', markersize=10, color='grey')
plot.plot(output[0, 31]*10**-3, output[0, 32]*10**-3, output[0, 33]*10**-3, color='orange')
plt.title('ELO-Moon System')
plt.legend(['LLO orbiter', 'Moon'])
plot.set_xlabel('x-direction [km]')
plot.set_ylabel('y-direction [km]')
plot.set_zlabel('z-direction [km]')

plt.figure()
plot = plt.axes(projection='3d')
plot.plot(output[:, 28]*10**-3, output[:, 29]*10**-3, output[:, 30]*10**-3, color='orange')
plot.plot(output[:, 31]*10**-3, output[:, 32]*10**-3, output[:, 33]*10**-3, color='orange')
plot.plot(0, 0, 0, marker='o', markersize=10, color='grey')
plot.plot(output[0, 31]*10**-3, output[0, 32]*10**-3, output[0, 33]*10**-3, color='orange')
plot.plot(output[0, 28]*10**-3, output[0, 29]*10**-3, output[0, 30]*10**-3, color='orange')
plt.title('ELO-Moon System')
plt.legend(['EML2O', 'LLO orbiter', 'Moon'])
plot.set_xlabel('x-direction [km]')
plot.set_ylabel('y-direction [km]')
plot.set_zlabel('z-direction [km]')

fig1, (ax1, ax2, ax3) = plt.subplots(3, 1, constrained_layout=True, sharey=True)
ax1.plot(x_eml2[:, 0], x_eml2[:, 1], color='orange')
ax1.plot(x_moon[:, 0], x_moon[:, 1], color='grey')
ax1.plot(x_elo[:, 0], x_elo[:, 1], color='red')
ax1.plot(0, 0, marker='o', markersize=10, color='blue')
ax1.plot(x_eml2[0, 0], x_eml2[0, 1], marker='o', markersize=3, color='orange')
ax1.plot(x_moon[0, 0], x_moon[0, 1],marker='o', markersize=3, color='grey')
ax1.plot(x_elo[0, 0], x_elo[0, 1], marker='o', markersize=3, color='red')
ax1.set_title('Earth-centered trajectory in xy-plane')
ax1.set_xlabel('x-direction [km]')
ax1.set_ylabel('y-direction [km]')
ax2.plot(x_eml2[:, 0], x_eml2[:, 2], color='orange')
ax2.plot(x_moon[:, 0], x_moon[:, 2], color='grey')
ax2.plot(x_elo[:, 0], x_elo[:, 2], color='red')
ax2.plot(0, 0, marker='o', markersize=10, color='blue')
ax2.plot(x_eml2[0, 0], x_eml2[0, 2], marker='o', markersize=3, color='orange')
ax2.plot(x_moon[0, 0], x_moon[0, 2],marker='o', markersize=3, color='grey')
ax2.plot(x_elo[0, 0], x_elo[0, 2], marker='o', markersize=3, color='red')
ax2.set_title('Earth-centered trajectory in xz-plane')
ax2.set_xlabel('x-direction [km]')
ax2.set_ylabel('z-direction [km]')
ax3.plot(x_eml2[:, 1], x_eml2[:, 2], color='orange')
ax3.plot(x_moon[:, 1], x_moon[:, 2], color='grey')
ax3.plot(x_elo[:, 1], x_elo[:, 2], color='red')
ax3.plot(0, 0, marker='o', markersize=10, color='blue')
ax3.plot(x_eml2[0, 1], x_eml2[0, 2], marker='o', markersize=3, color='orange')
ax3.plot(x_moon[0, 1], x_moon[0, 2],marker='o', markersize=3, color='grey')
ax3.plot(x_elo[0, 1], x_elo[0, 2], marker='o', markersize=3, color='red')
ax3.set_title('Earth-centered trajectory in yz-plane')
ax3.set_xlabel('y-direction [km]')
ax3.set_ylabel('z-direction [km]')
ax2.legend(['eml2 trajectory', 'Moon trajectory', 'elo trajectory', 'Earth'], loc='upper left', bbox_to_anchor=(1, 1))

"""
28, Body-fixed relative Cartesian position of EML2O w.r.t. Moon
31, Body-fixed relative Cartesian position of ELO w.r.t. Moon
"""
fig2, (ax1, ax2, ax3) = plt.subplots(3, 1, constrained_layout=True, sharey=True)
ax1.plot(output[:, 31]*10**-3, output[:, 32]*10**-3)
ax1.plot(0, 0, marker='o', markersize=6, color='grey')
ax1.set_title('Moon-centered trajectory of ELO in xy-plane')
ax1.set_xlabel('x-direction [km]')
ax1.set_ylabel('y-direction [km]')
ax2.plot(output[:, 31]*10**-3, output[:, 33]*10**-3)
ax2.plot(0, 0, marker='o', markersize=6, color='grey')
ax2.set_title('Moon-centered trajectory of ELO in xz-plane')
ax2.set_xlabel('x-direction [km]')
ax2.set_ylabel('z-direction [km]')
ax3.plot(output[:, 32]*10**-3, output[:, 33]*10**-3)
ax3.plot(0, 0, marker='o', markersize=6, color='grey')
ax3.set_title('Moon-centered trajectory of ELO in yz-plane')
ax3.set_xlabel('y-direction [km]')
ax3.set_ylabel('z-direction [km]')

fig3, (ax1, ax2, ax3) = plt.subplots(3, 1, constrained_layout=True, sharey=True)
ax1.plot(output[:, 31]*10**-3, output[:, 32]*10**-3, color='red')
ax1.plot(output[:, 28]*10**-3, output[:, 29]*10**-3, color='orange')
ax1.plot(0, 0, marker='o', markersize=6, color='grey')
ax1.set_title('Moon-centered trajectory of ELO in xy-plane')
ax1.set_xlabel('x-direction [km]')
ax1.set_ylabel('y-direction [km]')
ax2.plot(output[:, 31]*10**-3, output[:, 33]*10**-3, color='red')
ax2.plot(output[:, 28]*10**-3, output[:, 30]*10**-3, color='orange')
ax2.plot(0, 0, marker='o', markersize=6, color='grey')
ax2.set_title('Moon-centered trajectory of ELO in xz-plane')
ax2.set_xlabel('x-direction [km]')
ax2.set_ylabel('z-direction [km]')
ax3.plot(output[:, 32]*10**-3, output[:, 33]*10**-3, color='red')
ax3.plot(output[:, 29]*10**-3, output[:, 30]*10**-3, color='orange')
ax3.plot(0, 0, marker='o', markersize=6, color='grey')
ax3.set_title('Moon-centered trajectory of ELO in yz-plane')
ax3.set_xlabel('y-direction [km]')
ax3.set_ylabel('z-direction [km]')

plt.figure()
plt.title("Breakdown of the accelerations acting on eml2")
plt.plot(time, output[:, 3])
plt.plot(time, output[:, 4])
plt.plot(time, output[:, 5])
plt.plot(time, output[:, 6])
plt.plot(time, output[:, 7])
plt.plot(time, output[:, 8])
plt.plot(time, output[:, 9])
plt.plot(time, output[:, 10])
plt.plot(time, output[:, 11])
plt.plot(time, output[:, 12])
plt.plot(time, output[:, 13])
plt.yscale("log")
plt.grid(True, which="both", ls="--")
plt.ylim(10**-16, 10**0)
plt.xlim(0,10)
plt.xlabel('Time [day]')
plt.ylabel('Acceleration [m/$s^{2}$]')
plt.legend(['SRP', 'PM Earth', 'PM Moon', 'PM Sun', 'PM Mercury', 'PM Venus',
            'PM Mars', 'PM Jupiter', 'PM Saturn', 'PM Uranus', 'PM Neptune']
           , loc='upper left', bbox_to_anchor=(1, 1))
plt.figure()
#plt.plot(time, np.linalg.norm(output[:, 14:17], axis=1))
plt.title("Breakdown of the accelerations acting on the elo")
plt.plot(time, output[:, 17])
plt.plot(time, output[:, 18])
plt.plot(time, output[:, 19])
plt.plot(time, output[:, 20])
plt.plot(time, output[:, 21])
plt.plot(time, output[:, 22])
plt.plot(time, output[:, 23])
plt.plot(time, output[:, 24])
plt.plot(time, output[:, 25])
plt.plot(time, output[:, 26])
plt.plot(time, output[:, 27])
plt.grid(True, which="both", ls="--")
plt.yscale('log')
plt.ylim(10**-16, 10**0)
plt.xlim(0,10)
plt.xlabel('Time [day]')
plt.ylabel('Acceleration [m/$s^{2}$]')
plt.legend(['SRP', 'PM Earth', 'SH Moon', 'PM Sun', 'PM Mercury', 'PM Venus',
            'PM Mars', 'PM Jupiter', 'PM Saturn', 'PM Uranus', 'PM Neptune']
           , loc='upper left', bbox_to_anchor=(1, 1))






plt.show()
