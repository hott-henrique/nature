import numpy as np

from genetic.base import CrossoverStrategyBase


class BLXAlphaBeta(CrossoverStrategyBase):

    def __init__(self, alpha: np.float64, beta: np.float64) -> "BLXAlphaBeta":
        super().__init__()
        self.alpha = np.float64(alpha)
        self.beta  = np.float64(beta)

    def operate(self, population: np.ndarray, associated_fitness: np.ndarray) -> np.ndarray:
        population = population.copy()

        for i in range(0, len(population) - 1, 2):
            n = len(population[0])

            X, Y = np.array([ population[i], population[i + 1] ])[np.argsort([ associated_fitness[i], associated_fitness[i + 1] ])]

            for j in range(n):
                d = np.abs(X[j] - Y[j])

                if X[j] <= Y[j]:
                    population[i][j] = np.random.uniform(low=X[j] - self.alpha * d, high=Y[j] + self.beta * d)
                    population[i + 1][j] = np.random.uniform(low=X[j] - self.alpha * d, high=Y[j] + self.beta * d)
                else:
                    population[i][j] = np.random.uniform(low=Y[j] - self.beta * d, high=X[j] + self.alpha * d)
                    population[i + 1][j] = np.random.uniform(low=Y[j] - self.beta * d, high=X[j] + self.alpha * d)

        return population
