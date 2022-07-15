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

'Obtaining the 99.7% confidence interval for each antenna configuration'
stdP_1 = est_data_1_antenna[:, 13:25]
stdP_1_3sigma = 3*stdP_1
stdP_2 = est_data_2_antenna[:, 13:25]
stdP_2_3sigma = 3*stdP_2
stdP_4 = est_data_4_antenna[:, 13:25]
stdP_4_3sigma = 3*stdP_4
stdP_8 = est_data_8_antenna[:, 13:25]
stdP_8_3sigma = 3*stdP_8
stdP_16 = est_data_16_antenna[:, 13:25]
stdP_16_3sigma = 3*stdP_16


