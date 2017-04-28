import os
import requests


def run(data_dir, output_dir):

    input_file_path = os.path.join(data_dir, 'data.txt')
    output_file_path = os.path.join(output_dir, 'output.txt')

    input_file = open(input_file_path)
    output_file = open(output_file_path, 'w')

    uniprot_url = 'http://www.uniprot.org/uniprot/'

    protein_ids = tuple(line.rstrip('\n') for line in input_file)

    for protein_id in protein_ids:

        url = uniprot_url + protein_id + '.fasta'
        uniprot_response = requests.get(url)

        if uniprot_response.status_code != 200:
            print('Error: there was a problem accessing data for' +
                  ' uniprot ID ' + protein_id + '.')
            return
        else:
            uniprot_entry = uniprot_response.content.decode('utf-8')

        sequence = ''.join(line.rstrip('\n') for
                           line in uniprot_entry.split('\n')[1:])

        positions = tuple(i for i in range(len(sequence) - 3)
                          if sequence[i] is 'N' and
                          sequence[i + 1] is not 'P' and
                          sequence[i + 2] in ['S', 'T'] and
                          sequence[i + 3] is not 'P')

        if positions:
            output_file.write(protein_id + '\n')
            for i, position in enumerate(positions):
                output_file.write(str(position + 1))
                if i == len(positions) - 1:
                    output_file.write('\n')
                else:
                    output_file.write('\t')

