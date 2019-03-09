"""The RNA codon table dictates the details regarding the encoding
 of specific codons into the amino acid alphabet.

Given: An RNA string s corresponding to a strand of mRNA (of length at most 10 kbp).
Return: The protein string encoded by s."""


rna = open('rosalind_prot.txt').read()


def translator(data):
    RNA2codon_table = {
       "UUU": "F", "CUU": "L", "AUU": "I", "GUU": "V",
       "UUC": "F", "CUC": "L", "AUC": "I", "GUC": "V",
       "UUA": "L", "CUA": "L", "AUA": "I", "GUA": "V",
       "UUG": "L", "CUG": "L", "AUG": "M", "GUG": "V",
       "UCU": "S", "CCU": "P", "ACU": "T", "GCU": "A",
       "UCC": "S", "CCC": "P", "ACC": "T", "GCC": "A",
       "UCA": "S", "CCA": "P", "ACA": "T", "GCA": "A",
       "UCG": "S", "CCG": "P", "ACG": "T", "GCG": "A",
       "UAU": "Y", "CAU": "H", "AAU": "N", "GAU": "D",
       "UAC": "Y", "CAC": "H", "AAC": "N", "GAC": "D",
       "UAA":  "", "CAA": "Q", "AAA": "K", "GAA": "E",
       "UAG":  "", "CAG": "Q", "AAG": "K", "GAG": "E",
       "UGU": "C", "CGU": "R", "AGU": "S", "GGU": "G",
       "UGC": "C", "CGC": "R", "AGC": "S", "GGC": "G",
       "UGA":  "", "CGA": "R", "AGA": "R", "GGA": "G",
       "UGG": "W", "CGG": "R", "AGG": "R", "GGG": "G"
    }
    codons = []
    for i in range(0, len(data), 3):
        RNA = data[i: i + 3]
        codons.append(RNA2codon_table.get(RNA, ''))
    return ''.join(codons)

print(translator(rna))