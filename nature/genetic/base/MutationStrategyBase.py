import abc

import numpy as np


class MutationStrategyBase(abc.ABC):

    def __init__(self) -> "MutationStrategyBase":
        super().__init__()

    @abc.abstractmethod
    def operate(self, population: np.ndarray):
        pass
