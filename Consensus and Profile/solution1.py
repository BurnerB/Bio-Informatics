"""

Given: A collection of at most 10 DNA strings of equal length (at most 1 kbp) in FASTA format.

Return: A consensus string and profile matrix for the collection. 
(If several possible consensus strings exist, then you may return any one of them.)

"""

from Bio import SeqIO
from collections import Counter

def main(fasta_file):
    with open(fasta_file) as fh:
        dna_strings = [str(fasta.seq) for fasta in SeqIO.parse(fh, 'fasta')]
        transposed = zip(*dna_strings)
        counters = [Counter(column) for column in transposed]

        # create consensus
        consensus = ''.join([counter.most_common(1)[0][0] for counter in counters])
        return consensus

        # create profile matrix
        matrix = ''
        for base in 'ACGT':
            matrix += '{}:'.format(base)
            for counter in counters:
                matrix += ' {}'.format(counter[base])
            matrix += '\n'
        matrix = matrix.rstrip()
        return matrix

print(main("rosalind_cons.txt"))