Correlating two columns
=======================

Consider the task of finding two perfectly correlated (be that positive or
negative) sets of numbers. However, the context of the problem specifies that
one of these sets is a discrete, and the other is continuous.

Then the objective function for such an algorithm would simply be the square of
the r-value, or correlation coefficient. We can obtain this objective function
using SciPy::

   >>> from scipy.stats import linregress

   >>> def r_squared(df):
   ...     """ Return the square of the r-value between the columns of `df`. """
   ... 
   ...     _, _, r, _, _ = linregress(df.iloc[:, 0].values, df.iloc[:, 1].values)
   ...     return r ** 2

With this objective function, we can run the algorithm as normal -- with the
addition of another distribution in :code:`pdfs`. We can also include the
specification on the nature of the columns by using tuples in the column
limits::

   >>> import edo
   >>> from edo.pdfs import Normal, Poisson

   >>> pop, fit, all_pops, all_fits = edo.run_algorithm(
   ...     fitness=linregress_fitness,
   ...     size=100,
   ...     row_limits=[10, 50],
   ...     col_limits=[(1, 1), (1, 1)],
   ...     pdfs=[Normal, Poisson],
   ...     max_iter=50,
   ...     maximise=True,
   ...     seed=0
   ... )
