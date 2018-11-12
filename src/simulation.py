from agent import Agent
from numpy.random import rand
from numpy import pi


class Simulation(object):
    def __init__(self, N, L, r=1, v=0.3):
        self.group = [Agent(L*rand(), L*rand(), 2*pi*(rand()-0.5), v) for _ in range(N)]
