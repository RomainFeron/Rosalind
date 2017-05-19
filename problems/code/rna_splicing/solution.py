import os
from core import dna_to_protein


def run(data_dir, output_dir):

    input_file_path = os.path.join(data_dir, 'data.txt')
    output_file_path = os.path.join(output_dir, 'output.txt')

    input_file = open(input_file_path)
    output_file = open(output_file_path, 'w')

    data = input_file.readlines()

    sequence = ''
    i = 1
    while not data[i].startswith('>'):
        sequence += data[i].rstrip('\n')
        i += 1

    introns = [line[:-1] for line in data[i:] if not line.startswith('>')]

    exons = sequence
    for intron in introns:
        exons = exons.replace(intron, '')

    output_file.write(dna_to_protein(exons).rstrip('X'))
