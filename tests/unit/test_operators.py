""" Tests for the crossover and mutation operator scripts. """

from hypothesis import given
from hypothesis.strategies import floats, integers, tuples

from genetic_data.components import create_individual
from genetic_data.operators import crossover, mutate_individual
from genetic_data.pdfs import Gamma, Poisson

operator_limits = given(
    row_limits=tuples(integers(min_value=1, max_value=1e3),
                      integers(min_value=1, max_value=1e3)),
    col_limits=tuples(integers(min_value=1, max_value=1e3),
                      integers(min_value=1, max_value=1e3)),
    weights=tuples(floats(min_value=1e-10, max_value=1),
                   floats(min_value=1e-10, max_value=1)),
    prob=floats(min_value=1e-10, max_value=1)
)

@operator_limits
def test_crossover_length(row_limits, col_limits, weights, prob):
    """ Verify that `crossover` produces a valid individual. """

    pdfs = [Gamma, Poisson]

    parent1 = create_individual(row_limits, col_limits, pdfs, weights)
    parent2 = create_individual(row_limits, col_limits, pdfs, weights)
    offspring = crossover(parent1, parent2, prob)

    assert isinstance(offspring, tuple)
    assert len(offspring) == offspring[1] + 2
    for col in offspring[2:]:
        assert isinstance(col, tuple(pdfs))

@operator_limits
def test_mutate_individual(row_limits, col_limits, weights, prob):
    """ Verify that an individual can be mutated to give another individual. """

    pdfs = [Gamma, Poisson]
    individual = create_individual(row_limits, col_limits, pdfs, weights)
    mutant = mutate_individual(individual, prob, row_limits, col_limits, pdfs,
                               weights)

    assert isinstance(mutant, tuple)
    assert len(mutant) == mutant[1] + 2
    for col in mutant[2:]:
        assert isinstance(col, tuple(pdfs))
