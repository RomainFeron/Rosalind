from resources import amino_acid


def dna_to_protein(sequence):

    for i in range(0, len(sequence) - 3, 3):
        print(i, sequence[i:i + 3], amino_acid[sequence[i:i + 3]])

    return(''.join(amino_acid[sequence[i:i + 3]] for
           i in range(0, len(sequence) - 3, 3)))


print(dna_to_protein('GGGATGACCCCGCGACTTGGATTAGAGTCTCTTTTGGAATAA'))
