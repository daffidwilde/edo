Tutorial: running a GA for a simple fitness function
====================================================

Genetic algorithms are metaheuristics used to solve optimisation and search
problems effectively. They rely on :ref:`operators <ref-operators>` inspired by
the concept of natural selection. These operators are typically referred to as
selection, crossover and mutation respectively.

For the purposes of this tutorial, we will make use of the following example.

Given an :math:`m \times n` matrix of integers, :math:`X`, we can consider
:math:`X` to be a dataset with :math:`m` rows (instances) and :math:`n` columns
(attributes). Let :math:`X'` be a random sample of five elements from :math:`X`.
We define the fitness, :math:`f : M_{m, n} \left(\mathbb{Z}\right) \to
\mathbb{R}`, of :math:`X` to be:

.. math::
    f(X) := \left| \frac{1}{\left|X'\right|} \sum_{x' \in X'} x' -
    \frac{1}{\left|X\right|} \sum_{x \in X} x \right|

In simpler terms, the fitness of :math:`X` is the absolute difference between
the mean of a sample of five of its elements and the mean of all elements in
:math:`X`.

Installing GeneticData
----------------------

GeneticData relies only on Numpy, Scipy and Pandas so no additional installs are
required.

With that being said, the library is most easily installed using::

    $ pip install genetic_data

However, if you would like to install it from source::

    $ git clone https://github.com/daffidwilde/genetic_data.git
    $ cd genetic_data
    $ python setup.py install

Setting up the GA
-----------------



Running the GA
--------------
