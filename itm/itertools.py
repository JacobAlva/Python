# itertools: product, permutations, combinations, accumulate, groupby, and infinite iterators

# collection of tools for handling iterators. They are datatypes that can be used in a for loop.
# iterators are datatypes that can be used in a for loop. Most common is a list.
# Itertools offers some advanced iterator tools 

from itertools import product
a = [1,2]
b = [3]
prod = product(a,b)     # returns a unique combination of all elements 
prod = product(a,b, repeat = 2)     # product with repitition # times
print(list(prod))       


