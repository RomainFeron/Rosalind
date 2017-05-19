import os
import itertools


def run(data_dir, output_dir):

    input_file_path = os.path.join(data_dir, 'data.txt')
    output_file_path = os.path.join(output_dir, 'output.txt')

    input_file = open(input_file_path)
    output_file = open(output_file_path, 'w')

    alphabet = tuple(input_file.readline()[:-1].split(' '))
    kmer_size = int(input_file.readline()[:-1])

    for group in itertools.product(alphabet, repeat=kmer_size):
        output_file.write(''.join(group) + '\n')
