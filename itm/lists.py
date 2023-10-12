# Lists are ordered, mutable data structures that allow duplicate element

myList = ["ball", "cherry", "comb"]
print(myList)

"""
# Lists can contain elements of different data types
myList2 = [5, True, 45.3, "Bread"]
print(myList2)

# to ndexe items in the list
item = myList[0] # where zero is the first and the last is n-1
#print(item)

# list index out of range error is return when the index is larger than the list
#print(myList[3])

# prints last item. -2 for 2nd to last, etc.
#print(myList[-1])

# iterate over list
for i in myList2:
    print(i)

# to check if an element is in a list
if "Breader" in myList:
    print(True)
else:
    print(False)

print(len(myList)) #returns the length of the list


myList.append("lemon") #append/add item to the end of the list
print(myList)
"""

# to insert item at specific index
myList.insert(1, "berry") # 1 here is the index position
print(myList)

# to remove items
print(myList.pop(1)) # "pop" returns the indexed item and removes it (helps you to see what you are removing)
print(myList)

myList.remove("ball") # takes in a string and removes the item. NOT by INDEX
print(myList)

# remove all elements and empty list
myList.claer() 
myList.reverse() # reverses the order of the list
myList.sort() # sorts the list in ascending order and in-place (replaces existing list)