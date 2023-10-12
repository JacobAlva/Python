# Lists are ordered, mutable data structures that allow duplicate element

myList = ["ball", "cherry", "comb"]
print(myList)

# Lists can contain elements of different data types
myList2 = [5, True, 45.3, "Bread"]
print(myList2)

# to ndexe items in the list
item = myList[0] # where zero is the first and the last is n-1
print(item)

# list index out of range error is return when the index is larger than the list
#print(myList[3])

# prints last item. -2 for 2nd to last, etc.
print(myList[-1])

# iterate over list
for i in myList2:
    print(i)