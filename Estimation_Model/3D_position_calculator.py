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
#Average position errors between 5 and 14 days of simulation
eml2o_average_3D_pos_error_1 = sum(pos_3D_eml2o_1)/len(pos_3D_eml2o_1)
elo_average_3D_pos_error_1 = sum(pos_3D_elo_1)/len(pos_3D_elo_1)

print("Position error EML2O (1 antenna):", eml2o_average_3D_pos_error_1, 'm')
print("Position error ELO (1 antenna):", elo_average_3D_pos_error_1, 'm')


'2 Antenna'
x_error_eml2o_2 = est_data_2_antenna[:, 1:7]
x_error_elo_2 = est_data_2_antenna[:, 7:13]
stdP_2 = est_data_2_antenna[:, 13:25]

# 4 Antenna
x_error_eml2o_4 = est_data_4_antenna[:, 1:7]
x_error_elo_4 = est_data_4_antenna[:, 7:13]
stdP_4 = est_data_4_antenna[:, 13:25]

# 8 Antenna
x_error_eml2o_8 = est_data_8_antenna[:, 1:7]
x_error_elo_8 = est_data_8_antenna[:, 7:13]
stdP_8 = est_data_8_antenna[:, 13:25]

# 16 Antenna
x_error_eml2o_16 = est_data_16_antenna[:, 1:7]
x_error_elo_16 = est_data_16_antenna[:, 7:13]
stdP_16 = est_data_16_antenna[:, 13:25]