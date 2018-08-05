Set a seed
----------

Since genetic algorithms are stochastic in nature, it is a good idea to set a
seed for any particular run. By doing this, the same GA can be run again and
again and you will always obtain the same results.

Without one, the GA here will just fall back on Numpy's innate pseudo-random
number generator making any results inconsistent between runs.

Seeds are controlled by the :code:`seed` parameter in :code:`run_algorithm` and
should be integer. See the :ref:`tutorials <refs-tutorials>` for examples of how
this is done.
