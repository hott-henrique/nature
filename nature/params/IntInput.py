import typing as t

import numpy as np

from params.InputBase import InputBase


class IntInput(InputBase):

    def __init__(self,
                 size: np.uint64,
                 min_value: np.int64, max_value: np.int64) -> "IntInput":
        super().__init__(size=size)
        self.min_value = np.int64(min_value)
        self.max_value = np.int64(max_value)

    def random(self, amount: np.uint64) -> np.ndarray:
        return np.random.randint(low=self.min_value, high=self.max_value, size=(amount, self.size))

    def random_value(self, exclude: t.Iterable = list()) -> np.int64:
        while 1:
            value = np.random.randint(low=self.min_value, high=self.max_value)

            if value not in exclude:
                return value
