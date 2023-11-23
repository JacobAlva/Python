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
"""

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