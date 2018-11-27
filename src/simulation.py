from agent import Agent
from numpy.random import rand
from numpy import pi, cos, sin
import matplotlib
import matplotlib.pyplot as plt


class Simulation(object):
    def __init__(self, N, L, temp, duration, r=1, v=0.3):
        self.L = L
        self.duration = duration
        self.r = r
        self.group = [Agent(L*rand(), L*rand(), 2*pi*(rand()-0.5), temp, v) for _ in range(N)]

    def run(self):
        for time in range(self.duration):

            self.calculate_new_angles()

            self.update_positions()

            self.apply_boundary_conditions()

            self.update_angles()

            self.plot()

    def calculate_new_angles(self):
        for agent in self.group:
            neighbour_angles = self.find_neighbour_angles(agent)
            agent.new_theta = agent.average_direction(neighbour_angles) + agent.perturbation()

    def find_neighbour_angles(self, agent):
        angles = list()
        for neighbour in self.group:
            if self.distance_squared(agent, neighbour) < self.r**2:
                angles.append(neighbour.theta)
        return angles

    def distance_squared(self, a1, a2):
        return ((a1.x - a2.x)**2) + ((a1.y - a2.y)**2)

    def update_positions(self):
        for agent in self.group:
            agent.update_position()

    def apply_boundary_conditions(self):
        for agent in self.group:
            agent.apply_periodic_boundary(self.L)

    def update_angles(self):
        for agent in self.group:
            agent.update_direction()

    def plot(self):
        x = [agent.x for agent in self.group]
        y = [agent.y for agent in self.group]
        vx = [agent.v * cos(agent.theta) for agent in self.group]
        vy = [agent.v * sin(agent.theta) for agent in self.group]
        plt.quiver(x, y, vx, vy)
        plt.xlim((0, self.L))
        plt.ylim((0, self.L))
        plt.pause(0.0001)
        plt.clf()


if __name__ == '__main__':
    Simulation(200, 10, 1, 100000).run()
