from .resources import complement


def reverse_complement(sequence):
    return ''.join(complement[base] for base in reversed(sequence))


def open_fasta(input_file):

    input_file.readline()
    return ''.join(line.rstrip('\n') for line in input_file)


def open_fasta_multiple(input_file):

    output = {}
    header = ''
    seq = ''
    for line in input_file:
        if line.startswith('>'):
            if header != '':
                output[header] = seq
                seq = ''
            header = line[1:-1]
        else:
            seq += line[:-1]
    output[header] = seq
    return output
