""" Unit tests for the standard columns pdf's. """

from copy import deepcopy
from hypothesis import given
from hypothesis.strategies import floats, integers
from genetic_data.pdfs import Gamma, Poisson

from trivials import TrivialPDF

class TestGamma():
    """ A class containing the tests for the Gamma column pdf. """

    limits = given(alpha=floats(min_value=1e-3),
                   theta=floats(min_value=1e-3),
                   nrows=integers(min_value=1))

    @given(nrows=integers(min_value=1))
    def test_sample(self, nrows):
        """ Verify that a given Gamma object can sample correctly. """
        gamma_pdf = Gamma(nrows)
        sample = gamma_pdf.sample()
        assert sample.shape == (nrows,)
        assert sample.dtype == 'float'

    @given(nrows=integers(min_value=1))
    def test_mutation_defaults(self, nrows):
        """ Verify that .mutate() returns self by default. """
        gamma = Gamma(nrows)
        mutant = deepcopy(gamma).mutate()
        assert mutant.alpha == gamma.alpha
        assert mutant.theta == gamma.theta
        assert mutant.nrows == gamma.nrows
        assert mutant.alternative_pdfs == gamma.alternative_pdfs
        assert mutant.seed == gamma.seed

    @given(nrows=integers(min_value=1))
    def test_change_parameters(self, nrows):
        """ Verify Gamma object can mutate by changing its parameters. """
        gamma = Gamma(nrows)
        mutant = deepcopy(gamma).mutate(change_alpha=True, change_theta=True)
        assert mutant.alpha > 0
        assert mutant.alpha != gamma.alpha
        assert mutant.theta > 0
        assert mutant.theta != gamma.theta

    def test_change_pdf(self):
        """ Verify Gamma object can mutate to another kind of pdf. Here the
        TrivialPDF class is used for illustration. """
        gamma = Gamma(alternative_pdfs=[TrivialPDF])
        mutant = deepcopy(gamma).mutate(change_pdf=True)
        assert mutant != gamma
        assert 'TrivialPDF' in str(mutant.__class__)

    def test_change_seed(self):
        """ Verify Gamma object can mutate by changing its seed. """
        gamma = Gamma()
        mutant = deepcopy(gamma).mutate(change_seed=True)
        assert mutant.seed != gamma.seed


class TestPoisson():
    """ A class containing the tests for the Poisson column pdf. """

    limits = given(mu=floats(min_value=1e-3, max_value=1e12),
                   nrows=integers(min_value=1))

    @given(nrows=integers(min_value=1))
    def test_sample(self, nrows):
        """ Verify that a given Poisson object can sample correctly. """
        poisson = Poisson(nrows)
        sample = poisson.sample()
        assert sample.shape == (nrows,)
        assert sample.dtype == 'int'

    @given(nrows=integers(min_value=1))
    def test_mutation_defaults(self, nrows):
        """ Verify .mutate() returns self by default. """
        poisson = Poisson(nrows)
        mutant = deepcopy(poisson).mutate()
        assert mutant.mu == poisson.mu
        assert mutant.nrows == poisson.nrows
        assert mutant.alternative_pdfs == poisson.alternative_pdfs
        assert mutant.seed == poisson.seed

    @given(nrows=integers(min_value=1))
    def test_change_parameter(self, nrows):
        """ Verify Poisson object can mutate by changing its parameter. """
        poisson = Poisson(nrows)
        mutant = deepcopy(poisson).mutate(change_mu=True)
        assert mutant.mu > 0
        assert mutant.mu != poisson.mu

    def test_change_pdf(self):
        """ Verify Poisson object can mutate to another kind of pdf. Here the
        TrivialPDF class is used for illustration. """
        poisson = Poisson(alternative_pdfs=[TrivialPDF])
        mutant = poisson.mutate(change_pdf=True)
        assert 'TrivialPDF' in str(mutant.__class__)

    def test_change_seed(self):
        """ Verify Poisson object can mutate by changing its seed. """
        poisson = Poisson()
        mutant = deepcopy(poisson).mutate(change_seed=True)
        assert mutant.seed != poisson.seed
