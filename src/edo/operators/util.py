""" A collection of functions for use across several operators. """


def get_family_counts(metadata, families):
    """ Get the number of instances in `metadata` that belong to each family in
    `families`. """

    return {
        family: sum([pdf.name == family.name for pdf in metadata])
        for family in families
    }
