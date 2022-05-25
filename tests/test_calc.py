"""
Some unit tests
"""
#general
import unittest
import numpy as np

#own libraries
from Initials import initial_states_obtainer
from Initials import Simulation_Time_Setup
from Saved_Data import Data_Loader
from Measurement_Model import measurement_functions
from Estimation_Model import Estimation_Setup
from Estimation_Model import estimator_functions
Name = Simulation_Time_Setup.DIRECTORY_NAME

states = Data_Loader.json_states_reader(Name)
output = Data_Loader.json_output_reader(Name)

nominal_range_observ = Estimation_Setup.nominal_range_array
nominal_rangerate_observ = Estimation_Setup.nominal_rangerate_array

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

    def test_measurementsarray_loader(self):
        a = Data_Loader.json_measurementarray_reader(Name)
        self.assertEqual(a[0, 1], states[0, 1])
        self.assertEqual(a[1, 2], states[60, 2])
        self.assertEqual(a[2, 3], states[120, 3])

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

    def test_measurementarray(self):
        a0 = states[0, :]
        a1 = states[60, :]
        a2 = states[120, :]
        b = measurement_functions.measurement_array(states, Simulation_Time_Setup.measurement_interval)
        self.assertEqual(b[0, 0], a0[0])
        self.assertEqual(b[0, 3], a0[3])
        self.assertEqual(b[0, 5], a0[5])
        self.assertEqual(b[1, 1], a1[1])
        self.assertEqual(b[1, 4], a1[4])
        self.assertEqual(b[2, 1], a2[1])
        self.assertEqual(b[2, 3], a2[3])
        self.assertEqual(b[2, 5], a2[5])

    def test_rangeobservations(self):
        a = measurement_functions.intersatellite_distances(states)
        b = measurement_functions.range_observations(states, 0, 0)
        self.assertEqual(a[23], b[23])
        self.assertEqual(a[1111], b[1111])

    def test_rangerateobservations(self):
        a = 108/np.sqrt(108)
        X = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11])
        b = measurement_functions.rangerate_observation_row(X, 0, 0)
        self.assertEqual(a, b)

    def test_observations(self):
        Y_range = estimator_functions.observations(nominal_range_observ, nominal_rangerate_observ, 0)
        Y_both = estimator_functions.observations(nominal_range_observ, nominal_rangerate_observ, 1)
        Y_rangerate = estimator_functions.observations(nominal_range_observ, nominal_rangerate_observ, 2)
        self.assertEqual(Y_range[100], Y_both[100, 0])
        self.assertEqual(Y_rangerate[12], Y_both[12,1])
        self.assertEqual(Y_both[30, 1], nominal_rangerate_observ[30])
        self.assertEqual(Y_range[24], nominal_range_observ[24])

if __name__ == '__main__':
    unittest.main()