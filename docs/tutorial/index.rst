Tutorials: running a GA for simple fitness functions
====================================================

In this tutorial, we will make use of a few small examples to demonstrate how
GeneticData's genetic algorithm can be used and applied to various mathematical
problems. Before that, however, the library needs to be installed.

Installing GeneticData
----------------------

GeneticData is built on Python 3, and relies only on
`NumPy <http://www.numpy.org/>`_ and `Pandas <https://pandas.pydata.org/>`_.
Hence, no additional installs are required. In addition to this, however,
`Matplotlib <http://matplotlib.org/>`_ (2.2+) is assumed for these tutorials.

With that being said, the library is most easily installed using :code:`pip`::

    $ pip install genetic_data

However, if you would like to install it from source then go ahead and clone the
GitHub repo::

    $ git clone https://github.com/daffidwilde/genetic_data.git
    $ cd genetic_data
    $ python setup.py install

Optimising a function
---------------------

The problem
+++++++++++

Suppose we want to optimise the function :math:`f(x) = x^2` for :math:`x \in
\mathbb{R}`. We can use our GA here by considering each :math:`x` to be a
dataset with exactly one row and one column like so:

.. table::
   :align: center

   +-----------+-----------+
   |           | column 0  |
   +===========+===========+
   | **row 0** | :math:`x` |
   +-----------+-----------+

For the sake of this example, let us assume our initial population has 100
individuals in it, and each of these :math:`x` values is normally distributed.
To incorporate some spread in the search space, let us allow these distributions
to randomly sample their mean and standard deviation within some bounds. By
default, these bounds are [-10, 10] and [0, 10] respectively for normally
distributed data.

That is, each initial :math:`x` is sampled from a distribution in the family of
normal distributions given by:

.. math::
    \mathcal{N} = \left\{
        N \left(\mu, \sigma^2\right) | \ \mu \in [-10, 10], \sigma \in [0,10]
    \right\}

The hope is that the GA will converge to something near the optimum of
:math:`f(x)` relatively quickly, so we will not impose any additional stopping
conditions except for a maximum number of iterations of 5.

Formulation
+++++++++++

So, to formulate and solve this problem in GeneticData we do the following:

First, import the library::

    >>> import genetic_data as gd

Define fitness::

    >>> def x_squared(df):
    ...     """ Take a 1x1 `pandas.DataFrame` object and return the square of
    ...     its only value. """
    ...
    ...     return df.iloc[0, 0] ** 2

Set up and run the GA::

    >>> pop, fit, all_pops, all_fits = gd.run_algorithm(
    ...     fitness=x_squared,
    ...     size=100,`
    ...     row_limits=[1, 1],
    ...     col_limits=[1, 1],
    ...     max_iter=5,
    ...     maximise=False,
    ...     seed=0
    ... )

The outputs of :code:`run_algorithm` are the final population and its associated
fitness vector, as well as lists of all populations and fitness scores in the
simulation. These are held in the variables :code:`pop`, :code:`fit`,
:code:`all_pops` and :code:`all_fits` respectively.

.. note::
    Here, many of the parameters for the GA are using their default settings.
    Discussion on how to customise these parameters is found in the
    :ref:`how-to` section, and their definitions are listed in :ref:`params`.

Visualising results
+++++++++++++++++++

To see the results of the GA (and whether it worked as expected) we will plot
the fitnesses of all the individuals at each epoch (timestep).

We'll do this using Matplotlib and Numpy, so let's import them first::

    >>> import matplotlib.pyplot as plt
    >>> import numpy as np

Then using Matplotlib we can superimpose our theoretical fitness function (the
solid blue line) with our observed fitness scores (orange scatter points)::

    >>> fig, (top, middle, bottom) = plt.subplots(
    ...     nrows=3,
    ...     ncols=2,
    ...     figsize=(30, 45),
    ...     dpi=300,
    ...     sharex=True,
    ...     sharey=True
    ... )

    >>> xs = np.linspace(-25, 25, 101)

    >>> for i in range(6):
    ...
    ...     if i < 2:
    ...         axes = top
    ...     elif i < 4:
    ...         axes = middle
    ...     else:
    ...         axes = bottom
    ...
    ...     j = i % 2
    ...     data = [[ind.iloc[0, 0] for ind in all_pops[i]], all_fits[i]]
    ...
    ...     axes[j].plot(xs, xs ** 2, lw=3, zorder=-1)
    ...     axes[j].scatter(*data, s=200, color='orange')
    ...
    ...     axes[j].set_title(f'Fitness scores in epoch {i}', size=24, pad=25)
    ...     if i in [4, 5]:
    ...         axes[j].set_xlabel(r'$x$', size=24)
    ...     if i in [0, 2, 4]:
    ...         ax.set_ylabel('Fitness', size=24)

    >>> plt.tight_layout(pad=5)
    >>> plt.show()

The above code should give a figure like this:

.. image:: ../_static/example1_plot.png
   :width: 100 %
   :align: center
   :alt: Fitness scores of every individual 

   

Finding an optimal dataset
--------------------------

The problem
+++++++++++

Given a set of :math:`n` numbers, :math:`X`, we can consider :math:`X` to be a
dataset with a single column (attribute) and :math:`n` rows (instances). Let
:math:`Y = \{y_1, \ldots y_5\}` be a random sample of five elements from
:math:`X`. We define the fitness, :math:`\ f : \mathbb{R}^n \to \mathbb{R}`, of
our dataset :math:`X` to be the square of the mean of our sample, :math:`Y`.
That is:

.. math::
    f(X) = \bar Y^2, \quad
    \text{where} \quad
    \bar Y = \frac{1}{5} \sum_{i = 1}^{5} y_i

Again, let our objective be to minimise this fitness function. 

In terms of the genetic algorithm, we would expect an optimal solution to be a
dataset whose entries have a mean of 0. This is due to the fact that the sample
mean is an unbiased estimator to a population mean.
