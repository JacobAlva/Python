# itertools: product, permutations, combinations, accumulate, groupby, and infinite iterators

# collection of tools for handling iterators. They are datatypes that can be used in a for loop.
# iterators are datatypes that can be used in a for loop. Most common is a list.
# Itertools offers some advanced iterator tools 

"""
# PRODUCT
from itertools import product
a = [1,2]
b = [3]
prod = product(a,b)     # returns a unique combination of all elements 
prod = product(a,b, repeat = 2)     # product with repitition # times
print(list(prod))       


E PERMUTATIONS
from itertools import permutations
# returns all possible orderings of an input
a = [1,2,3,4]
perm = permutations(a)
print(perm)         # this retunrs an object from the library. Use an iterable (e.g. list to print out the output
# print(list(perm), len(list(perm)))

''' 
It is important to note that the permutations function returns an iterator, and when you convert it to a list using list(perm), it's exhausted. As a result, when you try to get the length using len(list(perm)), it returns 0 because the iterator has already been consumed. To get the correct length, you should store the permutations in a list before converting them to a list. Here's the corrected code:
'''
perm_list = list(perm)
print(list(perm_list), len(perm_list))

# to specify the length of the permutations
perm1 = permutations(a, 2)
p1L = list(perm1)
print(p1L, len(p1L))



# COMBINATIONS
from itertools import combinations, combinations_with_replacement, permutations
# returns all possible combinations of an iterable with a specified length

a = range(4, 12, 2)
comb = combinations(a, 2)   # range(start, stop, step). A range is also an iterable
print(a)
print(list(comb))

comb_wr = combinations_with_replacement(a, 2)
print(list(comb_wr))

# comparing perm, comb & comb_wr
perm = permutations(a, 2)
print(list(perm))
''' Notice the differences between all three. Similar but different'''
"""


# ACCUMULATE
''' The accumulate fxn makes an iterator that returns accumulated sums or any other binary fxn provided as input'''

from itertools import accumulate

a = range(1,5)
b = [i for i in a]      # comprehension
#b.insert(0, (1,1))
c = b[:1] + [1] + b[1:]   # splice and concat multiple lists
print(c)
acc = accumulate(c)
print(list(a))
print(list(acc))
print(b)

import operator     # for mathematical operations
acc2 = accumulate(c, func = operator.mul)       # returns an accumulated multiplication of each element
print(list(acc2))

d = [1,4,3,5,2]
acc3 = list(accumulate(d, func=max))      # compares each element and returns the max
print(d)
print(acc3)
print(acc3[-1])     # returns the highest element in the list

