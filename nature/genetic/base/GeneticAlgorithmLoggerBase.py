import numpy as np


class GeneticAlgorithmLoggerBase(object):

    def __init__(self) -> "GeneticAlgorithmLoggerBase":
        super().__init__()

    def on_fitness(self, population: np.ndarray, fitness: np.ndarray):
        pass
