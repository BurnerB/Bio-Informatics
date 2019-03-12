"""Given: Positive integers n≤40 and k≤5
Return: The total number of rabbit pairs that will be present after n
months, if we begin with 1 pair and in each generation, every pair of 
reproduction-age rabbits produces a litter of k rabbit pairs (instead of only 1 pair)."""

"""Problem:
Given: Positive integers n≤40 and k≤5.
Return: The total number of rabbit pairs that will be present after n months if we begin with 1 pair and in each generation, every pair of reproduction-age rabbits produces a litter of k rabbit pairs (instead of only 1 pair)."""

sungura_cache = {}

def sungura(n, k):
    #if we have cached the value,then return it
    if n in sungura_cache:
        return sungura_cache[n]

    #compute nth term
    if n == 1:
        answer = 1
    elif n == 2:
        answer = 1
    elif n > 2:
        return sungura(n-1, k) + k*sungura(n-2, k)

    #cache the value and return it
    sungura_cache[n] = answer
    return answer

print(sungura(34, 2))