"""

Given: Positive integers n≤100 and m≤20.
Return: The total number of pairs of rabbits that will remain after the n-th month if all rabbits live for m months.

"""

from functools import lru_cache
#least recently used cache decorator
@lru_cache(maxsize=1000)
def mortal_sungura(n, m):
    if n == 1:
        return 1
    if n == 2:
       return 1
    elif n <= m:
        return mortal_sungura(n-1, m) + mortal_sungura(n-2, m)
    elif n == m+1:
        return mortal_sungura(n-1, m) + mortal_sungura(n-2, m)-1
    else:
       return mortal_sungura(n-1, m) + mortal_sungura(n-2, m) - mortal_sungura(n- (m+1),m)


print(mortal_sungura(91, 19))