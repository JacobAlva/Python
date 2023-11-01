# colelctions: counter, namedtuple, orderedDict, defaultdict, deque

'''
    implements special container data types and provides alternatives
    to additional funtionalities compared to general built in containers 
    like dictionaries, lists or tuples.
'''
# this section reviews 5 diff types of collections

"""
# COUNTER
'''A counter is a container that stores elements as dictionary keys and
    their counts as dictionary values'''

from collections import Counter

a = "taabbcadbbadda" # any iterable could be used 
counter1 = Counter(a)
print(counter1)

# counter1 can be treated like any dictionary
print(counter1.values())                # returns a list or iterable of values
print(counter1.keys())                  # list of keys
print(counter1.items())                 # returns a list of key-value pairs
print(counter1.most_common())           # returns all items sorted in desc order
print(counter1.most_common(2))          # returns a list of the top 2 most common element enclosed in tuples
print(counter1.most_common(2)[0][0])    # selects the first element (key) of the first tuple in the list which is the value of the most common element in the collection
print(list(counter1.elements()))        # a list with all different elements repeating as many times as they count

# NAMED TUPLE
'''Easy to create light-weight object type similar to a struct'''

from collections import namedtuple
Point = namedtuple('Point', 'x,y')
pt = Point(2, -4)
print(pt)   # print the entire named tuple
print(pt.x, pt.y)   # access each field
print(pt.x * 2, pt.y + pt.x)    # perform arithmetic ops on field


# ORDERED DICT
''' Regular dictionaries but can remember the order items were inserted
    The have become less important since Python 3.7 that allows regular 
    dictionaries to remember order.
'''
from collections import OrderedDict
ordered_dict = OrderedDict() # using a dictionary  (with = {}) provides the same result
ordered_dict['b'] = 2
ordered_dict['c'] = 3
ordered_dict['d'] = 4
ordered_dict['a'] = 1
print(ordered_dict)


# DEFAULT DICTS
''' Similar to the regular dictionary except it has a default value if the key has 
    not been set yet.
'''
from collections import defaultdict
d_dict = defaultdict(int)       # the default value of an int is zero "0". Could take iterables also
d_dict['a'] = 1
d_dict['b'] = 2
d_dict['c'] = 3
d_dict['d']     # this would raise a key error with a normal dictionary but works with default_dicts     
print(d_dict)
print(d_dict['d'])
"""

