'''
    Generators are functions that return an object that can be iterated over. The generate the item inside the object lazily i.e. they generate only one at a time and only when you ask for it making them more memory efficient when dealing with large data sets. They are defined like normal functions but with a yield keyword instead of the return
'''

def mygenerator():
    yield 1
    yield 2
    yield 3

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
"""