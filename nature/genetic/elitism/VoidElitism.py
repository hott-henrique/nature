import numpy as np

from nature.genetic.base import ElitismStrategyBase


class VoidElitism(ElitismStrategyBase):

    def __init__(self) -> "VoidElitism":
        super().__init__()

    def operate(self, current_gen_population: np.ndarray, fitness: np.ndarray, next_gen_population: np.ndarray):
        pass
