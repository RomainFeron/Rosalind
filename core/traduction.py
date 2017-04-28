from .resources import amino_acid


def dna_to_rna(sequence):

    return(sequence.replace('T', 'U'))


def rna_to_dna(sequence):

    return(sequence.replace('U', 'T'))


def dna_to_protein(sequence):

    return(''.join(amino_acid[sequence[i:i + 3]] for
           i in range(0, len(sequence), 3)))
