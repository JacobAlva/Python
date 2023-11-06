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
"""

# GROUPBY
''' Makes an iterator that returns consecutive keys and groups from an iterable. '''

from itertools import groupby
"""
def less_than_3(x):
    return x < 3

a = [1, 2, 3, 4]
group_obj = groupby(a, key = less_than_3)
for key, value in group_obj:
    print(key, list(value))     # returns a grouped output of all elements in the list </> 3
# print(group_obj)
# print(key, list(value))

# using lambdas
'''Lambdas are small single-line functions having an input, perform operations & provide an output '''
# Lambdas can be used to reduce/improve the code above
group_obj_lam = groupby(a, key = lambda x: x<3)
for key, value in group_obj_lam:
    print(key, list(value))

people = [
    {"name": "John", 'age': 30},
    {"name": "Alice", "age": 25},
    {"name": "Bob", 'age': 30},
    {"name": "Jerry", "age": 25}
]

group_p = groupby(people, key=lambda x: x["age"])
for key, value in group_p:
    print(key, list(value))

#### for some reason, the above code did not group the dict entries by age, so I tried this:

# Define a custom grouping function
def group_by_age(person):
    return person["age"]

# Sort the list to ensure it's in the expected order
people.sort(key=lambda x: x["age"])

group_p = groupby(people, key=group_by_age)
for key, value in group_p:
    print(key, list(value))
"""

# INFINITE ITERATORS
from itertools import count, cycle, repeat

for i in count(5, 1):   # count(first_val, step[defaut step is 1])
    print(i)
    if (i == 30):       # break loop
        break

acyc = range(1,5)
x = 0
for i in cycle(acyc):
    print(i)
    x+=1
    if x > 30:
        break

