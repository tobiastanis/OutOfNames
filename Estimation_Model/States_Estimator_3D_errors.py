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

#own
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