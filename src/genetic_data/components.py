""" A script containing functions for each of the components of the genetic
algorithm. """

import random

def create_individual(row_limits, col_limits, column_classes, weights=None):
    """ Create an individual dataset's allele representation within the limits
    provided. Alleles are given in the form of a `namedtuple`.

    Parameters
    ----------
    row_limits : list
        Lower and upper bounds on the number of rows a dataset can have.
    col_limits : list
        Lower and upper bounds on the number of columns a dataset can have.
    column_classes : list
        A list of potential column classes to select from such as those found in
        `column_pdfs.py`.
    weights : list
        A sequence of relative weights the same length as `column_classes`. This
        acts as a loose probability distribution from which to sample column
        classes. If `None`, column classes are sampled equally.
    """

    min_nrows, max_nrows = row_limits
    min_ncols, max_ncols = col_limits

    if min_nrows > max_nrows:
        min_nrows, max_nrows = max_nrows, min_nrows
    if min_ncols > max_ncols:
        min_ncols, max_ncols = max_ncols, min_ncols

    nrows = random.randint(min_nrows, max_nrows)
    ncols = random.randint(min_ncols, max_ncols)

    individual = [
        nrows, ncols, *random.choices(column_classes, weights=weights, k=ncols)
    ]

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
    """

    population = []
    for _ in range(size):
        individual = create_individual(row_limits, col_limits,
                                       column_classes, weights)
        population.append(individual)

    return population
