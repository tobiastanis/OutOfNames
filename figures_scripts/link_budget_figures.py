import matplotlib.pyplot as plt
'Do tm 16 antennas!!! add physiscal dimensions to it'
import numpy as np
from Ranging_System import Link_Budget_Analysis

bitrate_down = Link_Budget_Analysis.bitrate_down
bitrate_up = Link_Budget_Analysis.bitrate_up

downlinkgain = Link_Budget_Analysis.Gain_down

sigma_tot = Link_Budget_Analysis.sigma_rhoTM

Gain = np.array([6.5, 9.5, 9.5, 12.5, 12.5, 15.5, 15.5])
ranging_error = np.array([385.57269806470686, 193.244113905254, 96.622056952627, 48.42574143146387, 24.212870715731942, 12.135181692192482, 6.067590846096244])
ranging_error_down = np.array([293.9318896119697, 147.31491062945992, 73.65745531472996, 36.91617626521393, 18.458088132606964, 9.25095812922967, 4.625479064614836])
ranging_error_up = np.array([249.5402768332889, 125.0664010246598, 62.5332005123299, 31.340841774634143, 15.670420887317075, 7.853814894289469,  3.9269074471447363])

plt.figure()
#plt.plot(Gain, ranging_error, linewidth=2 ,color='orange')
plt.plot(downlinkgain, sigma_tot, linewidth=2)
plt.plot(downlinkgain[0], sigma_tot[0], marker='o', markersize=5, color='red')
plt.plot(downlinkgain[40], sigma_tot[40], marker='o', markersize=5, color='red')
plt.plot(downlinkgain[80], sigma_tot[80], marker='o', markersize=5, color='red')
plt.plot(downlinkgain[120], sigma_tot[120], marker='o', markersize=5, color='red')
plt.plot(downlinkgain[160], sigma_tot[160], marker='o', markersize=5, color='red')
#plt.plot(Gain[0], ranging_error[0], marker='o', markersize=5, color='green')
#plt.plot(Gain[2], ranging_error[2], marker='o', markersize=5, color='green')
#plt.plot(Gain[4], ranging_error[4], marker='o', markersize=5, color='green')
#plt.plot(Gain[6], ranging_error[6], marker='o', markersize=5, color='green')
plt.xlabel('Downlink antenna gain [dBi]')
plt.ylabel('Ranging error [m]')
plt.title('Ranging error with respect to the antenna gain')
plt.legend(['Two-way ranging error'])
plt.grid(which='major', axis='both', linestyle='-')
plt.grid(which='minor', axis='both', linestyle='--')
plt.xlim(6.5, 18.5)
plt.ylim(1, 1000)
plt.yscale("log")


plt.figure()
#plt.plot(sigma_tot, bitrate_down, linewidth=2)
#plt.plot(sigma_tot, bitrate_up, linewidth=2)
plt.plot(bitrate_down, sigma_tot, linewidth=2)
plt.plot(bitrate_up, sigma_tot, linewidth=2)
plt.plot(bitrate_down[0], sigma_tot[0], marker='o', markersize=5, color='red')
plt.plot(bitrate_down[40], sigma_tot[40], marker='o', markersize=5, color='red')
plt.plot(bitrate_down[80], sigma_tot[80], marker='o', markersize=5, color='red')
plt.plot(bitrate_down[120], sigma_tot[120], marker='o', markersize=5, color='red')
plt.plot(bitrate_down[160], sigma_tot[160], marker='o', markersize=5, color='red')
plt.plot(bitrate_up[0], sigma_tot[0], marker='o', markersize=5, color='red')
plt.plot(bitrate_up[40], sigma_tot[40], marker='o', markersize=5, color='red')
plt.plot(bitrate_up[80], sigma_tot[80], marker='o', markersize=5, color='red')
plt.plot(bitrate_up[120], sigma_tot[120], marker='o', markersize=5, color='red')
plt.plot(bitrate_up[160], sigma_tot[160], marker='o', markersize=5, color='red')
plt.xlabel('Bit rate [bps]')
plt.ylabel('Ranging error [m]')
plt.title('Ranging error with respect to the Bit rate')
plt.legend(['Bit rate down', 'Bit rate up'])
plt.grid()
plt.xlim(0, 17000)
plt.ylim(1, 1000)
plt.yscale("log")
plt.grid(which='major', axis='both', linestyle='-')
plt.grid(which='minor', axis='both', linestyle='--')

plt.figure()
plt.plot(downlinkgain, bitrate_down, linewidth=2)
plt.plot(downlinkgain, bitrate_up, linewidth=2)
plt.plot(downlinkgain[0], bitrate_down[0], marker='o', markersize=5, color='red')
plt.plot(downlinkgain[40], bitrate_down[40], marker='o', markersize=5, color='red')
plt.plot(downlinkgain[80], bitrate_down[80], marker='o', markersize=5, color='red')
plt.plot(downlinkgain[120], bitrate_down[120], marker='o', markersize=5, color='red')
plt.plot(downlinkgain[160], bitrate_down[160], marker='o', markersize=5, color='red')
plt.plot(downlinkgain[0], bitrate_up[0], marker='o', markersize=5, color='red')
plt.plot(downlinkgain[40], bitrate_up[40], marker='o', markersize=5, color='red')
plt.plot(downlinkgain[80], bitrate_up[80], marker='o', markersize=5, color='red')
plt.plot(downlinkgain[120], bitrate_up[120], marker='o', markersize=5, color='red')
plt.plot(downlinkgain[160], bitrate_up[160], marker='o', markersize=5, color='red')
plt.ylabel('Bit rate [bps]')
plt.xlabel('Downlink gain [dB]')
plt.title('Bit rates with respect to the downlink gain')
plt.legend(['Bit rate down', 'Bit rate up'])
plt.grid()
plt.xlim(6.5, 18.5)




plt.show()