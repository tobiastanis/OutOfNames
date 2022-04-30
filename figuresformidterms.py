"""
Figures of Dynamic_Model.py
"""
# import external libraries
import numpy as np
import matplotlib.pyplot as plt
# import own libraries
import Nominal_Simulation

time = Nominal_Simulation.simulation_span
output = Nominal_Simulation.output
x_moon = Nominal_Simulation.X_Moon * 10 ** -3
x_lumio = Nominal_Simulation.states[:, 0:6] * 10 ** -3
x_llosat = Nominal_Simulation.states[:, 6:12] * 10 ** -3


test_lumio_wrt_moon = np.subtract(x_lumio,x_moon)
test_relative_position_vector = np.subtract(x_lumio, x_llosat)

#plt.figure()
#plt.plot(time, np.linalg.norm(relative_position_vector, axis=1))
#plt.plot(time, np.linalg.norm(lumio_wrt_moon, axis=1))
#plt.plot(time, np.linalg.norm(test_relative_position_vector, axis=1))
#plt.plot(time, np.linalg.norm(test_lumio_wrt_moon, axis=1))

plt.figure()
plot = plt.axes(projection='3d')
plot.plot(x_lumio[:, 0], x_lumio[:, 1], x_lumio[:, 2], color='orange')
plot.plot(x_llosat[:, 0], x_llosat[:, 1], x_llosat[:, 2], color='red')
plot.plot(x_moon[:, 0], x_moon[:, 1], x_moon[:, 2], color='grey')
plot.plot(0, 0, 0, marker='o', markersize=10, color='blue')
plot.plot(x_lumio[0, 0], x_lumio[0, 1], x_lumio[0, 2], marker='o', markersize=3,  color='orange')
plot.plot(x_llosat[0, 0], x_llosat[0, 1], x_llosat[0, 2], marker='o', markersize=3, color='red')
plot.plot(x_moon[0, 0], x_moon[0, 1], x_moon[0, 2], marker='o', markersize=3, color='grey')
plt.title('Earth-Moon-Satellites System')
plt.legend(['LUMIO', 'LLO orbiter', 'Moon', 'Earth'])
plot.set_xlabel('x-direction [km]')
plot.set_ylabel('y-direction [km]')
plot.set_zlabel('z-direction [km]')

fig1, (ax1, ax2, ax3) = plt.subplots(3, 1, constrained_layout=True, sharey=True)
ax1.plot(x_lumio[:, 0], x_lumio[:, 1], color='orange')
ax1.plot(x_moon[:, 0], x_moon[:, 1], color='grey')
ax1.plot(x_llosat[:, 0], x_llosat[:, 1], color='red')
ax1.plot(0, 0, marker='o', markersize=10, color='blue')
ax1.plot(x_lumio[0, 0], x_lumio[0, 1], marker='o', markersize=3, color='orange')
ax1.plot(x_moon[0, 0], x_moon[0, 1],marker='o', markersize=3, color='grey')
ax1.plot(x_llosat[0, 0], x_llosat[0, 1], marker='o', markersize=3, color='red')
ax1.set_title('Earth-centered trajectory in xy-plane', fontsize=18, style='oblique')
ax1.set_xlabel('x-direction [km]', fontsize=12)
ax1.set_ylabel('y-direction [km]', fontsize=12)
ax2.plot(x_lumio[:, 0], x_lumio[:, 2], color='orange')
ax2.plot(x_moon[:, 0], x_moon[:, 2], color='grey')
ax2.plot(x_llosat[:, 0], x_llosat[:, 2], color='red')
ax2.plot(0, 0, marker='o', markersize=10, color='blue')
ax2.plot(x_lumio[0, 0], x_lumio[0, 2], marker='o', markersize=3, color='orange')
ax2.plot(x_moon[0, 0], x_moon[0, 2],marker='o', markersize=3, color='grey')
ax2.plot(x_llosat[0, 0], x_llosat[0, 2], marker='o', markersize=3, color='red')
ax2.set_title('Earth-centered trajectory in xz-plane', fontsize=18, style='oblique')
ax2.set_xlabel('x-direction [km]', fontsize=12)
ax2.set_ylabel('z-direction [km]', fontsize=12)
ax3.plot(x_lumio[:, 1], x_lumio[:, 2], color='orange')
ax3.plot(x_moon[:, 1], x_moon[:, 2], color='grey')
ax3.plot(x_llosat[:, 1], x_llosat[:, 2], color='red')
ax3.plot(0, 0, marker='o', markersize=10, color='blue')
ax3.plot(x_lumio[0, 1], x_lumio[0, 2], marker='o', markersize=3, color='orange')
ax3.plot(x_moon[0, 1], x_moon[0, 2],marker='o', markersize=3, color='grey')
ax3.plot(x_llosat[0, 1], x_llosat[0, 2], marker='o', markersize=3, color='red')
ax3.set_title('Earth-centered trajectory in yz-plane', fontsize=18, style='oblique')
ax3.set_xlabel('y-direction [km]', fontsize=12)
ax3.set_ylabel('z-direction [km]', fontsize=12)
ax2.legend(['EML2-O trajectory', 'Moon trajectory', 'ELO trajectory', 'Earth'], loc='upper left', bbox_to_anchor=(1, 1))
ax1.grid(True, which="both", ls="--")
ax2.grid(True, which="both", ls="--")
ax3.grid(True, which="both", ls="--")



plt.figure()
plt.title("Breakdown of the accelerations acting on EML2-O", fontsize=20, style='oblique')
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
plt.xlabel('Time [day]', fontsize=15)
plt.ylabel('Acceleration [m/$s^{2}$]', fontsize=15)
plt.legend(['SRP', 'PM Earth', 'PM Moon', 'PM Sun', 'PM Mercury', 'PM Venus',
            'PM Mars', 'PM Jupiter', 'PM Saturn', 'PM Uranus', 'PM Neptune']
           , loc='upper left', bbox_to_anchor=(1, 1))
plt.figure()
#plt.plot(time, np.linalg.norm(output[:, 14:17], axis=1))
plt.title("Breakdown of the accelerations acting on ELO", fontsize=20, style='oblique')
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
plt.xlabel('Time [day]', fontsize=15)
plt.ylabel('Acceleration [m/$s^{2}$]', fontsize=15)
plt.legend(['SRP', 'PM Earth', 'SH Moon', 'PM Sun', 'PM Mercury', 'PM Venus',
            'PM Mars', 'PM Jupiter', 'PM Saturn', 'PM Uranus', 'PM Neptune']
           , loc='upper left', bbox_to_anchor=(1, 1))

fig2, (ax1, ax2) = plt.subplots(2, 1, constrained_layout=True, sharey=True)
ax1.set_title("Breakdown of the accelerations acting on EML2-O", fontsize=20, style='oblique')
ax1.plot(time, output[:, 3])
ax1.plot(time, output[:, 4])
ax1.plot(time, output[:, 5])
ax1.plot(time, output[:, 6])
ax1.plot(time, output[:, 7])
ax1.plot(time, output[:, 8])
ax1.plot(time, output[:, 9])
ax1.plot(time, output[:, 10])
ax1.plot(time, output[:, 11])
ax1.plot(time, output[:, 12])
ax1.plot(time, output[:, 13])
ax1.set_yscale("log")
ax1.grid(True, which="both", ls="--")
ax1.set_ylim(10**-16, 10**0)
ax1.set_xlim(0,10)
ax1.set_xlabel('Time [day]', fontsize=15)
ax1.set_ylabel('Acceleration [m/$s^{2}$]', fontsize=15)
ax1.legend(['SRP', 'PM Earth', 'PM Moon', 'PM Sun', 'PM Mercury', 'PM Venus',
            'PM Mars', 'PM Jupiter', 'PM Saturn', 'PM Uranus', 'PM Neptune']
           , loc='upper left', bbox_to_anchor=(1, 1))
ax2.set_title("Breakdown of the accelerations acting on ELO", fontsize=20, style='oblique')
ax2.plot(time, output[:, 17])
ax2.plot(time, output[:, 18])
ax2.plot(time, output[:, 19])
ax2.plot(time, output[:, 20])
ax2.plot(time, output[:, 21])
ax2.plot(time, output[:, 22])
ax2.plot(time, output[:, 23])
ax2.plot(time, output[:, 24])
ax2.plot(time, output[:, 25])
ax2.plot(time, output[:, 26])
ax2.plot(time, output[:, 27])
ax2.grid(True, which="both", ls="--")
ax2.set_yscale('log')
ax2.set_ylim(10**-16, 10**0)
ax2.set_xlim(0,10)
ax2.set_xlabel('Time [day]', fontsize=15)
ax2.set_ylabel('Acceleration [m/$s^{2}$]', fontsize=15)
ax2.legend(['SRP', 'PM Earth', 'SH Moon', 'PM Sun', 'PM Mercury', 'PM Venus',
            'PM Mars', 'PM Jupiter', 'PM Saturn', 'PM Uranus', 'PM Neptune']
           , loc='upper left', bbox_to_anchor=(1, 1))



plt.show()
