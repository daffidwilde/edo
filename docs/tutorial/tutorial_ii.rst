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
