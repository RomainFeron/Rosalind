import os
from collections import defaultdict
from core import reverse_complement


def run(data_dir, output_dir):

    input_file_path = os.path.join(data_dir, 'data.txt')
    output_file_path = os.path.join(output_dir, 'output.txt')

    input_file = open(input_file_path)
    output_file = open(output_file_path, 'w')

    sequence = ''.join(line.rstrip('\n') for line in input_file.readlines() if
                       not line.startswith('>'))

    positions = defaultdict(lambda: list())

    for i in range(len(sequence)):
        for size in range(4, 13):
            if i + size < len(sequence) + 1:
                subseq_f = sequence[i:i + size]
                subseq_rc = reverse_complement(subseq_f)
                if subseq_f == subseq_rc:
                    positions[i + 1].append(size)

    for k in sorted(positions):
        for v in sorted(positions[k]):
            output_file.write(str(k) + ' ' + str(v) + '\n')
