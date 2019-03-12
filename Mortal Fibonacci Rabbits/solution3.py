"""

Given: Positive integers n≤100 and m≤20.
Return: The total number of pairs of rabbits that will remain after the n-th month if all rabbits live for m months.

"""

def mortal_sungura(n,k=1):
  ages = [1] + [0]*(k-1)
  for i in range(n-1):
    ages = [sum(ages[1:])] + ages[:-1]
  return sum(ages)

print(mortal_sungura(91, 19))


"""

The key is that the ages array maintains a count of the rabbit pairs of different age. 
The first element is count of rabbits that are one month old, second element two months old and so on. 
There are k elements in that array, corresponding to the maximum number of months the rabbits can live.

The line from the for loop will calculate the number of newborns: 
sum(ages[1:]) - each rabbit pair will have a newborn except the ones that are newborns themselves,
that's why the first element in excluded from the sum: ages[1:]. 
The result will become the first element in the list and the rest of the list will be the rabbits advancing in age with one month
(the oldest ones dying, hence the ages[:-1] which excludes the last entry).
Best thing is to do a small example on paper with k of about 4, 5.

"""
