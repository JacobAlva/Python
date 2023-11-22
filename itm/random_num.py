# Random and psuedo random numbers

import random

a = random.random()     # returns a random float in the range 0-1
print(f'{a:.4f}')

b = random.uniform(1, 10)      # random float in the range 1 - 10
print(b)

print(random.randint(1, 5))      # prints random integers

print(random.randrange(1, 5))   # similar to randint but doesn't include the upper band values

c = random.normalvariate(0, 1)
print(c)

