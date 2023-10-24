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

# set operations
odds = {1, 3, 5, 7, 9}
evens = {0, 2, 4, 6, 8, "g"}
primes = {2, 3, 5, 7}
print(type(evens))
print(odds.union(primes))                # union
print(evens.intersection(primes))       # intersection
print(primes.difference(odds))          # in A (primes) but not in B (odds) in that order
print(odds.difference(primes))          # same operation in a different order retunrs a different result
print(odds.symmetric_difference(primes))    # returns the difference of both sets. Result is same irrespective of order
print(primes.symmetric_difference(odds))    # output is same in both 


# previous operations above don't modify the set, they rather create a new set with the output
# to modify the set in place

set5 = {1, 3, 5, 7, 9}
set6 = {1, 3, 5, 0, 2, 6, 8, "g"}
set7 = {3, 4, 9, 0}
print(set5)
set5.update(set6)       # updates set5 as the union of both sets
print(set5)

set6.intersection_update(set7)  # updates set6 with the intersection of both sets
print(set6)

print(set7)
set7.difference_update(set5)    # removes all element of set5 from set7
print(set7) 

print(set6)
set8 = {1, 0, 4, 7, 89}
set8.symmetric_difference_update(set6)  # symmetric difference update 
print(set8)
"""

set9 = {1, 2, 3, 4, 5}
set10 = {1, 2, 3}

print(set9.issubset(set10))     # returns a boolean if A is subset of B or not
print(set10.issubset(set9))
print(set9.issuperset(set10))   # is superset
print(set10.issuperset(set9))
print(set9.isdisjoint(set10))   # Return True if two sets have a null intersection.

