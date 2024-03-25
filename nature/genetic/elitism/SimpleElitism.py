import numpy as np

from nature.genetic.base import ElitismStrategyBase


class SimpleElitism(ElitismStrategyBase):

    def __init__(self) -> "SimpleElitism":
        super().__init__()

    def operate(self, current_gen_population: np.ndarray, fitness: np.ndarray, next_gen_population: np.ndarray):
        next_gen_population[-1] = np.copy(current_gen_population[np.argmax(fitness)])
