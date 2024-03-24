import typing as t

import numpy as np

from params.InputBase import InputBase


class FloatInput(InputBase):

    def __init__(self,
                 size: np.uint64,
                 min_value: np.float64, max_value: np.float64) -> "FloatInput":
        super().__init__(size=size)
        self.min_value = np.float64(min_value)
        self.max_value = np.float64(max_value)

    def random(self, amount: np.uint64) -> np.ndarray:
        return np.random.uniform(low=self.min_value, high=self.max_value, size=(amount, self.size))

    def random_value(self, exclude: t.Iterable = list()) -> np.float64:
        while 1:
            value = np.random.uniform(low=self.min_value, high=self.max_value)

            if value not in exclude:
                return value
