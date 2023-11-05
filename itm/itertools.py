# itertools: product, permutations, combinations, accumulate, groupby, and infinite iterators

# collection of tools for handling iterators. They are datatypes that can be used in a for loop.
# iterators are datatypes that can be used in a for loop. Most common is a list.
# Itertools offers some advanced iterator tools 

"""
from itertools import product
a = [1,2]
b = [3]
prod = product(a,b)     # returns a unique combination of all elements 
prod = product(a,b, repeat = 2)     # product with repitition # times
print(list(prod))       
"""

from itertools import permutations
# returns all possible orderings of an input
a = [1,2,3]
perm = permutations(a)
print(perm)         # this retunrs an object from the library. Use an iterable (e.g. list to print out the output
print(list(perm), len(list(perm)))

