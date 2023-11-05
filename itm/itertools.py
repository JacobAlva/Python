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
a = [1,2,3,4]
perm = permutations(a)
print(perm)         # this retunrs an object from the library. Use an iterable (e.g. list to print out the output
# print(list(perm), len(list(perm)))

""" 
It is important to note that the permutations function returns an iterator, and when you convert it to a list using list(perm), it's exhausted. As a result, when you try to get the length using len(list(perm)), it returns 0 because the iterator has already been consumed. To get the correct length, you should store the permutations in a list before converting them to a list. Here's the corrected code:
"""
perm_list = list(perm)
print(list(perm_list), len(perm_list))

# to specify the length of the permutations
perm1 = permutations(a, 2)
p1L = list(perm1)
print(p1L, len(p1L))

