import numpy as np

from nature.genetic.base import MutationStrategyBase


class AmplificationMutation(MutationStrategyBase):

    def __init__(self, probability: np.float64, factor: np.float64) -> "AmplificationMutation":
        super().__init__()
        self.probability = np.float64(probability)
        self.factor = np.float64(factor)

    def operate(self, population: np.ndarray):
        sz_individual = population.shape[1]

        for individual in population:
            for i in range(sz_individual):
                if np.random.rand() <= self.probability:
                    individual[i] = self.factor * individual[i]

