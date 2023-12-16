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

# Argument unpacking
def func(a, b, c):
    print(a, b, c)

list2 = [1,2,3] 
func(*list2)            # iterable must have the same length as function parameter

dict2 = {'a':6, 'b':7, 'c':8}       # dict keys must be same as function parameters
func(**dict2)


# Container unpacking
#numb = [1, 2, 3, 4, 5, 6]
numb = (1, 2, 3, 4, 5, 6)

#*beg, las, fir = numb        # the * will always unpack the elements into a list even if the referenced iterable is not a list
beg, *mid, las = numb 
beg, nxt, *las = numb
print(beg)
print(mid)
print(las)
"""


# Merge iterables into a list
my_tuple = (1, 2, 3, 4)
my_list = [4, 5, 6]
my_set = {7, 8, 9}
my_dict = {'a':10, 'b':11}

new_list = (*my_tuple, *my_list, *my_set, *my_dict.values())        # returns the value of the dict, otherwise, *my_dict returns the keys
print(new_list)
print(type(new_list))
print(my_dict.values())

# To merge dictionaries
dicta = {'a':10, 'b':11}
dictb = {'c':12, 'd':13}
# dictc = {*dicta, *dictb}    # this will return a set of the keys from the merger
dictc = {**dicta, **dictb}      # returns the merged dictionaries as dicts
print(type(dictc))
print(dictc)