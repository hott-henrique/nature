import abc

import numpy as np

class SelectionStrategyBase(abc.ABC):

    def __init__(self) -> "SelectionStrategyBase":
        super().__init__()

    @abc.abstractmethod
    def operate(self, population: np.ndarray, fitness: np.ndarray) -> tuple[np.ndarray, np.ndarray]:
        pass
