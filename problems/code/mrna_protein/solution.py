import os
from core.resources import prot_alphabet


def run(data_dir, output_dir):

    input_file_path = os.path.join(data_dir, 'data.txt')
    output_file_path = os.path.join(output_dir, 'output.txt')

    input_file = open(input_file_path)
    output_file = open(output_file_path, 'w')

    protein_seq = input_file.readline().replace('\n', 'X')
    n_rna_seq = 1

    for aa in protein_seq:
        n_rna_seq *= len(prot_alphabet[aa])

    output_file.write(str(n_rna_seq % 1000000))
