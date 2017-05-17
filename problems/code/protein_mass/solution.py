import os
from core.resources import prot_mass_table


def run(data_dir, output_dir):

    input_file_path = os.path.join(data_dir, 'data.txt')
    output_file_path = os.path.join(output_dir, 'output.txt')

    input_file = open(input_file_path)
    output_file = open(output_file_path, 'w')

    sequence = ''.join(line.rstrip('\n') for line in input_file.readline())

    weight = round(sum((prot_mass_table[aa] for aa in sequence)), 3)
    print(weight)
