'''
    Generators are functions that return an object that can be iterated over. The generate the item inside the object lazily i.e. they generate only one at a time and only when you ask for it making them more memory efficient when dealing with large data sets. They are defined like normal functions but with a yield keyword instead of the return
'''

import sys

def mygenerator():
    yield 11
    yield 2
    yield 3
    #return 5

g = mygenerator()

"""
# loop through the generator
#for i in g:
 #   print(i)

value = next(g)     # prints the first yield statement
print(value)

value = next(g)     
print(value)

value = next(g)     
print(value)

''' A generator will raise a StopIteration error if it doesn't reach another yield statement. .'''
value = next(g)     
print(value)

# gen as input to other functions that takee iterables
#print(sum(g))
print(sorted(g))       # returns a new list with the items of the generator in a sorted order.
print(g)


# Understanding the execution of a generator

def countdown(num):
    print('Starting...')
    while num > 0:
        yield num
        num -= 1

cd = countdown(4)

value = next(cd)
print(value)

print(next(cd))
print(next(cd))
print(next(cd))
print(next(cd))     # returns a StopIteration error
"""

# Application of generators

"""
def firstn(n):
    nums = []
    num = 0
    while num < n:
        nums.append(num)
        num += 1
    return nums

def firstn_generator(n):    # more memory efficient as it doesn't require the list
    num = 0
    while num < n:
        yield num
        num += 1

print(sum(firstn(10)))
#fn = firstn_generator(10)
#print(sum((fn)))
print(sum(firstn_generator(10)))
print(sum(range(1,10))) # testing

# testing the size & memory efficiency of the two methods
print(sys.getsizeof(firstn(1000)))
print(sys.getsizeof(firstn_generator(1000)))

''' another advantage of generators is that you do not have to wait for all the values to be generated before you start to use them.'''


# Fibonacci sequence with Generators

def fibonacci(limit):
    # 0 1 1 2 3 5 8 13...
    a, b = 0, 1
    while a < limit:
        yield a
        a, b = b, a+b

fib = fibonacci(30)
#print(next(fib))
for i in fib:
    print(i)
"""


# generator comprehension

generator1 = (i for i in range(10000) if i % 2 == 0)
#for i in generator1:
#    print(i)
print(type(generator1))
#print(list(generator1))                # converting generator to list
print(sys.getsizeof(generator1))


mylist = [i for i in range(10000) if i % 2 == 0]        # list comprehension
#print(mylist)
print(sys.getsizeof(mylist))


#NOTE
'''
    It is important to note that the sys.getsizeof() returns the size of the generator object itself, not the size of all items it can generate. This is why it shows a much smaller size compared to the list, which generates a complete list in memory.

        print(sys.getsizeof(firstn(1000000)))               # This gives the size of the entire list in memory.
        print(sys.getsizeof(firstn_generator(1000000)))     # This gives the size of the generator object itself.

    To illustrate the memory efficiency of a generator, you'd typically compare the memory used when iterating over the list vs. iterating over the generator. However, sys.getsizeof() isn't the right tool for measuring the memory usage of all items yielded by a generator, as it doesn't accumulate the size of each item generated.

'''