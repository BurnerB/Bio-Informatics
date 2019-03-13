"""

For a given collection of sequences in FASTA-format, we are given the task to print the adjacency list of the overlap graph of the sequences with the overlap length of 3 bp.
To do this, we need to compare the suffixes of all the sequences to the prefixes.
When a match is found the ID of the two sequences should be printed (the ID of the sequence containing the suffix should be printed on the left and the other one should be printed on the right).
To avoid directed loops in the overlap graph, we should not print any sequences that have a suffix that matches its own prefix.



Given: A collection of DNA strings in FASTA format having total length at most 10 kbp.

Return: The adjacency list corresponding to O3. You may return edges in any order.
"""

from Bio import SeqIO                                                  
prefixes = []                                                          
suffixes = []                                                          
handle = open('rosalind_grph.txt', 'r')                                 

for record in SeqIO.parse(handle, 'fasta'):                            
    count1 = 0                                                         
    count2 = 0                                                         
    prefix = [record.id]                                               
    suffix = [record.id]                                               
    pre = ''                                                           
    suf = ''                                                           
    for nt in record.seq:                                              
        if count1 < 3:                                                 
            pre += nt                                                  
            count1 += 1                                                
    prefix.append(pre)                                                 
    for tn in reversed(record.seq):                                    
        if count2 < 3:                                                 
            suf += tn                                                  
            count2 += 1                                                
    suffix.append(''.join(reversed(suf)))                              
    prefixes.append(prefix)                                            
    suffixes.append(suffix)                                                                                                    
                                                                       
for i, k in enumerate(suffixes):                                       
    currentsf = suffixes[i][1]                                         
    currentid = suffixes[i][0]                                         
    for j, l in enumerate(prefixes):                                   
        if currentsf == prefixes[j][1] and currentid != prefixes[j][0]:
            print(currentid, prefixes[j][0])