import numpy as np

from nature.genetic.base import MutationStrategyBase
from nature.params import InputBase


class FullMutation(MutationStrategyBase):

    def __init__(self, probability: np.float64, input_model: InputBase) -> "FullMutation":
        super().__init__()
        self.probability = probability
        self.input_model = input_model

    def operate(self, population: np.ndarray):
        for individual in population:
            for i in range(len(individual)):
                if np.random.random() < self.probability:
                    individual[i] = self.input_model.random_value()
