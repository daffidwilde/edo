""" Tests for the components of the algorithm. """

from hypothesis import given
from hypothesis.strategies import floats, integers, tuples

from genetic_data.pdfs import Gamma, Poisson
from genetic_data.components import create_individual, create_initial_population

from trivials import TrivialPDF, trivial_fitness

ind_limits = given(
    row_limits=tuples(integers(min_value=1, max_value=1e3),
                      integers(min_value=1, max_value=1e3)),
    col_limits=tuples(integers(min_value=1, max_value=1e3),
                      integers(min_value=1, max_value=1e3)),
    weights=tuples(floats(min_value=1e-10, max_value=1-1e-10),
                   floats(min_value=1e-10, max_value=1-1e-10),
                   floats(min_value=1e-10, max_value=1-1e-10))
)

pop_limits = given(
    size=integers(min_value=0, max_value=100),
    row_limits=tuples(integers(min_value=1, max_value=1e3),
                      integers(min_value=1, max_value=1e3)),
    col_limits=tuples(integers(min_value=1, max_value=1e3),
                      integers(min_value=1, max_value=1e3)),
    weights=tuples(floats(min_value=1e-10, max_value=1-1e-10),
                   floats(min_value=1e-10, max_value=1-1e-10),
                   floats(min_value=1e-10, max_value=1-1e-10))
)


class TestCreation():
    """ Tests for the creation of an individual and an initial population. """

    @ind_limits
    def test_individual(self, row_limits, col_limits, weights):
        """ Create an individual and verify that it is a list of the correct
        length with the right characteristics. """

        pdfs = [TrivialPDF(), Gamma(), Poisson()]

        individual = create_individual(row_limits, col_limits, pdfs, weights)
        assert isinstance(individual, list)
        assert len(individual) == individual[1] + 2
        assert isinstance(individual[0], int) and isinstance(individual[1], int)

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


class TestGetFitness():
    """ Test the get_fitness function. """

    @pop_limits
    def test_get_fitness(self, size, row_limits, col_limits, weights):
        """ Create a population and get its fitness. Then verify that the
        fitness is of the correct size and data type. """
        pass
