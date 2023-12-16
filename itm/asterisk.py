''' ASTERISK (*)
    The asterisk is a very important symbol in Python with multiple uses including... Which would be explored below.
'''

"""
# simple multiplication
print(5 * 7)
print(5 ** 7)   # power operation / exponential

# to create iterables (list, tuples, strings) with repeated elements
rep = [1] * 5
print(rep)
rep = [1,2,3] * 5
print(rep)
rep = (1) * 5
print(rep)
rep = 'Paw' * 2
print(rep)
"""

# for the *args & **kwargs arguments
def foo(a, b, *args, **kwargs):
    print(a, b)
    for arg in args:
        print(arg)
    for key in kwargs:
        print(key, kwargs[key])
    for key, val in kwargs.items():
        print(key, val)

foo(1, 2, 3, 4, 5, bwe=6, ald=3, alpw=9)


# Enforce keyword only arguments
def kywd(a, b, *, c):
    print(a, b, c)

kywd(1, 3, c=5)