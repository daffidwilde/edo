Representation of individuals
-----------------------------

Typically in genetic algorithms, individuals are the bit string representation
of potential solutions to the problem at hand. Some people would say that our GA
is not a GA at all because we do not follow this convention.

However, we believe that the problem of generating artificial datasets is too
delicate to be solved by manipulating bit strings, and what makes an algorithm
genetic are the crossover and mutation operators. Instead of bit strings,
individuals are represented by a tuple containing two objects: a physical
dataset with rows and columns, and a list of probability distributions whose
elements are associated with the respective column of the dataset.
