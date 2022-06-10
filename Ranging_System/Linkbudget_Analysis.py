"""
Info:
VHF (130 - 170 MHz) Channelsize 25 kHz
UHF (400 - 470 MHz) Channelsize 50 kHz
S-band (2.2 - 2.5 GHz) Channelsize up to 1 MHz
X-Band (8 - 12.5 GHz) Channelsize up to 100 MHz
Ku Band (12.5 - 18 HHz) Channelsize 100 MHz (multiple channels may be combined)
K Band (18 - 26.5 GHz) Channelsize 100 MHz (multiple channels may be combined)
Ka Band (26.5 - 40 GHz) Channelsize 100 MHz (multiple channels may be combined)

VHF & UHF mainly used for TM/TC (telemetry&telecommand) low datarate, suited for small satellites
- Hard to get spectrum, need big antenna for reasonable gain
- not really suited for high performance due to low bandwidth

S-band used for TM/TC on uSats or Payload data medium datarate, high efficiency
- Most used for 'low bandwidth'
- Available for payload data
- Many components available, so cheap, high performance solutions

X-band: high cost and not small and beyond is too large

S-band probably best choice
"""

#general
import numpy as np
#own
from Initials.Simulation_Time_Setup import DIRECTORY_NAME
from Saved_Data import Data_Loader
#tudatpy
from tudatpy.kernel import constants


states = Data_Loader.json_measurementarray_reader(DIRECTORY_NAME)

d = np.subtract(states[:, 0:3], states[:, 6:9])
d_abs = np.linalg.norm(d, axis=1)

dmin = min(d_abs)               #Minimum operation distance [m]
dmax = max(d_abs)               #Maximum operation distance [m]

"""
margin = EbNo - EbNo_treshold - implementationLOSS [dB]
EbNo = SNR = 10log(bitrate) [dB]                            (Energy per bit to noise power spectral density ratio)
EbNo_treshold = e.g. 2.5 [dB]          ----ask how to determine this----
implementationLOSS = e.g. 1 [dB]       ----ask how to determine this----

SNR = Rx_signal + G/T - 1-*log(kb)                          (Signal-to-noise ratio)
Rx_signal = EIRP - attenuation - polarizationLOSS - receiverLOSS
G/T = (None for intersatellite?) [dBK]              Gain to noise temperature
kb = Boltzmann constant

EIRP = e.g. 9.0 [dBW]                  ----Check where it comes from----
attenuation = freespace             (no atmosphere)
PolarizationLOSS = e.g. 0 [dB]         ----ask how to determine this----
receiverLOSS = e.g. 2 [dB]             ----ask how to determine this----

freespace(LOSS) = 20log(4pi*d/lambda)   (Lfs)




"""


