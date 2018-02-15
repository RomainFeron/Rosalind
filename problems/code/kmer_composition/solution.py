import os
from core import open_fasta, ordered_kmers
from collections import OrderedDict


def run(data_dir, output_dir):

    input_file_path = os.path.join(data_dir, 'data.txt')
    output_file_path = os.path.join(output_dir, 'output.txt')

    input_file = open(input_file_path)
    output_file = open(output_file_path, 'w')

    sequence = open_fasta(input_file)
    kmers = ordered_kmers(4)

    kmers_count = OrderedDict.fromkeys(kmers, 0)

    for i in range(len(sequence) - 3):
        kmers_count[sequence[i:i + 4]] += 1

    output_file.write(' '.join([str(v) for v in kmers_count.values()]))
