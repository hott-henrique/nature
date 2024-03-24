import abc

import numpy as np


class CrossoverStrategyBase(abc.ABC):

    def __init__(self) -> "CrossoverStrategyBase":
        super().__init__()

    @abc.abstractmethod
    def operate(self, population: np.ndarray, associated_fitness: np.ndarray) -> np.ndarray:
        pass
