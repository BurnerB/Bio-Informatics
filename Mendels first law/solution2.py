"""Given: Three positive integers k, m, and n, 
representing a population containing k+m+n organisms: k individuals are homozygous dominant for a factor, m are heterozygous, and n
are homozygous recessive.

Return: The probability that two randomly selected mating organisms will produce an individual possessing a dominant allele
 (and thus displaying the dominant phenotype). Assume that any two organisms can mate."""


def firstLaw(k,m,n):
    N = float(k+m+n)
    return(1 - 1/N/(N-1)*(n*(n-1) + n*m + m*(m-1)/4.))

print(firstLaw(24 ,27 ,19))