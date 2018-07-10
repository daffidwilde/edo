""" Default crossover and mutation operators for a genetic algorithm. """

import random

def crossover(parent1, parent2, prob=0.5):
    """ Select alleles from `parent1` with probability `prob`. Otherwise select
    from `parent2`. Collate alleles to form a new individual or offspring. """

    weights = [prob, 1-prob]
    nrows = random.choices([parent1[0], parent2[0]], weights)[0]
    ncols = random.choices([parent1[1], parent2[1]], weights)[0]

    longest_parent = sorted([parent1, parent2], key=len, reverse=True)[0]

    cols = []
    for i in range(ncols):
        if i < min(parent1[1], parent2[1]):
            col = random.choices([parent1[i+2], parent2[i+2]], weights)[0]
        else:
            col = longest_parent[i+2]
        cols.append(col)

    offspring = tuple([nrows, ncols, *cols])
    return offspring

def mutate_individual(individual, prob, row_limits, col_limits, pdfs, weights):
    """ Mutate an individual's allele representation. Alleles are split into
    three parts: number of rows, number of columns, and the column
    distributions. Each of these parts is mutated with a different """

    if row_limits[0] > row_limits[1]:
        row_limits = row_limits[::-1]
    if col_limits[0] > col_limits[1]:
        col_limits = col_limits[::-1]

    mutant = list(individual[:2])

    if random.random() < prob:
        mutant[0] = random.randint(*row_limits)
    if random.random() < prob:
        mutant[1] = random.randint(*col_limits)

    cols = []
    for col in individual[2: min(mutant[1], individual[1])+1]:
        col.nrows = mutant[0]
        cols.append(col)
    mutant += cols

    spare_cols = mutant[1] - len(mutant[2:])
    if spare_cols > 0:
        pdfs = [pdf(mutant[0]) for pdf in pdfs]
        mutant += random.choices(pdfs, weights, k=spare_cols)

    for col in mutant[2:]:
        number_attrs = len(col.get_params()) + 2
        changes = [random.random() < prob for _ in range(number_attrs)]
        col.mutate(*changes)

    return tuple(mutant)
