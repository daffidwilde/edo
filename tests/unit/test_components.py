""" Tests for the components of the algorithm. """

from hypothesis import settings
from genetic_data.pdfs import Gamma, Poisson
from genetic_data.components import create_individual, \
                                    create_initial_population, \
                                    get_fitness, \
                                    get_ordered_population, \
                                    select_breeders, \
                                    create_offspring, \
                                    mutate_population

from test_util.trivials import TrivialPDF, trivial_fitness
from test_util.parameters import individual_limits, \
                                 population_limits, \
                                 selection_limits, \
                                 offspring_limits, \
                                 mutation_limits


class TestCreation():
    """ Tests for the creation of an individual and an initial population. """

    @individual_limits
    def test_individual(self, row_limits, col_limits, weights):
        """ Create an individual and verify that it is a list of the correct
        length with the right characteristics. """

        pdfs = [Gamma, Poisson]

        individual = create_individual(row_limits, col_limits, pdfs, weights)
        assert isinstance(individual, tuple)
        assert len(individual) == individual[1] + 2
        assert isinstance(individual[0], int) and isinstance(individual[1], int)

        for col in individual[2:]:
            assert isinstance(col, tuple(pdfs))
            assert col.nrows == individual[0]

    @population_limits
    def test_initial_population(self, size, row_limits, col_limits, weights):
        """ Create an initial population of individuals and verify it is a list
        of the correct length with the right characteristics. """

        pdfs = [Gamma, Poisson]
        population = create_initial_population(size, row_limits, col_limits,
                                               pdfs, weights)

        assert isinstance(population, list)
        assert len(population) == size

        for ind in population:
            assert len(ind) == ind[1] + 2
            assert isinstance(ind[0], int) and isinstance(ind[1], int)

            for col in ind[2:]:
                assert isinstance(col, tuple(pdfs))
                assert col.nrows == ind[0]


class TestGetFitness():
    """ Test the get_fitness function. """

    @population_limits
    @settings(max_examples=100)
    def test_get_fitness(self, size, row_limits, col_limits, weights):
        """ Create a population and get its fitness. Then verify that the
        fitness is of the correct size and data type. """

        pdfs = [Gamma, Poisson]
        population = create_initial_population(size, row_limits, col_limits,
                                               pdfs, weights)
        population_fitness = get_fitness(trivial_fitness, population)

        assert population_fitness.shape == (size,)
        assert population_fitness.dtype == 'float'

    @population_limits
    def test_get_ordered_population(self, size, row_limits, col_limits,
                                    weights):
        """ Create a population, get its fitness and order the individuals in
        descending order of their fitness. Verify that all individuals are
        there. """

        pdfs = [Gamma, Poisson]
        population = create_initial_population(size, row_limits, col_limits,
                                               pdfs, weights)
        population_fitness = get_fitness(trivial_fitness, population)
        ordered_population = get_ordered_population(population,
                                                    population_fitness)

        assert set(ordered_population.keys()) == set(population)


class TestBreedingProcess():
    """ Test the breeder selection and offspring creation process. """

    @selection_limits
    @settings(max_examples=200)
    def test_select_breeders(self, size, row_limits, col_limits, weights,
                             props):
        """ Create a population, get its fitness and select breeders based on
        that fitness vector. Verify that breeders are selected without
        replacement. """

        best_prop, lucky_prop = props
        pdfs = [Gamma, Poisson]
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

    @offspring_limits
    @settings(max_examples=200)
    def test_create_offspring(self, size, row_limits, col_limits, weights,
                              props, prob):
        """ Create a population and use them to create a new proto-population
        of offspring. Verify that each offspring is an individual and their are
        the correct number of them. That way, this collection of offspring are
        in fact a population. """

        best_prop, lucky_prop = props
        pdfs = [Gamma, Poisson]
        population = create_initial_population(size, row_limits, col_limits,
                                               pdfs, weights)
        population_fitness = get_fitness(trivial_fitness, population)
        ordered_population = get_ordered_population(population,
                                                    population_fitness)
        breeders = select_breeders(ordered_population, best_prop, lucky_prop)
        offspring = create_offspring(breeders, prob, size)

        assert isinstance(offspring, list)
        assert len(offspring) == size

        for ind in offspring:
            assert len(ind) == ind[1] + 2
            assert isinstance(ind[0], int) and isinstance(ind[1], int)

            for col in ind[2:]:
                assert isinstance(col, tuple(pdfs))
                assert col.nrows == ind[0]

    @mutation_limits
    def test_mutate_population(self, size, row_limits, col_limits, weights,
                               mutation_rate, allele_prob):
        """ Create a population and mutate it according to a mutation rate.
        Verify that the mutated population is of the correct size, and that each
        element of the population is an individual. """

        pdfs = [Gamma, Poisson]
        population = create_initial_population(size, row_limits, col_limits,
                                               pdfs, weights)
        mutant_population = mutate_population(population, mutation_rate,
                                              allele_prob, row_limits,
                                              col_limits, pdfs, weights)

        assert isinstance(mutant_population, list)
        assert len(mutant_population) == len(population)

        for ind in mutant_population:
            assert len(ind) == ind[1] + 2
            assert isinstance(ind[0], int) and isinstance(ind[1], int)

            for col in ind[2:]:
                assert isinstance(col, tuple(pdfs))
                assert col.nrows == ind[0]
