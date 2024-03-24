import numpy as np

from genetic.base import CrossoverStrategyBase


class BLXAlpha(CrossoverStrategyBase):

    def __init__(self, alpha: np.float64) -> "BLXAlpha":
        super().__init__()
        self.alpha = alpha

    def operate(self, population: np.ndarray, associated_fitness: np.ndarray) -> np.ndarray:
        population = population.copy()

        for i in range(0, len(population) - 1, 2):
            n = len(population[0])

            X, Y = population[i], population[i + 1]

            for j in range(n):
                d = np.abs(X[j] - Y[j])

                population[i][j] = np.random.uniform(low=min(X[j], Y[j]) - self.alpha * d, high=max(X[j], Y[j]) + self.alpha * d)
                population[i + 1][j] = np.random.uniform(low=min(X[j], Y[j]) - self.alpha * d, high=max(X[j], Y[j]) + self.alpha * d)

        return population
