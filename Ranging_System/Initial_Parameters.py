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
kb = constants.BOLTZMANN_CONSTANT
c = constants.SPEED_OF_LIGHT
pi = np.pi

###states###
states = Data_Loader.json_measurementarray_reader(DIRECTORY_NAME)
d = np.subtract(states[:, 0:3], states[:, 6:9])
d_abs = np.linalg.norm(d, axis=1)
"dmax is used, since worst case is calculated and worst case comes with largest distance"
dmax = max(d_abs)               #Maximum operation distance [m]
print(dmax)
########################################################################################################################
################################################ INITIAL RADIO PARAMETERS ##############################################
########################################################################################################################
"""
difference between needed and chanel bandwidth, in this case use bandwidth that you need not the channel
based on datarate and transimission power, a certain energy come in
- bandwidth equal to bitrate
"""
#General
distance = 1.00*dmax                # Worst case distance, 3 percent extra max distance added [m]
#Downlink (EML2O)
Tx_down = 3                         #Transmission power [dBW]
frequency_down = 2290e6             #Frequency [Hz]
#Bandwidth_down = 1e6                #Bandwidth [Hz]
cablelosses_down = 1                #Losses within the system (both sides) [dB]
req_EBNO_down = 2.5                 #Required Energy per bit to noise power spectral density ratio [dB]
polarizationloss_down = 0.5         #Polarization loss [dB]
margin_down = 3                     #Link margin [dB]
#Gain_down = np.linspace(6.5, 65, 10)#Gain array [dBi]
Gain_down = 6.5
Tnoise_down = 26.9 #dB/K
bitrate_down = 900 #bps

#Uplink (ELO)
Tx_up = 3                           #Transmission power [dBW]
frequency_up = 2110e6               #Frequency [Hz]
#Bandwidth_up = 1e6                  #Bandwidth [Hz]
cablelosses_up = 1                  #Losses within the system (both sides) [dB]
req_EBNO_up= 2.5                    #Required Energy per bit to noise power spectral density ratio [dB], need to be higher than 2.5d B
polarizationloss_up = 0.5           #Polarization loss [dB]
margin_up = 3                       #Link margin [dB]
Gain_up = 23.6                      #Gain [dBi]
Tnoise_up = 26.9                    #dB/K
bitrate_up = 900                  #bps
########################################################################################################################
################################################ CALCULATIONS ##########################################################
########################################################################################################################
#Down from LUMIO ---> Pathfinder
wavelength_down = c / frequency_down                                    #Wavelength down [m]
freespaceloss_down = 20*np.log10(4*pi*dmax/wavelength_down)             #FreeSpace Loss down [dB]
EIRP_down = Tx_down - cablelosses_down + Gain_down                      #Effective Isotropic Radiated Power [dB]
#T_noise_down = 10**(Tx_down/10)/Bandwidth_down*1/kb

Rx_down = EIRP_down - freespaceloss_down - polarizationloss_down
GoverT_down = Gain_down - Tnoise_down           # G/T LUMIO


#Up from PAthfinder ---> LUMIO
wavelength_up = c / frequency_up
freespaceloss_up = 20*np.log10(4*pi*dmax/wavelength_up)
EIRP_up = Tx_up - cablelosses_up + Gain_up

Rx_up = EIRP_up - freespaceloss_up - polarizationloss_up
GoverT_up = Gain_up - Tnoise_up         # G/T Pathfinder


EbN0_down = Rx_down + GoverT_up - 10*np.log10(kb*bitrate_down)

EbN0_up = Rx_up + GoverT_down - 10*np.log10(kb*bitrate_up)

EbN0_margin_down = EbN0_down - req_EBNO_down
EbN0_margin_up = EbN0_up - req_EBNO_up

print('EbN0_margin_down:', EbN0_margin_down, '\n', 'EbN0_margin_up:', EbN0_margin_up)

ranging_error_per_bit = c / bitrate_down            #meter per bit (per measurement)
no_of_meaurements = bitrate_down
ranging_error = ranging_error_per_bit/np.sqrt(no_of_meaurements)
print(ranging_error_per_bit)

integration_time_down = no_of_meaurements/bitrate_down           #transmissiontime [s]
integration_time_up = no_of_meaurements/bitrate_up
# We are using GMSK, so EbN0 = EsN0
sigma_rhoTM_down = (4*c*(1/bitrate_down)**2/(pi*integration_time_down*10**((EbN0_down-3)/10)))
sigma_rhoTM_up = (4*c*(1/bitrate_up)**2/(pi*integration_time_up*10**((EbN0_up-3)/10)))
sigma_rhoTM = np.sqrt(sigma_rhoTM_down**2 + sigma_rhoTM_up**2)


print('EbN0_down:', EbN0_down, '\n', 'EbN0_up:', EbN0_up)
print('integration_time_down:', integration_time_down, 's')
print('integration_time_up:', integration_time_up, 's')
print('down:', sigma_rhoTM_down, '\n', 'up:', sigma_rhoTM_up)
print('sigma_rhoTM:', sigma_rhoTM)


#Tsd = 1/bitrate

#Check DSN handbook for integration time
# Graph function of antenna gain vs  sigma


# Eventually compare 3sigma lines of different scenarios with each other or take average values after days 3 or 4
