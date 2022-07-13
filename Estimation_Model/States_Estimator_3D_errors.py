"""
                              [0 ,   1:13         13:25,     25]
est_data_n_antenna = np.array[ET, states_errors, stdP, visibility]

File names:
estimation_data_1_antenna
estimation_data_2_antenna
estimation_data_4_antenna
estimation_data_8_antenna
estimation_data_16_antenna

"""
#general
import numpy as np
import matplotlib.pyplot as plt
#own
from Initials.Simulation_Time_Setup import measurement_span_t
from Initials.Simulation_Time_Setup import DIRECTORY_NAME
from Saved_Data import Data_Loader

est_data_1_antenna = Data_Loader.json_estimation_data_reader(DIRECTORY_NAME, "estimation_data_1_antenna.json")
est_data_2_antenna = Data_Loader.json_estimation_data_reader(DIRECTORY_NAME, "estimation_data_2_antenna.json")
est_data_4_antenna = Data_Loader.json_estimation_data_reader(DIRECTORY_NAME, "estimation_data_4_antenna.json")
est_data_8_antenna = Data_Loader.json_estimation_data_reader(DIRECTORY_NAME, "estimation_data_8_antenna.json")
est_data_16_antenna = Data_Loader.json_estimation_data_reader(DIRECTORY_NAME, "estimation_data_16_antenna.json")

et = est_data_1_antenna[:, 0]
visibility = est_data_1_antenna[:, 25]

'1 Antenna'
#Position errors and uncertainty
x_error_eml2o_1 = est_data_1_antenna[:, 1:7]
x_error_elo_1 = est_data_1_antenna[:, 7:13]
stdP_1 = est_data_1_antenna[:, 13:25]
stdP_1_3sigma = 3*stdP_1

#from 5 days 1440 to end 4032
stdP_1_3sigma_after_5days = stdP_1_3sigma[1440:4033, :]

pos_3D_eml2o_1 = np.linalg.norm(stdP_1_3sigma_after_5days[:, 0:3], axis=1)
pos_3D_elo_1 = np.linalg.norm(stdP_1_3sigma_after_5days[:, 6:9], axis=1)

velo_3D_eml2o_1 = np.linalg.norm(stdP_1_3sigma_after_5days[:, 3:6], axis=1)
velo_3D_elo_1 = np.linalg.norm(stdP_1_3sigma_after_5days[:, 9:12], axis=1)

#Average position errors between 5 and 14 days of simulation
eml2o_average_3D_pos_error_1 = sum(pos_3D_eml2o_1)/len(pos_3D_eml2o_1)
elo_average_3D_pos_error_1 = sum(pos_3D_elo_1)/len(pos_3D_elo_1)

eml2o_average_3D_velo_error_1 = sum(velo_3D_eml2o_1)/len(velo_3D_eml2o_1)
elo_average_3D_velo_error_1 = sum(velo_3D_elo_1)/len(velo_3D_elo_1)

'2 Antenna'
x_error_eml2o_2 = est_data_2_antenna[:, 1:7]
x_error_elo_2 = est_data_2_antenna[:, 7:13]
stdP_2 = est_data_2_antenna[:, 13:25]
stdP_2_3sigma = 3*stdP_2

#from 5 days 1440 to end 4032
stdP_2_3sigma_after_5days = stdP_2_3sigma[1440:4033, :]

pos_3D_eml2o_2 = np.linalg.norm(stdP_2_3sigma_after_5days[:, 0:3], axis=1)
pos_3D_elo_2 = np.linalg.norm(stdP_2_3sigma_after_5days[:, 6:9], axis=1)

velo_3D_eml2o_2 = np.linalg.norm(stdP_2_3sigma_after_5days[:, 3:6], axis=1)
velo_3D_elo_2 = np.linalg.norm(stdP_2_3sigma_after_5days[:, 9:12], axis=1)

#Average position errors between 5 and 14 days of simulation
eml2o_average_3D_pos_error_2 = sum(pos_3D_eml2o_2)/len(pos_3D_eml2o_2)
elo_average_3D_pos_error_2 = sum(pos_3D_elo_2)/len(pos_3D_elo_2)

eml2o_average_3D_velo_error_2 = sum(velo_3D_eml2o_2)/len(velo_3D_eml2o_2)
elo_average_3D_velo_error_2 = sum(velo_3D_elo_2)/len(velo_3D_elo_2)

# 4 Antenna
x_error_eml2o_4 = est_data_4_antenna[:, 1:7]
x_error_elo_4 = est_data_4_antenna[:, 7:13]
stdP_4 = est_data_4_antenna[:, 13:25]
stdP_4_3sigma = 3*stdP_4

#from 5 days 1440 to end 4032
stdP_4_3sigma_after_5days = stdP_4_3sigma[1440:4033, :]

pos_3D_eml2o_4 = np.linalg.norm(stdP_4_3sigma_after_5days[:, 0:3], axis=1)
pos_3D_elo_4 = np.linalg.norm(stdP_4_3sigma_after_5days[:, 6:9], axis=1)

velo_3D_eml2o_4 = np.linalg.norm(stdP_4_3sigma_after_5days[:, 3:6], axis=1)
velo_3D_elo_4 = np.linalg.norm(stdP_4_3sigma_after_5days[:, 9:12], axis=1)

#Average position errors between 5 and 14 days of simulation
eml2o_average_3D_pos_error_4 = sum(pos_3D_eml2o_4)/len(pos_3D_eml2o_4)
elo_average_3D_pos_error_4 = sum(pos_3D_elo_4)/len(pos_3D_elo_4)

eml2o_average_3D_velo_error_4 = sum(velo_3D_eml2o_4)/len(velo_3D_eml2o_4)
elo_average_3D_velo_error_4 = sum(velo_3D_elo_4)/len(velo_3D_elo_4)


# 8 Antenna
x_error_eml2o_8 = est_data_8_antenna[:, 1:7]
x_error_elo_8 = est_data_8_antenna[:, 7:13]
stdP_8 = est_data_8_antenna[:, 13:25]
stdP_8_3sigma = 3*stdP_8

#from 5 days 1440 to end 4032
stdP_8_3sigma_after_5days = stdP_8_3sigma[1440:4033, :]

pos_3D_eml2o_8 = np.linalg.norm(stdP_8_3sigma_after_5days[:, 0:3], axis=1)
pos_3D_elo_8 = np.linalg.norm(stdP_8_3sigma_after_5days[:, 6:9], axis=1)

velo_3D_eml2o_8 = np.linalg.norm(stdP_8_3sigma_after_5days[:, 3:6], axis=1)
velo_3D_elo_8 = np.linalg.norm(stdP_8_3sigma_after_5days[:, 9:12], axis=1)

#Average position errors between 5 and 14 days of simulation
eml2o_average_3D_pos_error_8 = sum(pos_3D_eml2o_8)/len(pos_3D_eml2o_8)
elo_average_3D_pos_error_8 = sum(pos_3D_elo_8)/len(pos_3D_elo_8)

eml2o_average_3D_velo_error_8 = sum(velo_3D_eml2o_8)/len(velo_3D_eml2o_8)
elo_average_3D_velo_error_8 = sum(velo_3D_elo_8)/len(velo_3D_elo_8)

# 16 Antenna
x_error_eml2o_16 = est_data_16_antenna[:, 1:7]
x_error_elo_16 = est_data_16_antenna[:, 7:13]
stdP_16 = est_data_16_antenna[:, 13:25]
stdP_16_3sigma = 3*stdP_16

#from 5 days 1440 to end 4032
stdP_16_3sigma_after_5days = stdP_16_3sigma[1440:4033, :]

pos_3D_eml2o_16 = np.linalg.norm(stdP_16_3sigma_after_5days[:, 0:3], axis=1)
pos_3D_elo_16 = np.linalg.norm(stdP_16_3sigma_after_5days[:, 6:9], axis=1)

velo_3D_eml2o_16 = np.linalg.norm(stdP_16_3sigma_after_5days[:, 3:6], axis=1)
velo_3D_elo_16 = np.linalg.norm(stdP_16_3sigma_after_5days[:, 9:12], axis=1)

#Average position errors between 5 and 14 days of simulation
eml2o_average_3D_pos_error_16 = sum(pos_3D_eml2o_16)/len(pos_3D_eml2o_16)
elo_average_3D_pos_error_16 = sum(pos_3D_elo_16)/len(pos_3D_elo_16)

eml2o_average_3D_velo_error_16 = sum(velo_3D_eml2o_16)/len(velo_3D_eml2o_16)
elo_average_3D_velo_error_16 = sum(velo_3D_elo_16)/len(velo_3D_elo_16)


print('Average 3D-position and velocity errors of EML2O and ELO per different antenna configuration')
print("Position error EML2O (1 antenna):", eml2o_average_3D_pos_error_1, 'm')
print("Velocity error EML2O (1 antenna):", eml2o_average_3D_velo_error_1, 'm')
print("Position error ELO (1 antenna):", elo_average_3D_pos_error_1, 'm')
print("Velocity error ELO (1 antenna):", elo_average_3D_velo_error_1, 'm')

print("Position error EML2O (2 antenna):", eml2o_average_3D_pos_error_2, 'm')
print("Velocity error EML2O (2 antenna):", eml2o_average_3D_velo_error_2, 'm')
print("Position error ELO (2 antenna):", elo_average_3D_pos_error_2, 'm')
print("Velocity error ELO (2 antenna):", elo_average_3D_velo_error_2, 'm')

print("Position error EML2O (4 antenna):", eml2o_average_3D_pos_error_4, 'm')
print("Velocity error EML2O (4 antenna):", eml2o_average_3D_velo_error_4, 'm')
print("Position error ELO (4 antenna):", elo_average_3D_pos_error_4, 'm')
print("Velocity error ELO (4 antenna):", elo_average_3D_velo_error_4, 'm')

print("Position error EML2O (8 antenna):", eml2o_average_3D_pos_error_8, 'm')
print("Velocity error EML2O (8 antenna):", eml2o_average_3D_velo_error_8, 'm')
print("Position error ELO (8 antenna):", elo_average_3D_pos_error_8, 'm')
print("Velocity error ELO (8 antenna):", elo_average_3D_velo_error_8, 'm')

print("Position error EML2O (16 antenna):", eml2o_average_3D_pos_error_16, 'm')
print("Velocity error EML2O (16 antenna):", eml2o_average_3D_velo_error_16, 'm')
print("Position error ELO (16 antenna):", elo_average_3D_pos_error_16, 'm')
print("Velocity error ELO (16 antenna):", elo_average_3D_velo_error_16, 'm')

########################################################################################################################
"""Simulation figures"""
########################################################################################################################
t = measurement_span_t
#ranging_errors_array = np.array([385.57269806470686, 96.622056952627, 24.212870715731942, 6.067590846096244, 1.5204995354685686])

'State element errors per configuration'
#1 Antenna
fig1, (ax1, ax2) = plt.subplots(2, 1, constrained_layout=True, sharey=False)
ax1.plot(t, x_error_eml2o_1[:, 0], color='red', label='x')
ax1.plot(t, x_error_eml2o_1[:, 1], color='blue', label='y')
ax1.plot(t, x_error_eml2o_1[:, 2], color='green', label='z')
ax1.plot(t, stdP_1_3sigma[:, 0], color='red', linestyle='-.', label='3$\sigma_{x}$')
ax1.plot(t, stdP_1_3sigma[:, 1], color='blue', linestyle='-.', label='3$\sigma_{y}$')
ax1.plot(t, stdP_1_3sigma[:, 2], color='green', linestyle='-.', label='3$\sigma_{z}$')
ax1.legend(loc='upper left')
ax1.plot(t, -stdP_1_3sigma[:, 0], color='red', linestyle='-.')
ax1.plot(t, -stdP_1_3sigma[:, 1], color='blue', linestyle='-.')
ax1.plot(t, -stdP_1_3sigma[:, 2], color='green', linestyle='-.')
ax1.set_xlabel('Time [days]', size=14)
ax1.set_ylabel('Position error [m]', size=14)
ax1.set_title('Position error EML2O with 1 antenna ($\sigma$ = 385.6 m)', size=20)
ax1.set_xlim(0, 14)
ax1.set_ylim(-5000, 5000)
ax1.grid(True, which="both")
ax2.plot(t, x_error_eml2o_1[:, 3], color='red', label='$\dot{x}$')
ax2.plot(t, x_error_eml2o_1[:, 4], color='blue', label='$\dot{y}$')
ax2.plot(t, x_error_eml2o_1[:, 5], color='green', label='$\dot{z}$')
ax2.plot(t, stdP_1_3sigma[:, 3], color='red', linestyle='-.', label='3$\sigma_{\dot{x}}$')
ax2.plot(t, stdP_1_3sigma[:, 4], color='blue', linestyle='-.', label='3$\sigma_{\dot{y}}$')
ax2.plot(t, stdP_1_3sigma[:, 5], color='green', linestyle='-.', label='3$\sigma_{\dot{z}}$')
ax2.legend(loc='upper left')
ax2.plot(t, -stdP_1_3sigma[:, 3], color='red', linestyle='-.')
ax2.plot(t, -stdP_1_3sigma[:, 4], color='blue', linestyle='-.')
ax2.plot(t, -stdP_1_3sigma[:, 5], color='green', linestyle='-.')
ax2.set_xlabel('Time [days]', size=14)
ax2.set_ylabel('Velocity error [m/s]', size=14)
ax2.set_title('Velocity error EML2O with 1 antenna ($\sigma$ = 385.6 m)', size=20)
ax2.set_xlim(0, 14)
ax2.set_ylim(-0.02, 0.02)
ax2.grid(True, which="both")


#2 Antennas
fig2, (ax1, ax2) = plt.subplots(2, 1, constrained_layout=True, sharey=False)
ax1.plot(t, x_error_eml2o_2[:, 0], color='red', label='x')
ax1.plot(t, x_error_eml2o_2[:, 1], color='blue', label='y')
ax1.plot(t, x_error_eml2o_2[:, 2], color='green', label='z')
ax1.plot(t, stdP_2_3sigma[:, 0], color='red', linestyle='-.', label='3$\sigma_{x}$')
ax1.plot(t, stdP_2_3sigma[:, 1], color='blue', linestyle='-.', label='3$\sigma_{y}$')
ax1.plot(t, stdP_2_3sigma[:, 2], color='green', linestyle='-.', label='3$\sigma_{z}$')
ax1.legend(loc='upper left')
ax1.plot(t, -stdP_2_3sigma[:, 0], color='red', linestyle='-.')
ax1.plot(t, -stdP_2_3sigma[:, 1], color='blue', linestyle='-.')
ax1.plot(t, -stdP_2_3sigma[:, 2], color='green', linestyle='-.')
ax1.set_xlabel('Time [days]', size=14)
ax1.set_ylabel('Position error [m]', size=14)
ax1.set_title('Position error EML2O with 2 antenna ($\sigma$ = 96.6 m)', size=20)
ax1.set_xlim(0, 14)
ax1.set_ylim(-4000, 4000)
ax1.grid(True, which="both")
ax2.plot(t, x_error_eml2o_2[:, 3], color='red', label='$\dot{x}$')
ax2.plot(t, x_error_eml2o_2[:, 4], color='blue', label='$\dot{y}$')
ax2.plot(t, x_error_eml2o_2[:, 5], color='green', label='$\dot{z}$')
ax2.plot(t, stdP_2_3sigma[:, 3], color='red', linestyle='-.', label='3$\sigma_{\dot{x}}$')
ax2.plot(t, stdP_2_3sigma[:, 4], color='blue', linestyle='-.', label='3$\sigma_{\dot{y}}$')
ax2.plot(t, stdP_2_3sigma[:, 5], color='green', linestyle='-.', label='3$\sigma_{\dot{z}}$')
ax2.legend(loc='upper left')
ax2.plot(t, -stdP_2_3sigma[:, 3], color='red', linestyle='-.')
ax2.plot(t, -stdP_2_3sigma[:, 4], color='blue', linestyle='-.')
ax2.plot(t, -stdP_2_3sigma[:, 5], color='green', linestyle='-.')
ax2.set_xlabel('Time [days]', size=14)
ax2.set_ylabel('Velocity error [m/s]', size=14)
ax2.set_title('Velocity error EML2O with 2 antenna ($\sigma$ = 96.6 m)', size=20)
ax2.set_xlim(0, 14)
ax2.set_ylim(-0.01, 0.01)
ax2.grid(True, which="both")

#4 Antennas
fig3, (ax1, ax2) = plt.subplots(2, 1, constrained_layout=True, sharey=False)
ax1.plot(t, x_error_eml2o_4[:, 0], color='red', label='x')
ax1.plot(t, x_error_eml2o_4[:, 1], color='blue', label='y')
ax1.plot(t, x_error_eml2o_4[:, 2], color='green', label='z')
ax1.plot(t, stdP_4_3sigma[:, 0], color='red', linestyle='-.', label='3$\sigma_{x}$')
ax1.plot(t, stdP_4_3sigma[:, 1], color='blue', linestyle='-.', label='3$\sigma_{y}$')
ax1.plot(t, stdP_4_3sigma[:, 2], color='green', linestyle='-.', label='3$\sigma_{z}$')
ax1.legend(loc='upper left')
ax1.plot(t, -stdP_4_3sigma[:, 0], color='red', linestyle='-.')
ax1.plot(t, -stdP_4_3sigma[:, 1], color='blue', linestyle='-.')
ax1.plot(t, -stdP_4_3sigma[:, 2], color='green', linestyle='-.')
ax1.set_xlabel('Time [days]', size=14)
ax1.set_ylabel('Position error [m]', size=14)
ax1.set_title('Position error EML2O with 4 antenna ($\sigma$ = 24.2 m)', size=20)
ax1.set_xlim(0, 14)
ax1.set_ylim(-3000, 3000)
ax1.grid(True, which="both")
ax2.plot(t, x_error_eml2o_4[:, 3], color='red', label='$\dot{x}$')
ax2.plot(t, x_error_eml2o_4[:, 4], color='blue', label='$\dot{y}$')
ax2.plot(t, x_error_eml2o_4[:, 5], color='green', label='$\dot{z}$')
ax2.plot(t, stdP_4_3sigma[:, 3], color='red', linestyle='-.', label='3$\sigma_{\dot{x}}$')
ax2.plot(t, stdP_4_3sigma[:, 4], color='blue', linestyle='-.', label='3$\sigma_{\dot{y}}$')
ax2.plot(t, stdP_4_3sigma[:, 5], color='green', linestyle='-.', label='3$\sigma_{\dot{z}}$')
ax2.legend(loc='upper left')
ax2.plot(t, -stdP_4_3sigma[:, 3], color='red', linestyle='-.')
ax2.plot(t, -stdP_4_3sigma[:, 4], color='blue', linestyle='-.')
ax2.plot(t, -stdP_4_3sigma[:, 5], color='green', linestyle='-.')
ax2.set_xlabel('Time [days]', size=14)
ax2.set_ylabel('Velocity error [m/s]', size=14)
ax2.set_title('Velocity error EML2O with 4 antenna ($\sigma$ = 24.2 m)', size=20)
ax2.set_xlim(0, 14)
ax2.set_ylim(-0.008, 0.008)
ax2.grid(True, which="both")

#8 antennas
#2 Antennas
fig4, (ax1, ax2) = plt.subplots(2, 1, constrained_layout=True, sharey=False)
ax1.plot(t, x_error_eml2o_8[:, 0], color='red', label='x')
ax1.plot(t, x_error_eml2o_8[:, 1], color='blue', label='y')
ax1.plot(t, x_error_eml2o_8[:, 2], color='green', label='z')
ax1.plot(t, stdP_8_3sigma[:, 0], color='red', linestyle='-.', label='3$\sigma_{x}$')
ax1.plot(t, stdP_8_3sigma[:, 1], color='blue', linestyle='-.', label='3$\sigma_{y}$')
ax1.plot(t, stdP_8_3sigma[:, 2], color='green', linestyle='-.', label='3$\sigma_{z}$')
ax1.legend(loc='upper left')
ax1.plot(t, -stdP_8_3sigma[:, 0], color='red', linestyle='-.')
ax1.plot(t, -stdP_8_3sigma[:, 1], color='blue', linestyle='-.')
ax1.plot(t, -stdP_8_3sigma[:, 2], color='green', linestyle='-.')
ax1.set_xlabel('Time [days]', size=14)
ax1.set_ylabel('Position error [m]', size=14)
ax1.set_title('Position error EML2O with 8 antenna ($\sigma$ = 6.07 m)', size=20)
ax1.set_xlim(0, 14)
ax1.set_ylim(-1500, 1500)
ax1.grid(True, which="both")
ax2.plot(t, x_error_eml2o_8[:, 3], color='red', label='$\dot{x}$')
ax2.plot(t, x_error_eml2o_8[:, 4], color='blue', label='$\dot{y}$')
ax2.plot(t, x_error_eml2o_8[:, 5], color='green', label='$\dot{z}$')
ax2.plot(t, stdP_8_3sigma[:, 3], color='red', linestyle='-.', label='3$\sigma_{\dot{x}}$')
ax2.plot(t, stdP_8_3sigma[:, 4], color='blue', linestyle='-.', label='3$\sigma_{\dot{y}}$')
ax2.plot(t, stdP_8_3sigma[:, 5], color='green', linestyle='-.', label='3$\sigma_{\dot{z}}$')
ax2.legend(loc='upper left')
ax2.plot(t, -stdP_8_3sigma[:, 3], color='red', linestyle='-.')
ax2.plot(t, -stdP_8_3sigma[:, 4], color='blue', linestyle='-.')
ax2.plot(t, -stdP_8_3sigma[:, 5], color='green', linestyle='-.')
ax2.set_xlabel('Time [days]', size=14)
ax2.set_ylabel('Velocity error [m/s]', size=14)
ax2.set_title('Velocity error EML2O with 8 antenna ($\sigma$ = 6.07 m)', size=20)
ax2.set_xlim(0, 14)
ax2.set_ylim(-0.006, 0.006)
ax2.grid(True, which="both")

#16 Antennas
fig5, (ax1, ax2) = plt.subplots(2, 1, constrained_layout=True, sharey=False)
ax1.plot(t, x_error_eml2o_16[:, 0], color='red', label='x')
ax1.plot(t, x_error_eml2o_16[:, 1], color='blue', label='y')
ax1.plot(t, x_error_eml2o_16[:, 2], color='green', label='z')
ax1.plot(t, stdP_16_3sigma[:, 0], color='red', linestyle='-.', label='3$\sigma_{x}$')
ax1.plot(t, stdP_16_3sigma[:, 1], color='blue', linestyle='-.', label='3$\sigma_{y}$')
ax1.plot(t, stdP_16_3sigma[:, 2], color='green', linestyle='-.', label='3$\sigma_{z}$')
ax1.legend(loc='upper left')
ax1.plot(t, -stdP_16_3sigma[:, 0], color='red', linestyle='-.')
ax1.plot(t, -stdP_16_3sigma[:, 1], color='blue', linestyle='-.')
ax1.plot(t, -stdP_16_3sigma[:, 2], color='green', linestyle='-.')
ax1.set_xlabel('Time [days]', size=14)
ax1.set_ylabel('Position error [m]', size=14)
ax1.set_title('Position error EML2O with 16 antenna ($\sigma$ = 1.52 m)', size=20)
ax1.set_xlim(0, 14)
ax1.set_ylim(-200, 200)
ax1.grid(True, which="both")
ax2.plot(t, x_error_eml2o_16[:, 3], color='red', label='$\dot{x}$')
ax2.plot(t, x_error_eml2o_16[:, 4], color='blue', label='$\dot{y}$')
ax2.plot(t, x_error_eml2o_16[:, 5], color='green', label='$\dot{z}$')
ax2.plot(t, stdP_16_3sigma[:, 3], color='red', linestyle='-.', label='3$\sigma_{\dot{x}}$')
ax2.plot(t, stdP_16_3sigma[:, 4], color='blue', linestyle='-.', label='3$\sigma_{\dot{y}}$')
ax2.plot(t, stdP_16_3sigma[:, 5], color='green', linestyle='-.', label='3$\sigma_{\dot{z}}$')
ax2.legend(loc='upper left')
ax2.plot(t, -stdP_16_3sigma[:, 3], color='red', linestyle='-.')
ax2.plot(t, -stdP_16_3sigma[:, 4], color='blue', linestyle='-.')
ax2.plot(t, -stdP_16_3sigma[:, 5], color='green', linestyle='-.')
ax2.set_xlabel('Time [days]', size=14)
ax2.set_ylabel('Velocity error [m/s]', size=14)
ax2.set_title('Velocity error EML2O with 16 antenna ($\sigma$ = 1.52 m)', size=20)
ax2.set_xlim(0, 14)
ax2.set_ylim(-0.002, 0.002)
ax2.grid(True, which="both")

"""ELO plot"""
#1 Antenna
fig6, (ax1, ax2) = plt.subplots(2, 1, constrained_layout=True, sharey=False)
ax1.plot(t, x_error_elo_1[:, 0], color='red', label='x')
ax1.plot(t, x_error_elo_1[:, 1], color='blue', label='y')
ax1.plot(t, x_error_elo_1[:, 2], color='green', label='z')
ax1.plot(t, stdP_1_3sigma[:, 6], color='red', linestyle='-.', label='3$\sigma_{x}$')
ax1.plot(t, stdP_1_3sigma[:, 7], color='blue', linestyle='-.', label='3$\sigma_{y}$')
ax1.plot(t, stdP_1_3sigma[:, 8], color='green', linestyle='-.', label='3$\sigma_{z}$')
ax1.legend(loc='upper left')
ax1.plot(t, -stdP_1_3sigma[:, 6], color='red', linestyle='-.')
ax1.plot(t, -stdP_1_3sigma[:, 7], color='blue', linestyle='-.')
ax1.plot(t, -stdP_1_3sigma[:, 8], color='green', linestyle='-.')
ax1.set_xlabel('Time [days]', size=14)
ax1.set_ylabel('Position error [m]', size=14)
ax1.set_title('Position error ELO with 1 antenna ($\sigma$ = 385.6 m)', size=20)
ax1.set_xlim(0, 14)
ax1.set_ylim(-75000, 75000)
ax1.grid(True, which="both")
ax2.plot(t, x_error_elo_1[:, 3], color='red', label='$\dot{x}$')
ax2.plot(t, x_error_elo_1[:, 4], color='blue', label='$\dot{y}$')
ax2.plot(t, x_error_elo_1[:, 5], color='green', label='$\dot{z}$')
ax2.plot(t, stdP_1_3sigma[:, 9], color='red', linestyle='-.', label='3$\sigma_{\dot{x}}$')
ax2.plot(t, stdP_1_3sigma[:, 10], color='blue', linestyle='-.', label='3$\sigma_{\dot{y}}$')
ax2.plot(t, stdP_1_3sigma[:, 11], color='green', linestyle='-.', label='3$\sigma_{\dot{z}}$')
ax2.legend(loc='upper left')
ax2.plot(t, -stdP_1_3sigma[:, 9], color='red', linestyle='-.')
ax2.plot(t, -stdP_1_3sigma[:, 10], color='blue', linestyle='-.')
ax2.plot(t, -stdP_1_3sigma[:, 11], color='green', linestyle='-.')
ax2.set_xlabel('Time [days]', size=14)
ax2.set_ylabel('Velocity error [m/s]', size=14)
ax2.set_title('Velocity error ELO with 1 antenna ($\sigma$ = 385.6 m)', size=20)
ax2.set_xlim(0, 14)
ax2.set_ylim(-25, 25)
ax2.grid(True, which="both")

#2 Antennas
fig7, (ax1, ax2) = plt.subplots(2, 1, constrained_layout=True, sharey=False)
ax1.plot(t, x_error_elo_2[:, 0], color='red', label='x')
ax1.plot(t, x_error_elo_2[:, 1], color='blue', label='y')
ax1.plot(t, x_error_elo_2[:, 2], color='green', label='z')
ax1.plot(t, stdP_2_3sigma[:, 6], color='red', linestyle='-.', label='3$\sigma_{x}$')
ax1.plot(t, stdP_2_3sigma[:, 7], color='blue', linestyle='-.', label='3$\sigma_{y}$')
ax1.plot(t, stdP_2_3sigma[:, 8], color='green', linestyle='-.', label='3$\sigma_{z}$')
ax1.legend(loc='upper left')
ax1.plot(t, -stdP_2_3sigma[:, 6], color='red', linestyle='-.')
ax1.plot(t, -stdP_2_3sigma[:, 7], color='blue', linestyle='-.')
ax1.plot(t, -stdP_2_3sigma[:, 8], color='green', linestyle='-.')
ax1.set_xlabel('Time [days]', size=14)
ax1.set_ylabel('Position error [m]', size=14)
ax1.set_title('Position error EML2O with 2 antenna ($\sigma$ = 96.6 m)', size=20)
ax1.set_xlim(0, 14)
ax1.set_ylim(-30000, 30000)
ax1.grid(True, which="both")
ax2.plot(t, x_error_elo_2[:, 3], color='red', label='$\dot{x}$')
ax2.plot(t, x_error_elo_2[:, 4], color='blue', label='$\dot{y}$')
ax2.plot(t, x_error_elo_2[:, 5], color='green', label='$\dot{z}$')
ax2.plot(t, stdP_2_3sigma[:, 9], color='red', linestyle='-.', label='3$\sigma_{\dot{x}}$')
ax2.plot(t, stdP_2_3sigma[:, 10], color='blue', linestyle='-.', label='3$\sigma_{\dot{y}}$')
ax2.plot(t, stdP_2_3sigma[:, 11], color='green', linestyle='-.', label='3$\sigma_{\dot{z}}$')
ax2.legend(loc='upper left')
ax2.plot(t, -stdP_2_3sigma[:, 9], color='red', linestyle='-.')
ax2.plot(t, -stdP_2_3sigma[:, 10], color='blue', linestyle='-.')
ax2.plot(t, -stdP_2_3sigma[:, 11], color='green', linestyle='-.')
ax2.set_xlabel('Time [days]', size=14)
ax2.set_ylabel('Velocity error [m/s]', size=14)
ax2.set_title('Velocity error EML2O with 2 antenna ($\sigma$ = 96.6 m)', size=20)
ax2.set_xlim(0, 14)
ax2.set_ylim(-6, 6)
ax2.grid(True, which="both")

#4 Antennas
fig8, (ax1, ax2) = plt.subplots(2, 1, constrained_layout=True, sharey=False)
ax1.plot(t, x_error_elo_4[:, 0], color='red', label='x')
ax1.plot(t, x_error_elo_4[:, 1], color='blue', label='y')
ax1.plot(t, x_error_elo_4[:, 2], color='green', label='z')
ax1.plot(t, stdP_4_3sigma[:, 6], color='red', linestyle='-.', label='3$\sigma_{x}$')
ax1.plot(t, stdP_4_3sigma[:, 7], color='blue', linestyle='-.', label='3$\sigma_{y}$')
ax1.plot(t, stdP_4_3sigma[:, 8], color='green', linestyle='-.', label='3$\sigma_{z}$')
ax1.legend(loc='upper left')
ax1.plot(t, -stdP_4_3sigma[:, 6], color='red', linestyle='-.')
ax1.plot(t, -stdP_4_3sigma[:, 7], color='blue', linestyle='-.')
ax1.plot(t, -stdP_4_3sigma[:, 8], color='green', linestyle='-.')
ax1.set_xlabel('Time [days]', size=14)
ax1.set_ylabel('Position error [m]', size=14)
ax1.set_title('Position error ELO with 4 antenna ($\sigma$ = 24.2 m)', size=20)
ax1.set_xlim(0, 14)
ax1.set_ylim(-4000, 4000)
ax1.grid(True, which="both")
ax2.plot(t, x_error_elo_4[:, 3], color='red', label='$\dot{x}$')
ax2.plot(t, x_error_elo_4[:, 4], color='blue', label='$\dot{y}$')
ax2.plot(t, x_error_elo_4[:, 5], color='green', label='$\dot{z}$')
ax2.plot(t, stdP_4_3sigma[:, 9], color='red', linestyle='-.', label='3$\sigma_{\dot{x}}$')
ax2.plot(t, stdP_4_3sigma[:, 10], color='blue', linestyle='-.', label='3$\sigma_{\dot{y}}$')
ax2.plot(t, stdP_4_3sigma[:, 11], color='green', linestyle='-.', label='3$\sigma_{\dot{z}}$')
ax2.legend(loc='upper left')
ax2.plot(t, -stdP_4_3sigma[:, 9], color='red', linestyle='-.')
ax2.plot(t, -stdP_4_3sigma[:, 10], color='blue', linestyle='-.')
ax2.plot(t, -stdP_4_3sigma[:, 11], color='green', linestyle='-.')
ax2.set_xlabel('Time [days]', size=14)
ax2.set_ylabel('Velocity error [m/s]', size=14)
ax2.set_title('Velocity error ELO with 4 antenna ($\sigma$ = 24.2 m)', size=20)
ax2.set_xlim(0, 14)
ax2.set_ylim(-0.8, 0.8)
ax2.grid(True, which="both")

#8 Antennas
fig9, (ax1, ax2) = plt.subplots(2, 1, constrained_layout=True, sharey=False)
ax1.plot(t, x_error_elo_8[:, 0], color='red', label='x')
ax1.plot(t, x_error_elo_8[:, 1], color='blue', label='y')
ax1.plot(t, x_error_elo_8[:, 2], color='green', label='z')
ax1.plot(t, stdP_8_3sigma[:, 6], color='red', linestyle='-.', label='3$\sigma_{x}$')
ax1.plot(t, stdP_8_3sigma[:, 7], color='blue', linestyle='-.', label='3$\sigma_{y}$')
ax1.plot(t, stdP_8_3sigma[:, 8], color='green', linestyle='-.', label='3$\sigma_{z}$')
ax1.legend(loc='upper left')
ax1.plot(t, -stdP_8_3sigma[:, 6], color='red', linestyle='-.')
ax1.plot(t, -stdP_8_3sigma[:, 7], color='blue', linestyle='-.')
ax1.plot(t, -stdP_8_3sigma[:, 8], color='green', linestyle='-.')
ax1.set_xlabel('Time [days]', size=14)
ax1.set_ylabel('Position error [m]', size=14)
ax1.set_title('Position error ELO with 8 antenna ($\sigma$ = 6.07 m)', size=20)
ax1.set_xlim(0, 14)
ax1.set_ylim(-2000, 2000)
ax1.grid(True, which="both")
ax2.plot(t, x_error_elo_8[:, 3], color='red', label='$\dot{x}$')
ax2.plot(t, x_error_elo_8[:, 4], color='blue', label='$\dot{y}$')
ax2.plot(t, x_error_elo_8[:, 5], color='green', label='$\dot{z}$')
ax2.plot(t, stdP_8_3sigma[:, 9], color='red', linestyle='-.', label='3$\sigma_{\dot{x}}$')
ax2.plot(t, stdP_8_3sigma[:, 10], color='blue', linestyle='-.', label='3$\sigma_{\dot{y}}$')
ax2.plot(t, stdP_8_3sigma[:, 11], color='green', linestyle='-.', label='3$\sigma_{\dot{z}}$')
ax2.legend(loc='upper left')
ax2.plot(t, -stdP_8_3sigma[:, 9], color='red', linestyle='-.')
ax2.plot(t, -stdP_8_3sigma[:, 10], color='blue', linestyle='-.')
ax2.plot(t, -stdP_8_3sigma[:, 11], color='green', linestyle='-.')
ax2.set_xlabel('Time [days]', size=14)
ax2.set_ylabel('Velocity error [m/s]', size=14)
ax2.set_title('Velocity error ELO with 8 antenna ($\sigma$ = 6.07 m)', size=20)
ax2.set_xlim(0, 14)
ax2.set_ylim(-0.4, 0.4)
ax2.grid(True, which="both")

#16 Antennas
fig10, (ax1, ax2) = plt.subplots(2, 1, constrained_layout=True, sharey=False)
ax1.plot(t, x_error_elo_16[:, 0], color='red', label='x')
ax1.plot(t, x_error_elo_16[:, 1], color='blue', label='y')
ax1.plot(t, x_error_elo_16[:, 2], color='green', label='z')
ax1.plot(t, stdP_16_3sigma[:, 6], color='red', linestyle='-.', label='3$\sigma_{x}$')
ax1.plot(t, stdP_16_3sigma[:, 7], color='blue', linestyle='-.', label='3$\sigma_{y}$')
ax1.plot(t, stdP_16_3sigma[:, 8], color='green', linestyle='-.', label='3$\sigma_{z}$')
ax1.legend(loc='upper left')
ax1.plot(t, -stdP_16_3sigma[:, 6], color='red', linestyle='-.')
ax1.plot(t, -stdP_16_3sigma[:, 7], color='blue', linestyle='-.')
ax1.plot(t, -stdP_16_3sigma[:, 8], color='green', linestyle='-.')
ax1.set_xlabel('Time [days]', size=14)
ax1.set_ylabel('Position error [m]', size=14)
ax1.set_title('Position error ELO with 16 antenna ($\sigma$ = 1.52 m)', size=20)
ax1.set_xlim(0, 14)
ax1.set_ylim(-1000, 1000)
ax1.grid(True, which="both")
ax2.plot(t, x_error_elo_16[:, 3], color='red', label='$\dot{x}$')
ax2.plot(t, x_error_elo_16[:, 4], color='blue', label='$\dot{y}$')
ax2.plot(t, x_error_elo_16[:, 5], color='green', label='$\dot{z}$')
ax2.plot(t, stdP_16_3sigma[:, 9], color='red', linestyle='-.', label='3$\sigma_{\dot{x}}$')
ax2.plot(t, stdP_16_3sigma[:, 10], color='blue', linestyle='-.', label='3$\sigma_{\dot{y}}$')
ax2.plot(t, stdP_16_3sigma[:, 11], color='green', linestyle='-.', label='3$\sigma_{\dot{z}}$')
ax2.legend(loc='upper left')
ax2.plot(t, -stdP_16_3sigma[:, 9], color='red', linestyle='-.')
ax2.plot(t, -stdP_16_3sigma[:, 10], color='blue', linestyle='-.')
ax2.plot(t, -stdP_16_3sigma[:, 11], color='green', linestyle='-.')
ax2.set_xlabel('Time [days]', size=14)
ax2.set_ylabel('Velocity error [m/s]', size=14)
ax2.set_title('Velocity error ELO with 16 antenna ($\sigma$ = 1.52 m)', size=20)
ax2.set_xlim(0, 14)
ax2.set_ylim(-0.15, 0.15)
ax2.grid(True, which="both")


plt.show()
