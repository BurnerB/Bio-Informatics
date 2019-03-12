"""Given: Positive integers n≤40 and k≤5
Return: The total number of rabbit pairs that will be present after n
months, if we begin with 1 pair and in each generation, every pair of 
reproduction-age rabbits produces a litter of k rabbit pairs (instead of only 1 pair)."""

"""Problem:
Given: Positive integers n≤40 and k≤5.
Return: The total number of rabbit pairs that will be present after n months if we begin with 1 pair and in each generation, every pair of reproduction-age rabbits produces a litter of k rabbit pairs (instead of only 1 pair)."""

from functools import lru_cache
#least recently used cache decorator
@lru_cache(maxsize=1000)
def sungura(n, k):
    if n == 0:
        return 0
    if n == 1:
       return 1
    else:
       return sungura(n-1, k) + k*sungura(n-2, k)

print(sungura(34, 2))
