""" A collection of trivial classes/functions for use in tests. """

class TrivialPDF():
    """ A column pdf representative. """
    def __init__(self, nrows=1, alternative_pdfs=None):
        self.nrows = nrows
        self.alternative_pdfs = alternative_pdfs
    def sample(self):
        pass
    def method(self):
        pass

def trivial_fitness(individual):
    """ A fitness function. """
    pass
