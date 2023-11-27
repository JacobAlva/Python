# Lists are ordered, mutable, iterable data structures that allow duplicate element

# lists are created with square brackets and elements separated by comma
myList = ["ball", "cherry", "ball", "comb"]
print(myList)

list1a = list("123441")
print(list1a)

# Lists can contain elements of different data types
myList2 = [5, True, 45.3, "Bread"]
#print(myList2)

"""
# to index items in the list
item = myList[0] # where zero is the first and the last is n-1
#print(item)

# list "index out of range" error is return when the index is larger than the list
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

#append/add item to the end of the list
myList.append("lemon") 
print(myList)

listx = []
listx.append("('apple', 'clas')")
listx.append((2, False, 14))
print(listx)

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

# Copying list
# While copying list, be careful not to marely assign as both lists will
# reference the same location in memory and any change to one will affect the other.

list5 = [1,2,4,5]
list6 = list5
list6.append("apple")
print(list5)
print(list6)

# to avoid this, use any of the following methods (.copy, list, or slicing "[:]", for loop)
list7 = list5.copy()    #.copy
list5.insert(2,"goat")
print(list5)
print(list7)

list8 = list(list5)     # using list function
list8.append(3)
print(list5)
print(list8)

list9 = list5[:]        # slicing from begining to the end. See line 77
list9.append('bread')
print(list5)
print(list9)

listX = [i for i in list5]  # for loop
list5.append("butter")
print(list5)
print(listX)
"""

#list comprehension - fast way to create a new list from an existing one
list10 = [1,2,3,4,5,6]
list11 = [i for i in list10]    # returns a copy of the list
list10.append(23)
print(list10)
print(list11)

# like any for loop, you can manipulate the value of i depending on what you want in the list
list12 = [i*i for i in list10]  # returns a square of every item in the list
print(list12)

print(max(list12))
print(min(list12))