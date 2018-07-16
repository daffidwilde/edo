.. GeneticData documentation master file, created by
   sphinx-quickstart on Mon Jul 16 12:37:18 2018.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Welcome to GeneticData's documentation!
=======================================

GeneticData is a library for generating artificial datasets through genetic
evolution. Typically, when faced with a problem in data science, the data is
fixed and the researcher must select an algorithm that suits both the problem
and performs well on the data. This is typically done by running multiple
algorithms on the dataset or by justifying a choice based on the findings of the
current literature. But what makes that data "good" for the algorithm? Why is it
that an algorithm performs well on some datasets and not others?

The purpose of this library is to create a population of families of datasets
for which a specific algorithm performs well with respect to its objective
function. This function is passed to a genetic algorithm (GA) where each 
individual represents a family of datasets defined by their dimensions, and the
statistical shape of each of its columns. The fitness of an individual is taken
using some amalgamation of the fitnesses from a sample of datasets belonging to
its family.

Through this genetic algorithm, the hope is to not only build up banks of
effective datasets for a particular algorithm but to give the user the ability
to determine and study the preferred characteristics of such datasets.

Moreover, since this GA can take any fitness function as argument, two or more
algorithms can be compared at once. For example, by considering two similar
algorithms :math:`A` and :math:`B` with fitness functions :math:`f_A` and
:math:`f_B` respectively. Then for a suitable dataset :math:`X` consider the
fitness function, denoted by :math:`f`, and
given by:

.. math::
    f(X) = f_A(X) - f_B(X)

This fitness function, when passed to the GA, will attempt to generate
individuals for which algorithm :math:`A` outperforms algorithm :math:`B`.

A schematic of a generic GA is given below.

.. image:: ./docs/_static/flowchart.png
    :scale: 100 %
    :alt: A schematic for a genetic algorithm
    :align: center

.. toctree::
   :maxdepth: 2
   :titlesonly:
   :caption: Contents:

   installation.rst
   usage/index.rst
   operators/index.rst
   components/index.rst
   reference/index.rst

Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
