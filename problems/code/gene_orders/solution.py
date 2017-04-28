import os
import itertools
from math import factorial


def run(data_dir, output_dir):

    input_file_path = os.path.join(data_dir, 'data.txt')
    output_file_path = os.path.join(output_dir, 'output.txt')

    input_file = open(input_file_path)
    output_file = open(output_file_path, 'w')

    n = int(input_file.readline().rstrip('\n'))
    numbers = range(1, n + 1)

    output_file.write(str(factorial(n)) + '\n')

    for permutation in itertools.permutations(numbers):
        output_file.write('\t'.join(str(p) for p in permutation) + '\n')
