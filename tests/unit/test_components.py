""" Tests for the components of the algorithm. """

from hypothesis import given, settings
from hypothesis.strategies import floats, integers, tuples

from genetic_data.column_pdfs import Gamma, Poisson
from genetic_data.components import create_individual, create_initial_population

from test_column_pdfs import TrivialPDF

class TestCreation():
    """ Tests for the creation of an individual and an initial population. """

    limits = given(
        row_limits=tuples(integers(min_value=1, max_value=1e3),
                          integers(min_value=1, max_value=1e3)),
        col_limits=tuples(integers(min_value=1, max_value=1e3),
                          integers(min_value=1, max_value=1e3)),
        weights=tuples(floats(min_value=1e-10, max_value=1-1e-10),
                       floats(min_value=1e-10, max_value=1-1e-10),
                       floats(min_value=1e-10, max_value=1-1e-10))
    )

    @limits
    def test_individual(self, row_limits, col_limits, weights):
        """ Create an individual and verify that it is a list of the correct
        length with the right characteristics. """

        pdfs = [TrivialPDF(), Gamma(), Poisson()]

        individual = create_individual(row_limits, col_limits, pdfs, weights)
        assert isinstance(individual, list)
        assert len(individual) == individual[1] + 2
        assert isinstance(individual[0], int) and isinstance(individual[1], int)

    pop_limits = given(
        size=integers(min_value=0, max_value=100),
        row_limits=tuples(integers(min_value=1, max_value=1e5),
                          integers(min_value=1, max_value=1e5)),
        col_limits=tuples(integers(min_value=1, max_value=1e3),
                          integers(min_value=1, max_value=1e3)),
        weights=tuples(floats(min_value=1e-10, max_value=1-1e-10),
                       floats(min_value=1e-10, max_value=1-1e-10),
                       floats(min_value=1e-10, max_value=1-1e-10))
    )

    @pop_limits
    def test_initial_population(self, size, row_limits, col_limits, weights):
        """ Create an initial population of individuals and verify it is a list
        of the correct length with the right characteristics. """

        pdfs = [TrivialPDF(), Gamma(), Poisson()]

        population = create_initial_population(size, row_limits, col_limits,
                                               pdfs, weights)

        assert isinstance(population, list)
        assert len(population) == size

        for ind in population:
            assert len(ind) == ind[1] + 2
            assert isinstance(ind[0], int) and isinstance(ind[1], int)
