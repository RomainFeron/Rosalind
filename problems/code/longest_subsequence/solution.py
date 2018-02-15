import os
import math


def run(data_dir, output_dir):

    input_file_path = os.path.join(data_dir, 'data_big.txt')
    output_file_path = os.path.join(output_dir, 'output.txt')

    input_file = open(input_file_path)
    output_file = open(output_file_path, 'w')

    n = int(input_file.readline()[:-1])
    permutation = tuple(int(p) for p in input_file.readline()[:-1].split(' '))

    # Honestly i had to google this and i'm still not understanding the algorithm fully
    P = [0] * n
    M = [0] * (n + 1)
    L = 0

    for i in range(n):
        low_bound = 1
        high_bound = L
        while low_bound <= high_bound:
            middle = math.ceil((low_bound + high_bound) / 2)
            if permutation[M[middle]] < permutation[i]:
                low_bound = middle + 1
            else:
                high_bound = middle - 1

        new_L = low_bound
        P[i] = M[new_L - 1]
        M[new_L] = i

        if new_L > L:
            L = new_L
    S = [0] * L
    k = M[L]
    for i in range(L - 1, -1, -1):
        S[i] = permutation[k]
        k = P[k]

    output_file.write(' '.join(str(i) for i in S) + '\n')

    P = [0] * n
    M = [0] * (n + 1)
    L = 0

    for i in range(n):
        low_bound = 1
        high_bound = L
        while low_bound <= high_bound:
            middle = math.ceil((low_bound + high_bound) / 2)
            if permutation[M[middle]] > permutation[i]:
                low_bound = middle + 1
            else:
                high_bound = middle - 1

        new_L = low_bound
        P[i] = M[new_L - 1]
        M[new_L] = i

        if new_L > L:
            L = new_L
    S = [0] * L
    k = M[L]
    for i in range(L - 1, -1, -1):
        S[i] = permutation[k]
        k = P[k]

    output_file.write(' '.join(str(i) for i in S) + '\n')
