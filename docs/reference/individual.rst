.. _create-ind:

Individuals
===========

At the beginning of any genetic algorithm, an initial population of individuals
is generated. Often this is done by sampling randomly from a parameter space,
though `other methods exist
<https://en.wikipedia.org/wiki/Latin_hypercube_sampling>`_ to get the most out
of the parameter space.

In this genetic algorithm, individuals are represented by a dataframe and a list
of column metadata about how the dataframe was generated and should be
manipulated. These objects are contained in a single :code:`namedtuple` object.

.. note::

    If you're unfamiliar with how named tuples work, they're similar to classes
    but more lightweight, whilst like a standard Python :code:`tuple` that is
    mutable. To learn more, you can go and read the `documentation
    <https://docs.python.org/2/library/collections.html#collections.namedtuple>`_.
