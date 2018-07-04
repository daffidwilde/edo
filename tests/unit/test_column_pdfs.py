""" Unit tests for the standard columns pdf's. """

from hypothesis import given
from hypothesis.strategies import floats, integers

from genetic_data.column_pdfs import Gamma

class TrivialPDF(object):
    """ A trivial pdf class for testing. """
    def sample(self):
        """ Trivial sample. """
        pass
    def mutate(self):
        """ Trivial mutation. """
        pass


@given(alpha=floats(min_value=1e-3),
       theta=floats(min_value=1e-3),
       nrows=integers(min_value=1))
def test_gamma_sample(alpha, theta, nrows):
    """ Verify that a given Gamma object can sample correctly. """

    gamma_pdf = Gamma(alpha, theta, nrows)
    sample = gamma_pdf.sample()
    assert sample.shape == (nrows,)
    assert sample.dtype == 'float'


@given(alpha=floats(min_value=1e-3),
       theta=floats(min_value=1e-3),
       nrows=integers(min_value=1))
def test_gamma_mutation_defaults(alpha, theta, nrows):
    """ Verify that by default Gamma.mutate() returns itself. """

    gamma_pdf = Gamma(alpha, theta, nrows, [TrivialPDF()])
    mutant = gamma_pdf.mutate()
    assert gamma_pdf == mutant

def test_gamma_change_pdf():
    """ Verify Gamma object can mutate to another kind of pdf. Here the
    TrivialPDF class is used for illustration. """

    gamma_pdf = Gamma(alternative_pdfs=[TrivialPDF()])
    mutant = gamma_pdf.mutate(change_pdf=True)
    assert 'TrivialPDF' in str(mutant.__class__)

@given(alpha=floats(min_value=1e-3),
       theta=floats(min_value=1e-3),
       nrows=integers(min_value=1))
def test_gamma_change_parameters(alpha, theta, nrows):
    """ Verify Gamma object can mutate by changing its parameters. """

    gamma_pdf = Gamma(alpha, theta, nrows)
    mutant = gamma_pdf.mutate(change_alpha=True, change_theta=True)
    assert 'Gamma' in str(mutant.__class__)
    assert mutant.alpha > 0
    assert mutant.theta > 0

def test_gamma_change_seed():
    """ Verify Gamma object can change its seed in mutation. """

    gamma_pdf = Gamma()
    old_seed = gamma_pdf.seed
    mutant = gamma_pdf.mutate(change_seed=True)
    assert 'Gamma' in str(mutant.__class__)
    assert mutant.seed != old_seed
