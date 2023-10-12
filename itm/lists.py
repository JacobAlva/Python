# Lists are ordered, mutable data structures that allow duplicate element

myList = ["ball", "cherry", "comb"]
print(myList2)

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

# to insert item at specific location
myList.insert(1, "berry") # 1 here is the index position
print(myList)