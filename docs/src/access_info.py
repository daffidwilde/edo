""" .. How to access information from an individual. """

import numpy as np

from edo.individual import create_individual
from edo.pdfs import Normal, Poisson

np.random.seed(0)

individual = create_individual(
    row_limits=[3, 3], col_limits=[4, 4], pdfs=[Normal, Poisson]
)

df = individual.dataframe
meta = individual.metadata

df.round(4).to_csv("../how-to/access_dataframe.csv")

with open("../how-to/access_metadata.rst", "w") as ind_file:
    string = '.. :orphan:\n\n'
    string += "And the metadata like this::\n\n    "
    string += '>>> individual.metadata \n    '
    string += '['
    for col in meta:
        string += col.__repr__() + ', '
    string = string[:-2]
    string += '] \n    '
    ind_file.write(string)
