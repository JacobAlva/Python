# colelctions: counter, namedtuple, orderedDict, defaultdict, deque

"""
    implements special container data types and provides alternatives
    to additional funtionalities compared to general built in containers 
    like dictionaries, lists or tuples.
"""
# this section reviews 5 diff types of collections

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

