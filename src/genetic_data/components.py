""" A script containing functions for each of the components of the genetic
algorithm. """

import random

from collections import namedtuple
from dask import compute, delayed, get

import numpy as np

def create_individual(min_nrows, max_nrows, min_ncols, max_ncols,
                      column_classes, weights=None):
    """ Create an individual dataset's allele representation within the limits
    provided. Alleles are given in the form of a `namedtuple`.

    Parameters
    ----------
    min_nrows, max_nrows : int
        Limits on the number of rows a dataset can have.
    min_ncols, max_ncols : int
        Limits on the number of columns a dataset can have.
    column_classes : list
        A list of potential column classes to select from such as those found in
        `column_pdfs.py`.
    weights : list
        A sequence of relative weights the same length as `column_classes`. This
        acts as a probability distribution from which to sample column classes.
        If not specified, column classes are sampled equally.
    """
    nrows = random.randint(min_nrows, max_nrows+1)
    ncols = random.randint(min_ncols, max_ncols+1)

    dataset = namedtuple(
        'Dataset', ['nrows', 'ncols'] + [f'col_{i}' for i in range(ncols)]
    )

    individual = dataset(
        nrows, ncols, *random.choices(column_classes,
                                      weights=weights,
                                      k=ncols)
    )
    return individual

def create_initial_population(size, min_nrows, max_nrows, min_ncols, max_ncols,
                              column_classes, weights=None):
    """ Create an initial population for the genetic algorithm based on the
    given parameters.

    Parameters
    ----------
    size : int
        The number of individuals in the population.
    min_nrows, max_nrows : int
        Limits on the number of rows a dataset can have.
    min_ncols, max_ncols : int
        Limits on the number of columns a dataset can have.
    column_classes : list
        A list of potential column classes such as those found in
        `column_pdfs.py`.
    weights : list
        A sequence of relative weights the same length as `column_classes`. This
        acts as a probability distribution from which to sample column classes.
        If not specified, column classes are sampled equally.
    """
