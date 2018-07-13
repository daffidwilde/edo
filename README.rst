genetic_data
============

A library for generating artificial datasets through genetic evolution.
-----------------------------------------------------------------------

Typically, when faced with a problem in data science, the data is fixed and a
researcher must select an algorithm that suits both the problem and the data.
This is typically done by running multiple algorithms on the dataset or by
justifying a choice based on the findings of current literature. This problem is
very closely linked to its mirror partner. That is, if one has a particular
algorithm, how is data chosen that is well-suited to it? And even: can you
determine cases where one algorithm outperforms another for the same problem?

The purpose of this library is to create a collection of families of datasets
for which a specific algorithm performs well by using its objective function.
This function is passed to a genetic algorithm (GA) where individuals are
families of datasets defined by their dimensions and the shape of each of its
columns. The fitness of an individual is taken as some amalgamation of the 
fitnesses from a sample of datasets belonging to its family.

Since this GA can take any fitness function as argument, two or more algorithm's
can be compared at once. For example, consider two similar algorithms **A** and
**B** with fitness functions **f_A** and **f_B** respectively. Then for a
suitable dataset **X**, consider the fitness function, denoted by **f**, and
given by:

.. math::
    f(X) = f_A(X) - f_B(X)

This fitness function, when passed to the GA, will generate individuals for
which algorithm **A** outperforms algorithm **B**.

What is a genetic algorithm?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. image:: ./docs/_static/flow_chart.pdf
    :scale: 100 %
    :alt: A schematic for a genetic algorithm
    :align: center
