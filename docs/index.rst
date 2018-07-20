.. GeneticData documentation master file, created by
   sphinx-quickstart on Mon Jul 16 12:37:18 2018.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Welcome to GeneticData's documentation!
=======================================

GeneticData provides a framework for generating families of artificial datasets
through genetic evolution for which a specific algorithm performs well.

More specifically, GeneticData runs a genetic algorithm (GA) using the objective
function of the algorithm of interest as its fitness function. In this GA, each 
individual represents a family of datasets, and each individual is represented
by a tuple (sometimes termed a "chromosome") which contains key information
about the kind of datasets in its family. Namely, that tuple has the following
entries:

* the number of rows (instances) in a dataset
* the number of columns (attributes) in a dataset
* the probability distribution for each column of a dataset

The fitness of an individual is taken using some amalgamation of the fitnesses
from a sample of datasets belonging to its family.

Through this approach, the hope is to not only make available banks of effective
datasets for a particular algorithm but to give the user the ability to
determine and study the preferred characteristics of such datasets.

.. toctree::
   :maxdepth: 2

   tutorial/index.rst
   operators/index.rst
   components/index.rst
   reference/index.rst

Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
