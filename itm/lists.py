# Lists are ordered, mutable data structures that allow duplicate element

myList = ["ball", "cherry", "comb"]
print(myList)


# Lists can contain elements of different data types
myList2 = [5, True, 45.3, "Bread"]
#print(myList2)

"""
# to index items in the list
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


# to insert item at specific index
myList.insert(1, "berry") # 1 here is the index position
print(myList)

# to remove items
print(myList.pop(1)) # "pop" returns the indexed item and removes it (helps you to see what you are removing)
print(myList)

myList.remove("ball") # takes in a string and removes the item. NOT by INDEX
print(myList)

# remove all elements and empty list
myList2.clear() 
myList.reverse()    # reverses the order of the list || check line 82
myList.sort()   # sorts the list in ascending order and in-place (replaces existing list)

# to sort and not modify the list, use "sorted"
list1 = [1,2,6,-4,3,0]
new_list = sorted(list1)
new_listrev = sorted(list1, reverse=True)   # to sort in reverse order
print(list1)
print(new_list)
print(new_listrev)
"""

#create new list with similar items
lista = [0] * 3
print(lista)

# concatenate lists
listb = [1, 2, 3, 4, 5]
listc = lista + listb 
print(listc)

# to slice a list (cut out a part)
a = listc[2:6] #if you don't specify a stop index, it cuts to the end
print(a)
print(listc[2:]) # cuts from 2 to the end
print(listc[:4]) #from start to 4
print(listc[:]) # returns original list as it slices from begining to the end

# double colon introduces the step index.
print(listc[2:6:2]) # selects every second item between index 2 and 6
print(listc[::-1]) # a cool way to reverse your list.

