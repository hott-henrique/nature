import typing as t

import numpy as np

from nature.params.InputBase import InputBase


class SetInput(InputBase):

    def __init__(self, size: np.uint64, possible_values: t.Iterable) -> "SetInput":
        super().__init__(size=size)
        self.possible_values = list(possible_values)

    def random(self, amount: np.uint64):
        return np.random.choice(self.possible_values, size=(amount, self.size))

    def random_value(self, exclude: t.Iterable = list()):
        while 1:
            value = np.random.choice(self.possible_values)

            if value not in exclude:
                return value
