# Tuples: ordered, immutable data structures, allow duplicate elements

"""
#this is a tuple
mytuple = ("Max", 28, "Bread") 
print(type(mytuple))

#this is a string
tuple1 = "Max" # a single element tuple like this is recognised as a string. To make it a tuple, add a comma ("Max",)
print(type(tuple1))

#this is a tuple | Parenthesis () are optional for tuples
tuple2 = "Max", #the ending comma changes this string to a tuple
print(type(tuple2)) 

# you can also create a tuple from an iterable such as a list using the tuple() function
list1 = ["may", 45, "Bread"]
tuple3 = tuple(list1)
print(type(tuple3))
print(type(list1))
list1.insert(2,"goat",)
print(list1)

# to pick the last element in the tuple
item = tuple3[-1]
print(item)

# iterate over tuple
for i in tuple3:
    print(i)

# check if element is in tuple
if "ball" in tuple3:
    print("Yes")
else:
    print("No")

"""

# get tuple length
tuple4 = ('a', 'p', 'papaya', 'l', 'e', 'l')
print(len(tuple4))

# get number of occurence of an element
print(tuple4.count('p'))

# first index of an element
print(tuple4.index('l'))