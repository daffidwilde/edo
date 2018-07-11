""" A collection of trivial classes/functions for use in tests. """

class TrivialPDF():
    """ A column pdf representative. """
    def __init__(self, alt_pdfs=None):
        self.alt_pdfs = alt_pdfs
    def sample(self):
        pass
    def method(self):
        pass

def trivial_fitness(individual):
    """ A fitness function. """
    pass
