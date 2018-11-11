import numpy as np


class Agent(object):
    def __init__(self, x, y, theta):
        self.v = 0.3
        self.x = x
        self.y = y
        self.theta = theta

    def average_direction(self, neighbour_angles):
        vx = 0
        vy = 0
        for angle in [self.theta] + neighbour_angles:
            vx += self.v*np.cos(angle)
            vy += self.v*np.sin(angle)
        return np.arctan2(vy, vx)
