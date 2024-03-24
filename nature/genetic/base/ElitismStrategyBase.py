import abc

import typing as t

import numpy as np


class ElitismStrategyBase(abc.ABC):

    def __init__(self) -> "ElitismStrategyBase":
        super().__init__()

    @abc.abstractmethod
    def operate(self, current_gen_population: np.ndarray, fitness: np.ndarray, next_gen_population: np.ndarray):
        pass
