#general
import numpy as np
#own
from Initials.Simulation_Time_Setup import DIRECTORY_NAME
from Saved_Data import Data_Loader

#tudatpy
from tudatpy.kernel import constants



class communication:
    def __init__(self,dmin, dmax, Tx, frequency, datarate, A_antenna, eta_antenna, cablelosses, polarizationlossfactor, T_noise):
        self.dmin = dmin
        self.dmax = dmax
        self.Tx = Tx
        self.frequency = frequency
        self.datarate = datarate
        self.A_antenna = A_antenna
        self.eta_antenna = eta_antenna
        self.cablelosses = cablelosses
        self.polarizationlossfactor = polarizationlossfactor
        self.T_noise = T_noise
    def communication_parameters(self):
        wavelength = constants.SPEED_OF_LIGHT/self.frequency
        Gain = self.eta_antenna*4*np.pi*self.A_antenna/wavelength**2
        GoverT = Gain + 10*np.log10(self.T_noise)



        polarizationLOSS = 10*np.log10(self.polarizationlossfactor)
        freespaceLOSS_min = 20*np.log10(4*np.pi*self.dmin/wavelength)
        freespaceLOSS_max = 20*np.log10(4*np.pi*self.dmax/wavelength)

        EIRP = self.Tx - self.cablelosses + Gain







