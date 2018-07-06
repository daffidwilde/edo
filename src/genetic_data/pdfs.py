""" Default column probability density functions for the genetic algorithm. """

import random

from scipy.stats import gamma, poisson

import numpy as np

class Gamma(object):
    """ Continuous column pdf given by the gamma distribution. """

    def __init__(self, alpha=1, theta=1, nrows=1, alternative_pdfs=None):
        """ Initialisation. """

        self.alpha = alpha
        self.theta = theta
        self.nrows = nrows
        self.alternative_pdfs = alternative_pdfs
        self.seed = random.randint(0, 1000000)

    def sample(self):
        """ Take a sample of size `nrows` from the gamma distribution with
        parameters `alpha` and `theta`. Seeded for reproducibility. """

        np.random.seed(self.seed)
        return gamma.rvs(a=self.alpha, scale=self.theta, size=self.nrows)

    def mutate(self, change_pdf=False, change_alpha=False,
               change_theta=False, change_seed=False):
        """ Mutation of the column. This is either changing to another pdf all
        together, or a change in the current parameters.

        Parameters
        ----------
        change_pdf : bool
            Change to another pdf. If so, no parameter mutation necessary.
        change_alpha : bool
            Mutate value of alpha, i.e. the shape of the distribution.
        change_theta : bool
            Mutate the value of theta, i.e. the scale of the distribution.
        change_seed : bool
            Mutate the current seed for sampling the actual dataset.

        Returns
        -------
        self : object
            A mutated Gamma object.
        """

        if change_pdf and self.alternative_pdfs:
            self = random.choice(self.alternative_pdfs)
            return self
        if change_alpha:
            old_alpha = self.alpha
            self.alpha = random.uniform(0, 100)
            while self.alpha in [0, old_alpha]:
                self.alpha = random.uniform(0, 100)
        if change_theta:
            old_theta = self.theta
            self.theta = random.uniform(0, 100)
            while self.theta in [0, old_theta]:
                self.theta = random.uniform(0, 100)
        if change_seed:
            old_seed = self.seed
            self.seed = random.randint(0, 1000000)
            while self.seed == old_seed:
                self.seed = random.randint(0, 1000000)
        return self

class Poisson(object):
    """ Discrete column pdf given by the Poisson distribution. """

    def __init__(self, mu=1, nrows=1, alternative_pdfs=None):
        """ Initialisation. """

        self.mu = mu
        self.nrows = nrows
        self.alternative_pdfs = alternative_pdfs
        self.seed = random.randint(0, 1000000)

    def sample(self):
        """ Take a sample of size `nrows` from the Poisson distribution with
        parameter `mu`. Seeded for reproducibility. """

        np.random.seed(self.seed)
        return poisson.rvs(self.mu, size=self.nrows)

    def mutate(self, change_pdf=False, change_mu=False, change_seed=False):
        """ Mutation of the column. This is either changing to another pdf all
        together, or a change in the current parameter.

        Parameters
        ----------
        change_pdf : bool
            Change to another pdf. If so, no parameter mutation necessary.
        change_mu : bool
            Mutate the value of mu, i.e. the mean of the distribution.
        change_seed : bool
            Mutate the current seed for sampling the actual dataset.

        Returns
        -------
        self : object
            A mutated Gamma object.
        """

        if change_pdf and self.alternative_pdfs:
            self = random.choice(self.alternative_pdfs)
            return self
        if change_mu:
            old_mu = self.mu
            self.mu = random.uniform(0, 100)
            while self.mu == old_mu:
                self.mu = random.uniform(0, 100)
        if change_seed:
            old_seed = self.seed
            self.seed = random.randint(0, 1000000)
            while self.seed == old_seed:
                self.seed = random.randint(0, 1000000)

        return self
