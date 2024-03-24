import numpy as np

from genetic.base import CrossoverStrategyBase


class PointCrossover(CrossoverStrategyBase):

    def __init__(self, crossing_rate: np.float64) -> "PointCrossover":
        super().__init__()
        self.crossing_rate = np.float64(crossing_rate)

    def operate(self, population: np.ndarray, associated_fitness: np.ndarray) -> np.ndarray:
        population = population.copy()

        for i in range(0, len(population) - 1, 2):
            if np.random.random() <= self.crossing_rate:
                parentA = population[i]
                parentB = population[i + 1]

                n = np.random.randint(low=1, high=len(population[0]))

                startA, endA = np.copy(parentA[0:n]), np.copy(parentA[n:])
                startB, endB = np.copy(parentB[0:n]), np.copy(parentB[n:])

                population[i] = np.concatenate([ startA, endB ])
                population[i + 1] = np.concatenate([ startB, endA ])

        return population
