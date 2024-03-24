import typing as t

import numpy as np

from params.InputBase import InputBase
from genetic.base import SelectionStrategyBase
from genetic.base import CrossoverStrategyBase
from genetic.base import MutationStrategyBase
from genetic.base import ElitismStrategyBase
from genetic.base.GeneticAlgorithmLoggerBase import GeneticAlgorithmLoggerBase


class GeneticAlgorithmBase(object):

    def __init__(self,
                 input_model: InputBase,
                 selection_strategy: SelectionStrategyBase,
                 crossover_strategy: CrossoverStrategyBase,
                 mutation_strategy: MutationStrategyBase,
                 elitism_strategy: ElitismStrategyBase,
                 objective_function: t.Callable[[ np.ndarray ], t.SupportsFloat],
                 logger: GeneticAlgorithmLoggerBase = GeneticAlgorithmLoggerBase()) -> "GeneticAlgorithmBase":
        super().__init__()
        self.input_model = input_model
        self.objective_function = objective_function
        self.selection_strategy = selection_strategy
        self.crossover_strategy = crossover_strategy
        self.mutation_strategy = mutation_strategy
        self.elitism_strategy = elitism_strategy
        self.logger = logger

    def simulate(self,
                 population_size: np.unsignedinteger,
                 max_generations: np.unsignedinteger):
        population = self.input_model.random(amount=population_size)

        for _ in range(max_generations):
            fitness = np.apply_along_axis(self.objective_function, -1, population)

            self.logger.on_fitness(population=population, fitness=fitness)

            parents, associated_fitness = self.selection_strategy.operate(population=population, fitness=fitness)

            new_population = self.crossover_strategy.operate(population=parents, associated_fitness=associated_fitness)

            self.mutation_strategy.operate(population=new_population)

            self.elitism_strategy.operate(current_gen_population=population, fitness=fitness, next_gen_population=new_population)

            population = new_population

        fitness = np.apply_along_axis(self.objective_function, -1, population)

        self.logger.on_fitness(population=population, fitness=fitness)

        max_fitness_individual_idx = np.argmax(fitness)

        return population[max_fitness_individual_idx], fitness[max_fitness_individual_idx]
