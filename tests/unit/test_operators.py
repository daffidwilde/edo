""" Tests for the crossover and mutation operator scripts. """

from genetic_data.components import create_individual
from genetic_data.operators import crossover, mutate_individual
from genetic_data.pdfs import Gamma, Poisson

from test_util.parameters import operator_limits

@operator_limits
def test_crossover(row_limits, col_limits, weights, prob):
    """ Verify that `crossover` produces a valid individual. """

    pdfs = [Gamma, Poisson]
    parent1 = create_individual(row_limits, col_limits, pdfs, weights)
    parent2 = create_individual(row_limits, col_limits, pdfs, weights)
    individual = crossover(parent1, parent2, prob)
    assert isinstance(individual, tuple)
    assert len(individual) == individual[1] + 2

    for col in individual[2:]:
        assert isinstance(col, tuple(pdfs))

@operator_limits
def test_mutate_individual(row_limits, col_limits, weights, prob):
    """ Verify that an individual can be mutated to give another individual. """

    pdfs = [Gamma, Poisson]
    alt_pdfs = {'Gamma': [Poisson], 'Poisson': [Gamma]}
    individual = create_individual(row_limits, col_limits, pdfs, weights,
                                   alt_pdfs)
    mutant = mutate_individual(individual, prob, row_limits, col_limits, pdfs,
                               weights, alt_pdfs)
    assert isinstance(mutant, tuple)
    assert len(mutant) == mutant[1] + 2

    for col in mutant[2:]:
        assert isinstance(col, tuple(pdfs))
