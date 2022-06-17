"""
Initial parameters of the Radio System
"""
#general
import numpy as np
#own
from Initials.Simulation_Time_Setup import DIRECTORY_NAME
from Saved_Data import Data_Loader
#tudatpy
from tudatpy.kernel import constants

###constants###
b = constants.BOLTZMANN_CONSTANT
c = constants.SPEED_OF_LIGHT
pi = np.pi

###states###
states = Data_Loader.json_measurementarray_reader(DIRECTORY_NAME)
d = np.subtract(states[:, 0:3], states[:, 6:9])
d_abs = np.linalg.norm(d, axis=1)
"dmax is used, since worst case is calculated and worst case comes with largest distance"
dmax = max(d_abs)               #Maximum operation distance [m]

########################################################################################################################
################################################ INITIAL RADIO PARAMETERS ##############################################
########################################################################################################################
#General
distance = 1.03*dmax                # Worst case distance, 3 percent extra max distance added [m]
#Downlink (EML2O)
Tx_down = 3                         #Transmission power [dBW]
frequency_down = 2200e6             #Frequency [Hz]
cablelosses_down = 1                #Losses within the system (both sides) [dB]
Req_EBNO_down = 2.5                 #Required Energy per bit to noise power spectral density ratio [dB]
polarizationloss_down = 0.5         #Polarization loss [dB]
margin_down = 3                     #Link margin [dB]
Gain_down = np.linspace(6.5, 65, 10)#Gain array [dBi]


#Uplink (ELO)
Tx_up = 3                           #Transmission power [dBW]
frequency_up = 2200e6               #Frequency [Hz]
cablelosses_up = 1                  #Losses within the system (both sides) [dB]
Req_EBNO_up= 2.5                    #Required Energy per bit to noise power spectral density ratio [dB]
polarizationloss_up = 0.5           #Polarization loss [dB]
margin_up = 3                       #Link margin [dB]
Gain_up = 23.6                      #Gain [dBi]

