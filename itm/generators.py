'''
    Generators are functions that return an object that can be iterated over. The generate the item inside the object lazily i.e. they generate only one at a time and only when you ask for it making them more memory efficient when dealing with large data sets. They are defined like normal functions but with a yield keyword instead of the return
'''

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
"""

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


