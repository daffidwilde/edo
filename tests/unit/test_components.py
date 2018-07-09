""" Tests for the components of the algorithm. """

from copy import deepcopy
from hypothesis import given, settings
from hypothesis.strategies import floats, integers, tuples

from genetic_data.pdfs import Gamma, Poisson
from genetic_data.components import create_individual, \
                                    create_initial_population, \
                                    get_fitness, \
                                    get_ordered_population, \
                                    select_breeders, \
                                    create_offspring, \
                                    mutate_population

from trivials import TrivialPDF, trivial_fitness

ind_limits = given(
    row_limits=tuples(integers(min_value=1, max_value=1e3),
                      integers(min_value=1, max_value=1e3)),
    col_limits=tuples(integers(min_value=1, max_value=1e3),
                      integers(min_value=1, max_value=1e3)),
    weights=tuples(floats(min_value=1e-10, max_value=1),
                   floats(min_value=1e-10, max_value=1),
                   floats(min_value=1e-10, max_value=1))
)

pop_limits = given(
    size=integers(min_value=1, max_value=100),
    row_limits=tuples(integers(min_value=1, max_value=1e3),
                      integers(min_value=1, max_value=1e3)),
    col_limits=tuples(integers(min_value=1, max_value=1e3),
                      integers(min_value=1, max_value=1e3)),
    weights=tuples(floats(min_value=1e-10, max_value=1),
                   floats(min_value=1e-10, max_value=1),
                   floats(min_value=1e-10, max_value=1))
)

selection_limits = given(
    size=integers(min_value=1, max_value=100),
    row_limits=tuples(integers(min_value=1, max_value=1e3),
                      integers(min_value=1, max_value=1e3)),
    col_limits=tuples(integers(min_value=1, max_value=1e3),
                      integers(min_value=1, max_value=1e3)),
    weights=tuples(floats(min_value=1e-10, max_value=1),
                   floats(min_value=1e-10, max_value=1),
                   floats(min_value=1e-10, max_value=1)),
    best_prop=floats(min_value=1e-10, max_value=1),
    lucky_prop=floats(min_value=1e-10, max_value=1)
)

mutation_limits = given(
    size=integers(min_value=1, max_value=100),
    row_limits=tuples(integers(min_value=1, max_value=1e3),
                      integers(min_value=1, max_value=1e3)),
    col_limits=tuples(integers(min_value=1, max_value=1e3),
                      integers(min_value=1, max_value=1e3)),
    weights=tuples(floats(min_value=1e-10, max_value=1),
                   floats(min_value=1e-10, max_value=1),
                   floats(min_value=1e-10, max_value=1)),
    mutation_rate=floats(min_value=0, max_value=1)
)

class TestCreation():
    """ Tests for the creation of an individual and an initial population. """

    @ind_limits
    def test_individual(self, row_limits, col_limits, weights):
        """ Create an individual and verify that it is a list of the correct
        length with the right characteristics. """

        pdfs = [TrivialPDF(), Gamma(), Poisson()]

        individual = create_individual(row_limits, col_limits, pdfs, weights)
        assert isinstance(individual, tuple)
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

        pdfs = [TrivialPDF(), Gamma(), Poisson()]
        population = create_initial_population(size, row_limits, col_limits,
                                               pdfs, weights)
        population_fitness = get_fitness(trivial_fitness, population)

        assert population_fitness.shape == (len(population),)
        assert population_fitness.dtype == 'float'

    @pop_limits
    def test_get_ordered_population(self, size, row_limits, col_limits,
                                    weights):
        """ Create a population, get its fitness and order the individuals in
        descending order of their fitness. Verify that all individuals are
        there. """

        pdfs = [TrivialPDF(), Gamma(), Poisson()]
        population = create_initial_population(size, row_limits, col_limits,
                                               pdfs, weights)
        population_fitness = get_fitness(trivial_fitness, population)
        ordered_population = get_ordered_population(population,
                                                    population_fitness)

        assert set(ordered_population.keys()) == set(population)


class TestBreedingProcess():
    """ Test the breeder selection and offspring creation process. """

    @selection_limits
    @settings(max_examples=100)
    def test_select_breeders(self, size, row_limits, col_limits, weights,
                             best_prop, lucky_prop):
        """ Create a population, get its fitness and select breeders based on
        that fitness vector. Verify that breeders are selected without
        replacement. """

        pdfs = [TrivialPDF(), Gamma(), Poisson()]
        population = create_initial_population(size, row_limits, col_limits,
                                               pdfs, weights)
        population_fitness = get_fitness(trivial_fitness, population)
        ordered_population = get_ordered_population(population,
                                                    population_fitness)
        breeders = select_breeders(ordered_population, best_prop, lucky_prop)

        ind_counts = {ind: 0 for ind in population}
        while breeders != []:
            for ind in population:
                if ind in breeders:
                    ind_counts[ind] += 1
                    breeders.remove(ind)
        for ind in ind_counts:
            assert ind_counts[ind] in [0, 1]

    @selection_limits
    def test_create_offspring(self):
        """ Select breeders from a population and create a new proto-population
        of offspring. Verify that each offspring is an individual and their are
        the correct number of them. That way, this collection of offspring are
        in fact a population. """

        pass

    @mutation_limits
    def test_mutate_population(self):
        """ Create a population and mutate it according to a mutation rate.
        Verify that the mutated population is of the correct size, and that each
        element of the population is an individual. """

        pass
