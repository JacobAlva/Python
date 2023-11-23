# Random and psuedo random numbers

import random

"""
a = random.random()     # returns a random float in the range 0-1
print(f'{a:.4f}')

b = random.uniform(1, 10)      # random float in the range 1 - 10
print(b)

print(random.randint(1, 5))      # prints random integers

print(random.randrange(1, 5))   # similar to randint but doesn't include the upper band values

c = random.normalvariate(0, 1)
print(c)


# lists and randoms
list1 = list("ABCDEFGH")
print(list1)
list2 = random.sample(list1, 3)     # creates a list of 3 unique random elements from list1
print(list2)
list3 = random.choices(list1, k=3)     # creates a list of 3 random elements from list1. Elements can repeat
print(list3)
random.shuffle(list1)       # suffles the list
print(list1)

# this will not work as you can't shuffle a tuple (immutable)
tups = (1,2,3,4,5,6)
random.shuffle(tups)
print(tups)


# Pseudorandoms and seeds
''' Remember, the random class are pseudo random numbers. This can be tested with the seed value which controls the randomness.'''

random.seed(1)
print(random.random())
print(random.randint(1,10))
random.seed(2)
print(random.random())
print(random.randint(1,10))
random.seed(1)
print(random.random())
print(random.randint(1,10))
random.seed(2)
print(random.random())
print(random.randint(1,10))

'''
    running this shows a repeat in the random values, indicating they are pseudorandom
    random seed functions can be used to reproduce data.
    Because the random class are reproduceable, they are not recommended to be used for security purposes, instead, use the secrets class.
'''


import secrets
''' The secrets class is a true random class with only three methods, and can be used for passwords, security tokens and authentication'''

sec1 = secrets.randbelow(10)      # Return a random int in the range (0, n-1). 
print(sec1)

sec2 = secrets.randbits(4)      # Generates an int(base 10) with k random bits.
print(sec2)

list4 = list("A,B,C,D,E,F,G")
sec3 = secrets.choice(list4)       # Choose a random element from a non-empty sequence.

"""

'''To work with arrays, you need to use the numpy module'''
import numpy

ar = numpy.random.rand(3)
print(ar)
#print(numpy.random.rand(3,3))       # returns a 3by3 array
print(numpy.random.randint(0, 10, 4))       # creats a 4 element array between 1-10
#print(numpy.random.randint(0, 10, (3,2,3)))
arr = numpy.array([[1,2,3], [4,5,6], [7,8,9]])
print(arr)
numpy.random.shuffle(arr)   # shuffles the position but doesn't shuffle the array itself
print(arr)

arr2 = numpy.random.randint(0,10,(3,3))
print(arr2)
numpy.random.shuffle(arr2)
print(arr2)