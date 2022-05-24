"""
Some unit tests
"""
import unittest
from Initials import initial_states_obtainer
#Test test function
def add(x, y):
    """ Add function """
    return x + y

class TestCalc(unittest.TestCase):

    def test_add(self):
        self.assertEqual(add(10, 5), 15)
        self.assertEqual(add(-1, 1), 0)
        self.assertEqual(add(-1, -1), -2)
    # per def, one test is run, but more statements give a more accurate test
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


if __name__ == '__main__':
    unittest.main()