"""
Some unit tests
"""
#general
import unittest
import numpy as np

#own libraries
from Initials import initial_states_obtainer
from Saved_Data import Data_Loader
from Measurement_Model import measurement_functions
Name = "EML2_ELO_60390_10days"

states = Data_Loader.json_states_reader(Name)
output = Data_Loader.json_output_reader(Name)

class TestCalc(unittest.TestCase):

    def test_t0(self):
        self.assertEqual(initial_states_obtainer.simulation_start_epoch(59091.50), 652060869.1826417446136475)
        self.assertEqual(initial_states_obtainer.simulation_start_epoch(59137.00), 655992069.1826417446136475)
        self.assertEqual(initial_states_obtainer.simulation_start_epoch(60390.00), 764251269.1826417446136475)
        self.assertEqual(initial_states_obtainer.simulation_start_epoch(60418.00), 766670469.1826417446136475)
    def test_inieml2(self):
        result = initial_states_obtainer.initial_states_eml2(60390.00)
        self.assertEqual(result[0], -310537.9975687619880773 * 10 ** 3)
        self.assertEqual(result[1], 249423.1565183288475964 * 10 ** 3)
        self.assertEqual(result[2], 174937.7572135815862566 * 10 ** 3)
        self.assertEqual(result[3], -0.9931718419758050 * 10 ** 3)
        self.assertEqual(result[4], -0.7664085138876902 * 10 ** 3)
        self.assertEqual(result[5], -0.5251732804449779 * 10 ** 3)
    def test_states_loader(self):
        self.assertEqual(states[0,0], -310537.9975687619880773 * 10 ** 3)
        self.assertEqual(states[0,1], 249423.1565183288475964 * 10 ** 3)
        self.assertEqual(states[0,2], 174937.7572135815862566 * 10 ** 3)
        self.assertEqual(states[0,3], -0.9931718419758050 * 10 ** 3)
        self.assertEqual(states[0,4], -0.7664085138876902 * 10 ** 3)
        self.assertEqual(states[0,5], -0.5251732804449779 * 10 ** 3)
    def test_moon(self):
        """Database Moon states and the ephemeris Moon states lie within 1 m position accuracy and 1 mm/s velocity
        accuracy if this condition is met"""
        mjd_time1 = 60390
        et_time1 = initial_states_obtainer.simulation_start_epoch(mjd_time1)
        result_data1 = initial_states_obtainer.states_moon_data(mjd_time1, mjd_time1)[0]
        result_tudat1 = initial_states_obtainer.moon_ephemeris(np.linspace(et_time1,et_time1,1))[0]
        self.assertAlmostEqual(result_data1[0], result_tudat1[0], 0, "x-direction is way too off")
        self.assertAlmostEqual(result_data1[1], result_tudat1[1], 0, "y-direction is way too off")
        self.assertAlmostEqual(result_data1[2], result_tudat1[2], 0, "z-direction is way too off")
        self.assertAlmostEqual(result_data1[3], result_tudat1[3], 3, "vx-direction is way too off")
        self.assertAlmostEqual(result_data1[4], result_tudat1[4], 3, "vy-direction is way too off")
        self.assertAlmostEqual(result_data1[5], result_tudat1[5], 3, "vz-direction is way too off")
        mjd_time2 = 60400
        et_time2 = initial_states_obtainer.simulation_start_epoch(mjd_time2)
        result_data2 = initial_states_obtainer.states_moon_data(mjd_time2, mjd_time2)[0]
        result_tudat2 = initial_states_obtainer.moon_ephemeris(np.linspace(et_time2, et_time2, 1))[0]
        self.assertAlmostEqual(result_data2[0], result_tudat2[0], 0, "x-direction is way too off")
        self.assertAlmostEqual(result_data2[1], result_tudat2[1], 0, "y-direction is way too off")
        self.assertAlmostEqual(result_data2[2], result_tudat2[2], 0, "z-direction is way too off")
        self.assertAlmostEqual(result_data2[3], result_tudat2[3], 3, "vx-direction is way too off")
        self.assertAlmostEqual(result_data2[4], result_tudat2[4], 3, "vy-direction is way too off")
        self.assertAlmostEqual(result_data2[5], result_tudat2[5], 3, "vz-direction is way too off")
    def test_intersatellitedistance(self):
        dist_func = measurement_functions.intersatellite_distance(states[1000, :])
        dist_tudat = np.linalg.norm(output[1000, 34:37], axis=0)
        self.assertEqual(dist_func, dist_tudat)
if __name__ == '__main__':
    unittest.main()