import numpy as np

from genetic.base import SelectionStrategyBase


class TournamentSelection(SelectionStrategyBase):

    def __init__(self) -> "TournamentSelection":
        super().__init__()

    def operate(self, population: np.ndarray, fitness: np.ndarray) -> tuple[np.ndarray, np.ndarray]:
        possibles = np.array(range(len(population)))

        new_population = list()
        new_population_fitness = list()

        for _ in range(np.int64(len(population) / 2)):
            # Select A ----------------------------------------------------------------------

            competitors = np.random.choice(possibles, size=2)

            competitors_fitness = np.abs(fitness[competitors])

            probabilities = competitors_fitness / np.sum(competitors_fitness)

            selected_A = np.random.choice(competitors, p=probabilities)

            new_population.append(population[selected_A])
            new_population_fitness.append(fitness[selected_A])

            # Select B ----------------------------------------------------------------------

            competitors = np.random.choice(np.setdiff1d(possibles, [ selected_A ]), size=2)

            competitors_fitness = np.abs(fitness[competitors])

            probabilities = competitors_fitness / np.sum(competitors_fitness)

            selected_B = np.random.choice(competitors, p=probabilities)

            new_population.append(population[selected_B])
            new_population_fitness.append(fitness[selected_B])

        return np.array(new_population), np.array(new_population_fitness)