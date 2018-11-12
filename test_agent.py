import unittest
import numpy as np

from agent import Agent


class TestAgent(unittest.TestCase):

    def test_average_angle_in_all_quadrants(self):
        for rotation in [0, np.pi/2, np.pi, 3*np.pi/2]:
            angles = [-np.pi + rotation, -np.pi/2 + rotation]
            expected = -np.pi + np.pi/4 + rotation
            a = Agent(0, 0, expected)
            a.average_direction(angles)
            self.assertAlmostEqual(expected, a.new_theta)


if __name__ == '__main__':
    unittest.main()
