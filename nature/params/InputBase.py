import abc
import typing as t

import numpy as np


class InputBase(abc.ABC):

    def __init__(self, size: np.uint64) -> "InputBase":
        super().__init__()
        self.size = np.uint64(size)

    @abc.abstractmethod
    def random(self, amount: np.uint64) -> np.ndarray:
        pass

    @abc.abstractmethod
    def random_value(self, exclude: t.Iterable = list()) -> t.Any:
        pass

