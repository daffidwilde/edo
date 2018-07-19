Operators
=========

Most genetic algorithms make use of three operators to move from the current
population to the next. These are *selection*, *crossover* and *mutation*. For
the GA used in GeneticData, descriptions of these operators are given below.

Selection
---------

The selection operator is the process by which individuals are chosen from the
current population to act as the "parents" of the next generation. Almost
always, selection operators determine whether an individual should become a
parent based on their fitness.

In GeneticData, a population is ranked in *descending* order of fitness and a
proportion of the top is skimmed off to become parents. We also allow for the
random selection of some "lucky" individuals to be carried forward with the
fittest members of the population, if there are any still available.

These proportions are controlled using the :code:`best_prop` and
:code:`lucky_prop` parameters in :code:`run_algorithm`.

.. note::
    The best individuals are always chosen before lucky ones. For instance, if
    :code:`best_prop` takes value 1, then all individuals are used as parents
    and :code:`lucky_prop` can be any value.

Crossover
---------

Crossover operators take two individuals and return one or more "offspring"
individuals. In GeneticData, the crossover operator returns exactly one
individual from a pair of parents.

Here, parents can have chromosomes of different lengths, i.e. if they have
different numbers of columns from one another. So, the "alleles" are sampled
from the parents in order; beginning with the number of rows, then the number of
columns, and then each column distribution until enough columns have been
chosen.

Alleles are sampled from the first parent with a probability, given by
:code:`prob`, otherwise they are sampled from the second parent. In the case
where the number of columns in the offspring is sampled from the longer parent,
column distributions are taken according to :code:`prob` from either parent
until the shorter parent's final column. All subsequent column distributions are
then inherited directly from the longer parent.

Example::

    >>> import random
    >>> from genetic_data.operators import crossover

    >>> random.seed(101)

    >>> parent1 = tuple([10, 3, 'one', 'one', 'one'])
    >>> parent2 = tuple([12, 1, 'two'])

    >>> offspring = crossover(parent1, parent2, prob=0.5)
    >>> print(offspring)
    (12, 3, 'two', 'one', 'one')


Mutation
--------

To maintain a level of variety in a population and to force a GA to explore more
of the search space, individuals are mutated during the "birth" process. There
are several practices taken but the most common is this. Take each individual in
the new population of offspring and run along their alleles, deciding whether or
not to mutate that allele according to a probability.

In GeneticData, this probability is controlled by the parameter
:code:`allele_prob`. There is also the ability to control the probability with
which *any* individual is mutated using the :code:`mutation_prob` parameter.

By default, :code:`mutation_prob` takes value 1 so all individuals are up for
mutation, and each allele is mutated in the following way:

* The number of rows and/or columns are mutated by resampling from the discrete
  uniform distribution over :code:`row_limits` and :code:`col_limits`
  respectively.
* Each subsequent column distribution is mutated by either:

  - mutating to another type of distribution passed to the GA in the
    :code:`pdfs` parameter (and sampling the required parameters for that
    distribution); or
  - mutating the parameter(s) for the current type of distribution, i.e.
    changing the shape of that column.
