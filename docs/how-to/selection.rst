Customise the selection process
-------------------------------

It maybe be benefitial to your context to have control over how parents are
selected in each iteration. You can do that in two ways here by altering the
following parameters:

- :code:`best_prop`: this is the proportion of the population to skim off
  the top and take forward as parents.
- :code:`lucky_prop`: after the best individuals are chosen, you can take some
  "lucky" individuals into the next generation. By default, this doesn't happen.

.. note::
    Taking lucky individuals should be done sparingly as they are chosen
    randomly and can throw the GA off. The use of this functionality is only
    encouraged for particularly complex contexts where you can't obtain good
    enough results otherwise.
