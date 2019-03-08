"""The GC-content of a DNA string is given by the percentage of symbols in the string that are 'C' or 'G'. For example, the GC-content of "AGCTATAG" is 37.5%.
    Note that the reverse complement of any DNA string has the same GC-content.
    DNA strings must be labeled when they are consolidated into a database.
    A commonly used method of string labeling is called FASTA format. In this format, the string is introduced by a line that begins with '>', followed by some labeling information. 
    Subsequent lines contain the string itself; the first line to begin with '>' indicates the label of the next string.
    In Rosalind's implementation, a string in FASTA format will be labeled by the ID "Rosalind_xxxx", where "xxxx" denotes a four-digit code between 0000 and 9999."""


"""Given: At most 10 DNA strings in FASTA format (of length at most 1 kbp each).
    Return: The ID of the string having the highest GC-content, followed by the GC-content of that string."""


"""Parse FASTA to dictionary,using sequence Id as key and gene sequence as value"""
def read_fasta(dataset):
        name, sequence = None, []
        for line in dataset:
            line = line.rstrip()
            if line.startswith(">"):
                if name: 
                    yield (name, ''.join(sequence))
                name, sequence = line, []
            else:
                sequence.append(line)
        if name: 
            yield (name, ''.join(sequence))
            
        
        


" Calculate GC content for each sequence"
def gc_content(dataset):
    all_GC = {}
    for key, value in dataset.items():
        GC = 0
        total = len(value)
        # print(total)
        for n in value:
            if n == "G":
                GC+=1
            elif n == "C":
                GC+=1
        # print(GC)
        content = GC/total *100
        dna = {key:content}
        all_GC.update(dna)
    # print(all_GC)

    max_key = max(zip(all_GC.keys(), all_GC.values()))
    return max_key

with open('rosalind_gc.txt') as data:
    for name, sequence in read_fasta(data):
        fasta = {name: sequence}
        # print(fasta)
        result = gc_content(fasta)
        print(result)