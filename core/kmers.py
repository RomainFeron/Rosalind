import itertools


def ordered_kmers(n):

    alphabet = ['A', 'T', 'G', 'C']
    ordered_kmers = sorted([''.join([c for c in p]) for p in
                           itertools.product(alphabet, repeat=4)])

    return ordered_kmers
