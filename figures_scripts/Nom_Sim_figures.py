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
from Measurement_Model.measurement_functions import h_wrt_moon_states
#tudatpy

time = Simulation_Time_Setup.simulation_span

#States wrt Earth in km
states = Data_Loader.json_2states_reader(Simulation_Time_Setup.DIRECTORY_NAME)
x_moon = moon_ephemeris(Simulation_Time_Setup.simulation_span_ephemeris) * 10 ** -3
x_eml2o = states[:, 0:6] * 10 ** -3
x_elo = states[:, 6:12] * 10 ** -3


output_eml2o = Data_Loader.json_eml2o_output_reader(Simulation_Time_Setup.DIRECTORY_NAME)
output_elo = Data_Loader.json_elo_output_reader(Simulation_Time_Setup.DIRECTORY_NAME)

#States wrt Moon in km
x_eml2o_moon = output_eml2o[:, 14:17] * 10 ** -3
x_elo_moon = output_elo[:, 14:17] * 10 ** -3

intersatellite_vector = np.subtract(x_eml2o[:, 0:3], x_elo[:, 0:3])
intersatellite_distance = np.linalg.norm(intersatellite_vector, axis=1)
print(intersatellite_distance)

max_intersatellitedistance = max(intersatellite_distance)
min_intersatellitedistance = min(intersatellite_distance)

print('Max inter-satellite distance:', max_intersatellitedistance, 'km')
print('Min inter-satellite distance:', min_intersatellitedistance, 'km')


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

plt.figure()
plot = plt.axes(projection='3d')
plot.plot(x_eml2o_moon[:, 0], x_eml2o_moon[:, 1], x_eml2o_moon[:, 2], color='orange')
plot.plot(x_elo_moon[:, 0], x_elo_moon[:, 1], x_elo_moon[:, 2], color='red')
plot.plot(0, 0, 0, marker='o', markersize=10, color='grey')
plot.plot(x_eml2o_moon[0, 0], x_eml2o_moon[0, 1], x_eml2o_moon[0, 2], marker='o', markersize=5,  color='orange')
plot.plot(x_elo_moon[0, 0], x_elo_moon[0, 1], x_elo_moon[0, 2], marker='o', markersize=5, color='red')
plt.title('Moon-Satellites System')
plt.legend(['EML2O', 'ELO', 'Moon'])
plot.set_xlabel('x-direction [km]')
plot.set_ylabel('y-direction [km]')
plot.set_zlabel('z-direction [km]')

plt.figure()
plot = plt.axes(projection='3d')
plot.plot(x_elo_moon[:, 0], x_elo_moon[:, 1], x_elo_moon[:, 2], color='red')
plot.plot(0, 0, 0, marker='o', markersize=10, color='grey')
plot.plot(x_elo_moon[0, 0], x_elo_moon[0, 1], x_elo_moon[0, 2], marker='o', markersize=3, color='red')
plt.title('Moon-ELO System')
plt.legend(['ELO', 'Moon'])
plot.set_xlabel('x-direction [km]')
plot.set_ylabel('y-direction [km]')
plot.set_zlabel('z-direction [km]')

fig1, (ax1, ax2, ax3) = plt.subplots(3, 1, constrained_layout=True)
ax1.plot(x_eml2o_moon[:, 0], x_eml2o_moon[:, 1], color='orange')
ax1.plot(x_elo_moon[:, 0], x_elo_moon[:, 1], color='red')
ax1.plot(0, 0, marker='o', markersize=8, color='grey')
ax1.plot(x_eml2o_moon[0, 0], x_eml2o_moon[0, 1], marker='o', markersize=5, color='orange')
ax1.plot(x_elo_moon[0, 0], x_elo_moon[0, 1], marker='o', markersize=5, color='red')
ax1.set_xlabel('x-direction [km]')
ax1.set_ylabel('y-direction [km]')
ax1.set_title('Moon-centered trajectories in xy-plane')
ax2.plot(x_eml2o_moon[:, 0], x_eml2o_moon[:, 2], color='orange')
ax2.plot(x_elo_moon[:, 0], x_elo_moon[:, 2], color='red')
ax2.plot(0, 0, marker='o', markersize=8, color='grey')
ax2.plot(x_eml2o_moon[0, 0], x_eml2o_moon[0, 2], marker='o', markersize=5, color='orange')
ax2.plot(x_elo_moon[0, 0], x_elo_moon[0, 2], marker='o', markersize=5, color='red')
ax2.set_xlabel('x-direction [km]')
ax2.set_ylabel('z-direction [km]')
ax2.set_title('Moon-centered trajectories in xz-plane')
ax3.plot(x_eml2o_moon[:, 1], x_eml2o_moon[:, 2], color='orange')
ax3.plot(x_elo_moon[:, 1], x_elo_moon[:, 2], color='red')
ax3.plot(0, 0, marker='o', markersize=8, color='grey')
ax3.plot(x_eml2o_moon[0, 1], x_eml2o_moon[0, 2], marker='o', markersize=5, color='orange')
ax3.plot(x_elo_moon[0, 1], x_elo_moon[0, 2], marker='o', markersize=5, color='red')
ax3.set_xlabel('y-direction [km]')
ax3.set_ylabel('z-direction [km]')
ax3.set_title('Moon-centered trajectories in yz-plane')
ax2.legend(['EML2O', 'ELO', 'Moon'], loc='upper left', bbox_to_anchor=(1, 1))

fig2, (ax1, ax2, ax3) = plt.subplots(3, 1, constrained_layout=True)
ax1.plot(x_elo_moon[:, 0], x_elo_moon[:, 1], color='red')
ax1.plot(0, 0, marker='o', markersize=8, color='grey')
ax1.plot(x_elo_moon[0, 0], x_elo_moon[0, 1], marker='o', markersize=5, color='red')
ax1.set_xlabel('x-direction [km]')
ax1.set_ylabel('y-direction [km]')
ax1.set_title('Moon-centered ELO trajectory in xy-plane')
ax2.plot(x_elo_moon[:, 0], x_elo_moon[:, 2], color='red')
ax2.plot(0, 0, marker='o', markersize=8, color='grey')
ax2.plot(x_elo_moon[0, 0], x_elo_moon[0, 2], marker='o', markersize=5, color='red')
ax2.set_xlabel('x-direction [km]')
ax2.set_ylabel('z-direction [km]')
ax2.set_title('Moon-centered ELO trajectory in xz-plane')
ax3.plot(x_elo_moon[:, 1], x_elo_moon[:, 2], color='red')
ax3.plot(0, 0, marker='o', markersize=8, color='grey')
ax3.plot(x_elo_moon[0, 1], x_elo_moon[0, 2], marker='o', markersize=5, color='red')
ax3.set_xlabel('y-direction [km]')
ax3.set_ylabel('z-direction [km]')
ax3.set_title('Moon-centered ELO trajectory in yz-plane')
ax2.legend(['ELO', 'Moon'], loc='upper left', bbox_to_anchor=(1, 1))

fig3, (ax1, ax2, ax3) = plt.subplots(3, 1, constrained_layout=True, sharey=True)
ax1.plot(x_eml2o[:, 0], x_eml2o[:, 1], color='orange')
ax1.plot(x_elo[:, 0], x_elo[:, 1], color='red')
ax1.plot(x_moon[:, 0], x_moon[:, 1], color='grey')
ax1.plot(0, 0, marker='o', markersize=10, color='blue')
ax1.plot(x_eml2o[0, 0], x_eml2o[0, 1], marker='o', markersize=3, color='orange')
ax1.plot(x_elo[0, 0], x_elo[0, 1], marker='o', markersize=3, color='red')
ax1.plot(x_moon[0, 0], x_moon[0, 1],marker='o', markersize=3, color='grey')
ax1.set_title('Earth-centered trajectories in xy-plane')
ax1.set_xlabel('x-direction [km]')
ax1.set_ylabel('y-direction [km]')
ax2.plot(x_eml2o[:, 0], x_eml2o[:, 2], color='orange')
ax2.plot(x_elo[:, 0], x_elo[:, 2], color='red')
ax2.plot(x_moon[:, 0], x_moon[:, 2], color='grey')
ax2.plot(0, 0, marker='o', markersize=10, color='blue')
ax2.plot(x_eml2o[0, 0], x_eml2o[0, 2], marker='o', markersize=3, color='orange')
ax2.plot(x_elo[0, 0], x_elo[0, 2], marker='o', markersize=3, color='red')
ax2.plot(x_moon[0, 0], x_moon[0, 2],marker='o', markersize=3, color='grey')
ax2.set_title('Earth-centered trajectories in xz-plane')
ax2.set_xlabel('x-direction [km]')
ax2.set_ylabel('z-direction [km]')
ax3.plot(x_eml2o[:, 1], x_eml2o[:, 2], color='orange')
ax3.plot(x_elo[:, 1], x_elo[:, 2], color='red')
ax3.plot(x_moon[:, 1], x_moon[:, 2], color='grey')
ax3.plot(0, 0, marker='o', markersize=10, color='blue')
ax3.plot(x_eml2o[0, 1], x_eml2o[0, 2], marker='o', markersize=3, color='orange')
ax3.plot(x_elo[0, 1], x_elo[0, 2], marker='o', markersize=3, color='red')
ax3.plot(x_moon[0, 1], x_moon[0, 2],marker='o', markersize=3, color='grey')
ax3.set_title('Earth-centered trajectories in yz-plane')
ax3.set_xlabel('y-direction [km]')
ax3.set_ylabel('z-direction [km]')
ax2.legend(['EML2O', 'ELO', 'Moon', 'Earth'], loc='upper left', bbox_to_anchor=(1, 1))

plt.figure()
plt.title("Breakdown of the accelerations acting on EML2O")
plt.plot(time, output_eml2o[:, 3])
plt.plot(time, output_eml2o[:, 4])
plt.plot(time, output_eml2o[:, 5])
plt.plot(time, output_eml2o[:, 6])
plt.plot(time, output_eml2o[:, 7])
plt.plot(time, output_eml2o[:, 8])
plt.plot(time, output_eml2o[:, 9])
plt.plot(time, output_eml2o[:, 10])
plt.plot(time, output_eml2o[:, 11])
plt.plot(time, output_eml2o[:, 12])
plt.plot(time, output_eml2o[:, 13])
plt.yscale("log")
plt.grid(True, which="both", ls="--")
plt.ylim(10**-16, 10**0)
plt.xlim(0,14)
plt.xlabel('Time [day]')
plt.ylabel('Acceleration [m/$s^{2}$]')
plt.legend(['SRP', 'SH Earth', 'SH Moon', 'PM Sun', 'PM Mercury', 'PM Venus',
            'PM Mars', 'PM Jupiter', 'PM Saturn', 'PM Uranus', 'PM Neptune']
           , loc='upper left', bbox_to_anchor=(1, 1))

plt.figure()
plt.title("Breakdown of the accelerations acting on EML2O")
plt.plot(time, output_elo[:, 3])
plt.plot(time, output_elo[:, 4])
plt.plot(time, output_elo[:, 5])
plt.plot(time, output_elo[:, 6])
plt.plot(time, output_elo[:, 7])
plt.plot(time, output_elo[:, 8])
plt.plot(time, output_elo[:, 9])
plt.plot(time, output_elo[:, 10])
plt.plot(time, output_elo[:, 11])
plt.plot(time, output_elo[:, 12])
plt.plot(time, output_elo[:, 13])
plt.yscale("log")
plt.grid(True, which="both", ls="--")
plt.ylim(10**-16, 10**0)
plt.xlim(0,14)
plt.xlabel('Time [day]')
plt.ylabel('Acceleration [m/$s^{2}$]')
plt.legend(['SRP', 'SH Earth', 'SH Moon', 'PM Sun', 'PM Mercury', 'PM Venus',
            'PM Mars', 'PM Jupiter', 'PM Saturn', 'PM Uranus', 'PM Neptune']
           , loc='upper left', bbox_to_anchor=(1, 1))

h = h_wrt_moon_states(x_eml2o_moon, x_elo_moon)
plt.figure()
plt.plot(Simulation_Time_Setup.simulation_span, h)
plt.hlines(y=1800, xmin=min(Simulation_Time_Setup.simulation_span), xmax=max(Simulation_Time_Setup.simulation_span), linewidth=1, color='r')


plt.show()