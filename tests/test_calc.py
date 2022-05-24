"""
Some unit tests
"""
#general
import unittest
#own libraries
from Initials import initial_states_obtainer
from Saved_Data import Data_Loader


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
        result = Data_Loader.json_states_reader("EML2_ELO_60390_10days")
        self.assertEqual(result[0,0], -310537.9975687619880773 * 10 ** 3)
        self.assertEqual(result[0,1], 249423.1565183288475964 * 10 ** 3)
        self.assertEqual(result[0,2], 174937.7572135815862566 * 10 ** 3)
        self.assertEqual(result[0,3], -0.9931718419758050 * 10 ** 3)
        self.assertEqual(result[0,4], -0.7664085138876902 * 10 ** 3)
        self.assertEqual(result[0,5], -0.5251732804449779 * 10 ** 3)


if __name__ == '__main__':
    unittest.main()