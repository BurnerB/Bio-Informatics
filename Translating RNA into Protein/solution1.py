"""The RNA codon table dictates the details regarding the encoding
 of specific codons into the amino acid alphabet.

Given: An RNA string s corresponding to a strand of mRNA (of length at most 10 kbp).
Return: The protein string encoded by s."""

from Bio.Seq import Seq
from Bio.Alphabet import IUPAC

rna = open('rosalind_prot.txt').read()




def translator(data):
    rna = str(data)
    rna = Seq(rna, IUPAC.unambiguous_rna)
    return str(rna.translate(to_stop=True))


print(translator(rna))