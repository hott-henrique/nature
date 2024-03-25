import numpy as np

from nature.genetic.base import MutationStrategyBase
from nature.params import InputBase


class SingleMutation(MutationStrategyBase):

    def __init__(self, probability: np.float64, input_model: InputBase) -> "SingleMutation":
        super().__init__()
        self.probability = probability
        self.input_model = input_model

    def operate(self, population: np.ndarray):
        for individual in population:
            if np.random.random() < self.probability:
                pos = np.random.randint(len(individual))
                individual[pos] = self.input_model.random_value(exclude=[ individual[pos] ])
