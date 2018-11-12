import numpy as np
from numpy.random import rand


class Agent(object):
    def __init__(self, x, y, theta, temp, v):
        self.x = x
        self.y = y
        self.theta = theta
        self.new_theta = theta
        self.v = v
        self.temp = temp

    def average_direction(self, neighbour_angles):
        vx = 0
        vy = 0
        for angle in neighbour_angles:
            vx += self.v*np.cos(angle)
            vy += self.v*np.sin(angle)
        return np.arctan2(vy, vx)

    def update_direction(self):
        self.theta = self.new_theta

    def update_position(self):
        self.x += self.v * np.cos(self.theta)
        self.y += self.v * np.sin(self.theta)


    def apply_periodic_boundary(self, L):
        if self.x < 0:
            self.x += L
        if self.x > L:
            self.x -= L

        if self.y < 0:
            self.y += L
        if self.y > L:
            self.y -= L

    def perturbation(self):
        return (rand()-0.5) * self.temp