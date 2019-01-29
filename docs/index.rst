.. Edo documentation master file, created by
   sphinx-quickstart on Mon Jul 16 12:37:18 2018.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Welcome to Edo's documentation!
===============================

Edo provides a framework for generating effective artificial datasets through
genetic evolution.

Consider a specific algorithm, and its objective function. Edo allows you to
pass that function to its genetic algorithm (GA) which will use this to go on
and create generations of datasets for which your algorithm performs
increasingly well at. Through this approach, you can not only create banks of
effective, reproducible datasets for your own use, but you are also able to
determine and study the preferred characteristics of such datasets, giving an
insight into why and when your algorithm performs well -- or not.

.. toctree::
   :maxdepth: 2
   :caption: Contents

   tutorial/index.rst
   how-to/index.rst
   discussion/index.rst
   reference/index.rst

Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
