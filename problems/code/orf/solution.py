import os
from core.resources import amino_acid
from core import dna_to_protein, reverse_complement, open_fasta


def get_sequences(sequence):

    proteins = set()

    for pos in range(len(sequence) - 3):
        codon = sequence[pos:pos + 3]
        if amino_acid[codon] is 'M':
            prot = codon
            pos_t = pos
            while True:
                pos_t += 3
                if pos_t + 3 > len(sequence):
                    break
                codon = sequence[pos_t:pos_t + 3]
                if amino_acid[codon] is 'X':
                    proteins.add(dna_to_protein(prot))
                    break
                prot += codon

    return(proteins)


def run(data_dir, output_dir):

    input_file_path = os.path.join(data_dir, 'data.txt')
    output_file_path = os.path.join(output_dir, 'output.txt')

    input_file = open(input_file_path)
    output_file = open(output_file_path, 'w')

    sequence = open_fasta(input_file)

    proteins = get_sequences(sequence)
    proteins = proteins.union(get_sequences(reverse_complement(sequence)))

    for protein in proteins:
        output_file.write(protein + '\n')
