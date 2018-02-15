import os
from core import open_fasta_multiple
from math import ceil
from collections import defaultdict


def run(data_dir, output_dir):

    input_file_path = os.path.join(data_dir, 'data.txt')
    output_file_path = os.path.join(output_dir, 'output.txt')

    input_file = open(input_file_path)
    output_file = open(output_file_path, 'w')

    data = open_fasta_multiple(input_file)
    sequences = list(data.values())
    chromosome = ''

    kmers = defaultdict(lambda: list())
    kmers_end = defaultdict(lambda: list())
    k = ceil(min([len(sequence) for sequence in sequences]) / 2)

    for sequence in sequences:
        for i in range(0, len(sequence) - k + 1):
            current_kmer = sequence[i:i + k]
            kmers[current_kmer[:k - 1]].append(current_kmer)
            kmers_end[current_kmer[1 - k:]].append(current_kmer)

    lonely = [kmers[kmer][0] for kmer in kmers.keys() if len(kmers[kmer]) == 1]

    for kmer in lonely:
        if kmer[:k - 1] not in kmers_end.keys():
            chromosome += kmer
            current_kmer = kmer

    while True:
        anchor = current_kmer[1 - k:]
        if anchor not in kmers.keys():
            break
        else:
            current_kmer = kmers[anchor][0]
            chromosome += current_kmer[-1]

    output_file.write(chromosome)
