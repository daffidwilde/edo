""" Unit tests for the standard columns pdf's. """

from copy import deepcopy
from hypothesis import given, settings
from hypothesis.strategies import floats, integers
from genetic_data.pdfs import Gamma, Poisson

from trivials import TrivialPDF

class TestGamma():
    """ A class containing the tests for the Gamma column pdf. """

    limits = given(alpha=floats(min_value=1e-3),
                   theta=floats(min_value=1e-3),
                   nrows=integers(min_value=1))

    @limits
    @settings(deadline=1000)
    def test_sample(self, alpha, theta, nrows):
        """ Verify that a given Gamma object can sample correctly. """
        gamma_pdf = Gamma(alpha, theta, nrows)
        sample = gamma_pdf.sample()
        assert sample.shape == (nrows,)
        assert sample.dtype == 'float'

    @limits
    @settings(deadline=1000)
    def test_mutation_defaults(self, alpha, theta, nrows):
        """ Verify that .mutate() returns self by default. """
        gamma = Gamma(alpha, theta, nrows)
        mutant = deepcopy(gamma).mutate()
        assert mutant.alpha == gamma.alpha
        assert mutant.theta == gamma.theta
        assert mutant.nrows == gamma.nrows
        assert mutant.alternative_pdfs == gamma.alternative_pdfs
        assert mutant.seed == gamma.seed

    @limits
    @settings(deadline=1000)
    def test_change_parameters(self, alpha, theta, nrows):
        """ Verify Gamma object can mutate by changing its parameters. """
        gamma = Gamma(alpha, theta, nrows)
        mutant = deepcopy(gamma).mutate(change_alpha=True, change_theta=True)
        assert mutant.alpha > 0
        assert mutant.alpha != gamma.alpha
        assert mutant.theta > 0
        assert mutant.theta != gamma.theta

    def test_change_pdf(self):
        """ Verify Gamma object can mutate to another kind of pdf. Here the
        TrivialPDF class is used for illustration. """
        gamma = Gamma(alternative_pdfs=[TrivialPDF()])
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

    @limits
    @settings(deadline=1000)
    def test_sample(self, mu, nrows):
        """ Verify that a given Poisson object can sample correctly. """
        poisson = Poisson(mu, nrows)
        sample = poisson.sample()
        assert sample.shape == (nrows,)
        assert sample.dtype == 'int'

    @limits
    @settings(deadline=1000)
    def test_mutation_defaults(self, mu, nrows):
        """ Verify .mutate() returns self by default. """
        poisson = Poisson(mu, nrows)
        mutant = deepcopy(poisson).mutate()
        assert mutant.mu == poisson.mu
        assert mutant.nrows == poisson.nrows
        assert mutant.alternative_pdfs == poisson.alternative_pdfs
        assert mutant.seed == poisson.seed

    @limits
    @settings(deadline=1000)
    def test_change_parameter(self, mu, nrows):
        """ Verify Poisson object can mutate by changing its parameter. """
        poisson = Poisson(mu, nrows)
        mutant = deepcopy(poisson).mutate(change_mu=True)
        assert mutant.mu > 0
        assert mutant.mu != poisson.mu

    def test_change_pdf(self):
        """ Verify Poisson object can mutate to another kind of pdf. Here the
        TrivialPDF class is used for illustration. """
        poisson = Poisson(alternative_pdfs=[TrivialPDF()])
        mutant = poisson.mutate(change_pdf=True)
        assert 'TrivialPDF' in str(mutant.__class__)

    def test_change_seed(self):
        """ Verify Poisson object can mutate by changing its seed. """
        poisson = Poisson()
        mutant = deepcopy(poisson).mutate(change_seed=True)
        assert mutant.seed != poisson.seed
