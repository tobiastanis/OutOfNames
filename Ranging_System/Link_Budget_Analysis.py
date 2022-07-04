"""
Initial parameters of the Radio System

Bias for future work
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
frequency_down = 2290e6             #Frequency [Hz]         [0.5 kbps - 2 Mbps
#Bandwidth_down = 1e6                #Bandwidth [Hz]
cablelosses_down = 1                #Losses within the system (both sides) [dB]
req_EBNO_down = 2.5                 #Required Energy per bit to noise power spectral density ratio [dB]
polarizationloss_down = 0.5         #Polarization loss [dB]
margin_down = 3                     #Link margin [dB]
Gain_down = np.linspace(6.5, 18.5, 161)#Gain array [dBi]
#Gain_down = 15.5
print(Gain_down[0], Gain_down[40], Gain_down[80], Gain_down[120], Gain_down[160])
#Gain_down = 15.5
Tnoise_down = 26.9 #dB/K
#bitrate_down = 6800 #bps

#Uplink (ELO)
Tx_up = 3                           #Transmission power [dBW]
frequency_up = 2110e6               #Frequency [Hz]     bitrate [0.5 - 128 kbps]
#Bandwidth_up = 1e6                  #Bandwidth [Hz]
cablelosses_up = 1                  #Losses within the system (both sides) [dB]
req_EBNO_up= 2.5                    #Required Energy per bit to noise power spectral density ratio [dB], need to be higher than 2.5d B
polarizationloss_up = 0.5           #Polarization loss [dB]
margin_up = 3                       #Link margin [dB]
Gain_up = 23.6                      #Gain [dBi]
Tnoise_up = 26.9                    #dB/K
#bitrate_up = 8000                  #bps
########################################################################################################################
################################################ CALCULATIONS ##########################################################
########################################################################################################################
#Down from EML2O ---> ELO
wavelength_down = c / frequency_down                                    #Wavelength down [m]
freespaceloss_down = 20*np.log10(4*pi*dmax/wavelength_down)             #FreeSpace Loss down [dB]
EIRP_down = Tx_down - cablelosses_down + Gain_down                      #Effective Isotropic Radiated Power [dB]
#T_noise_down = 10**(Tx_down/10)/Bandwidth_down*1/kb

Rx_down = EIRP_down - freespaceloss_down - polarizationloss_down
GoverT_down = Gain_down - Tnoise_down           # G/T LUMIO


#Up from ELO ---> EML2O
wavelength_up = c / frequency_up
freespaceloss_up = 20*np.log10(4*pi*dmax/wavelength_up)
EIRP_up = Tx_up - cablelosses_up + Gain_up

Rx_up = EIRP_up - freespaceloss_up - polarizationloss_up
GoverT_up = Gain_up - Tnoise_up         # G/T Pathfinder

# Calculating Energy to bit Noise power spectral ratio
bitrate_down = 1/kb*10**((Rx_down+GoverT_up-5.5)/10)
bitrate_up = 1/kb*10**((Rx_up+GoverT_down-5.5)/10)

EbN0_down = Rx_down + GoverT_up - 10*np.log10(kb*bitrate_down)
EbN0_up = Rx_up + GoverT_down - 10*np.log10(kb*bitrate_up)



# Margin above required EbN0, must be above 3 dB
EbN0_margin_down = EbN0_down - req_EBNO_down
EbN0_margin_up = EbN0_up - req_EBNO_up


print('EbN0_margin_down:', EbN0_margin_down, '\n', 'EbN0_margin_up:', EbN0_margin_up)

ranging_error_per_bit_down = c / bitrate_down            #meter per bit (per measurement)
ranging_error_per_bit_up = c / bitrate_up
ranging_error_per_bit = np.sqrt(ranging_error_per_bit_down**2 + ranging_error_per_bit_up**2)
no_of_meaurements = bitrate_down
ranging_error = ranging_error_per_bit/np.sqrt(no_of_meaurements)
print('Down:', ranging_error_per_bit_down, '\n', 'Up:', ranging_error_per_bit_up, '\n', 'ranging_error_per_bit:', ranging_error_per_bit)
print('Ranging_error_conventional:', ranging_error)
integration_time_down = no_of_meaurements/bitrate_down           #transmissiontime [s]
integration_time_up = no_of_meaurements/bitrate_up


#Symbol to Noise ratio
EsN0_down = EbN0_down
EsN0_up = EbN0_up

# We are using GMSK, so EbN0 = EsN0
# Forward error correction, send to bits in order to have one bit of information, so 1 symbol is made by two bits
#
sigma_rhoTM_down = (4*c*(1/bitrate_down)**2/(pi*integration_time_down*10**((EsN0_down-margin_down)/10)))
sigma_rhoTM_up = (4*c*(1/bitrate_up)**2/(pi*integration_time_up*10**((EsN0_up-margin_up)/10)))
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

