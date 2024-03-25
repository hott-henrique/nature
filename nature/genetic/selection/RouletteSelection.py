import numpy as np

from nature.genetic.base import SelectionStrategyBase


class RouletteSelection(SelectionStrategyBase):

    def __init__(self) -> "RouletteSelection":
        super().__init__()

    def operate(self, population: np.ndarray, fitness: np.ndarray) -> tuple[np.ndarray, np.ndarray]:
        possibles = np.array(range(len(population)))

        new_population = list()
        new_population_fitness = list()

        for _ in range(np.int64(len(population) / 2)):
            competitors_fitness = fitness + np.min(fitness)

            probabilities = competitors_fitness / np.sum(competitors_fitness)

            parents = np.random.choice(possibles, p=probabilities, size=2)

            new_population.extend(population[parents])
            new_population_fitness.extend(fitness[parents])

        return np.array(new_population), np.array(new_population_fitness)
