""" A script containing functions for each of the components of the genetic
algorithm. """

import random
import numpy as np
import pandas as pd

from genetic_data.operators import crossover, mutate_individual

def create_individual(row_limits, col_limits, column_classes, weights=None):
    """ Create an individual dataset's allele representation within the limits
    provided. Alleles are given in the form of a tuple.

    Parameters
    ----------
    row_limits : list
        Lower and upper bounds on the number of rows a dataset can have.
    col_limits : list
        Lower and upper bounds on the number of columns a dataset can have.
    column_classes : list
        A list of potential column classes to select from such as those found in
        `pdfs.py`.
    weights : list
        A sequence of relative weights the same length as `column_classes`. This
        acts as a loose probability distribution from which to sample column
        classes. If `None`, column classes are sampled equally.
    """

    if row_limits[0] > row_limits[1]:
        row_limits = row_limits[::-1]
    if col_limits[0] > col_limits[1]:
        col_limits = col_limits[::-1]

    alt_pdfs = {
        col: [c for c in column_classes if c != col] for col in column_classes
    }

    nrows = random.randint(*row_limits)
    ncols = random.randint(*col_limits)

    column_pdfs = [col(nrows, alt_pdfs[col]) for col in column_classes]

    individual = tuple([
        nrows, ncols, *random.choices(column_pdfs, weights=weights, k=ncols)
    ])

    return individual

def create_initial_population(size, row_limits, col_limits,
                              column_classes, weights=None):
    """ Create an initial population for the genetic algorithm based on the
    given parameters.

    Parameters
    ----------
    size : int
        The number of individuals in the population.
    row_limits : list
        Limits on the number of rows a dataset can have.
    col_limits : list
        Limits on the number of columns a dataset can have.
    column_classes : list
        A list of potential column classes such as those found in
        `column_pdfs.py`. Must have a `.sample()` and `.mutate()` method.
    weights : list
        A sequence of relative weights the same length as `column_classes`. This
        acts as a loose probability distribution from which to sample column
        classes. If `None`, column classes are sampled equally.

    Returns
    -------
    population : list
        A collection of individuals.
    """

    population = []
    for _ in range(size):
        individual = create_individual(row_limits, col_limits,
                                       column_classes, weights)
        population.append(individual)

    return population

def get_dataframe(individual):
    """ Return the actual dataset represented by an individual's alleles as a
    `pandas.DataFrame` object. """

    df = pd.DataFrame({
        f'col_{i}': col.sample() for i, col in enumerate(individual[2:])
    })

    return df

def get_fitness(fitness, population):
    """ Return the fitness score of each individual in a population. """

    population_fitness = np.empty(len(population))
    for i, individual in enumerate(population):
        df = get_dataframe(individual)
        population_fitness[i] = fitness(df)

    return population_fitness

def get_ordered_population(population, population_fitness):
    """ Return a dictionary with key-value pairs given by the individuals in a
    population and their respective fitness. This population is sorted into
    descending order of its values. """

    fitness_dict = {
        ind: fit for ind, fit in zip(population, population_fitness)
    }
    ordered_population = dict(
        sorted(fitness_dict.items(), reverse=True, key=lambda x: x[1])
    )

    return ordered_population

def select_breeders(ordered_population, best_prop, lucky_prop):
    """ Given a population ranked by their fitness, select a proportion of the
    `best` individuals and another of the `lucky` individuals if they are
    available. This mirrors the survival of the fittest paradigm whilst
    including a number of less-fit individuals to stop the algorithm from
    converging too early. """

    size = len(ordered_population)
    num_best = max(int(best_prop * size), 1)
    num_lucky = max(int(lucky_prop * size), 1)
    population = list(ordered_population.keys())

    breeders = []
    for _ in range(num_best):
        if population != []:
            best_breeder = population.pop(0)
            breeders.append(best_breeder)

    for _ in range(num_lucky):
        if population != []:
            lucky_breeder = random.choice(population)
            breeders.append(lucky_breeder)
            population.remove(lucky_breeder)

    return breeders

def create_offspring(breeders, prob, size):
    """ Given a set of breeders, create offspring from pairs of breeders until
    there are enough offspring. Each offspring is formed using a crossover
    operator on the two parent individuals. """

    offspring = []
    while len(offspring) < size:
        parent1, parent2 = random.choices(breeders, k=2)
        child = crossover(parent1, parent2, prob)
        offspring.append(child)

    return offspring

def mutate_population(population, mutation_rate, allele_prob, row_limits,
                      col_limits, pdfs, weights):
    """ Given a population, mutate a small number of its individuals according
    to a mutation rate. For each individual to be mutated, their alleles are
    mutated with probability `allele_prob`. """

    new_population = []
    for ind in population:
        if random.random() < mutation_rate:
            ind = mutate_individual(ind, allele_prob, row_limits, col_limits,
                                    pdfs, weights)
        new_population.append(ind)

    return new_population
