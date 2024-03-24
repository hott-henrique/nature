import numpy as np

from genetic.base import SelectionStrategyBase


class RandomSelection(SelectionStrategyBase):

    def __init__(self) -> "RandomSelection":
        super().__init__()

    def operate(self, population: np.ndarray, fitness: np.ndarray) -> tuple[np.ndarray, np.ndarray]:
        parents_sequence = np.random.randint(low=0, high=len(population),size=len(population))
        return population[parents_sequence], fitness[parents_sequence]
