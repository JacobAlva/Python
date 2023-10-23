# Sets: unordered, mutable data structure, no duplicates
""""
# set is made with curly braces
set1 = {5,1,3,4,2,2,3}
print(type(set1))
print(set1)

# using the set() constructor
set2 = set("Hello")

#list to set
myList = ["ball", "cherry", "ball", "comb"]
set3 = set(myList)
print(set3)

# to create an empty set    
# set4 = {}         # You can't use this because it is read as a dictionary
set4 = set()
set4.add(3)         # you can only add one element at a time.
set4.add("rat")
set4.add(9)
set4.add("5g")
print(set4)
set4.remove(3)      # removes an item from the set
print(set4)         # removing an inexistent element returns a "KeyError"

set4.discard(9)     # removes an element and does nothing if not a member
print(set4)

print(set4.pop())   # removes an arbitrary element from the set and removes it

set4.clear()        # empties the set
print(set4)     

# iterate over each
set5 = {5,1,3,4,2,2,3}
for i in set5:
    print(i)

# check if element exits
if 1 in set5:
    print("Yes")
"""

# set operations
odds = {1, 3, 5, 7, 9}
evens = {0, 2, 4, 6, 8}
primes = {2, 3, 5, 7}
