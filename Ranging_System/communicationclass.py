#general
import numpy as np

#tudatpy
from tudatpy.kernel import constants



class communication:
    def __init__(self,dmin, dmax, Tx, frequency, datarate, A_antenna, eta_antenna, cablelosses, polarizationlossfactor, T_noise, Rx_LOSS, implementationLOSS, EbNo_treshold, Bandwidth):
        self.dmin = dmin                                        #Calculated
        self.dmax = dmax                                        #Calculated
        self.Tx = 10*np.log10(Tx)                               #From exisiting literature?
        self.frequency = frequency                              #Low level S-band (2200MHz)
        self.datarate = datarate                                #approx 5000 bps?
        self.A_antenna = A_antenna                              #10cm^2?
        self.eta_antenna = eta_antenna                          #How to calculate? normal is around 50-60% right?
        self.cablelosses = cablelosses                          #How to calculate
        self.polarizationlossfactor = polarizationlossfactor    #Guess or determine this?
        self.T_noise = T_noise                                  #Is this just operationtemperatur?
        self.Rx_LOSS = Rx_LOSS                                  #Is this cableLOSS on receiver side?
        self.implementationLOSS = implementationLOSS            #
        self.EbNo_treshold = EbNo_treshold
        self.Bandwidth = Bandwidth
        self.noise_1Hz = None
        self.margin_min = None
        self.margin_max = None
        self.SNR_min = None
        self.SNR_max = None
        self.EbNo_min = None
        self.EbNo_max = None
        self.noise = None

    def communication_parameters(self):
        wavelength = constants.SPEED_OF_LIGHT/self.frequency
        Gain = self.eta_antenna*4*np.pi*self.A_antenna/wavelength**2
        GoverT = Gain + 10*np.log10(self.T_noise)

        polarizationLOSS = 10*np.log10(self.polarizationlossfactor)
        freespaceLOSS_min = 20*np.log10(4*np.pi*self.dmin/wavelength)
        freespaceLOSS_max = 20*np.log10(4*np.pi*self.dmax/wavelength)

        EIRP = self.Tx - self.cablelosses + Gain

        Rx_signal_min = EIRP - freespaceLOSS_min - polarizationLOSS - self.Rx_LOSS
        Rx_signal_max = EIRP - freespaceLOSS_max - polarizationLOSS - self.Rx_LOSS

        self.SNR_max = Rx_signal_max + GoverT - 10*np.log10(constants.BOLTZMANN_CONSTANT)
        self.SNR_min = Rx_signal_min + GoverT - 10*np.log10(constants.BOLTZMANN_CONSTANT)

        self.EbNo_max = self.SNR_max + 10*np.log10(self.datarate)
        self.EbNo_min = self.SNR_min + 10*np.log10(self.datarate)

        self.margin_max = self.EbNo_max - self.EbNo_treshold - self.implementationLOSS
        self.margin_min = self.EbNo_min - self.EbNo_treshold - self.implementationLOSS

        self.noise_1hz = constants.BOLTZMANN_CONSTANT*self.T_noise
        self.noise = self.noise_1hz * 10*np.log10(self.Bandwidth)
        # noise = kb*Ts*B
        #kb = boltzmann constant, Ts = T_noise, B = Bandwidth







