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
list2 = list(tuple3) # convert a tuple back to a list
print(type(tuple3))
print(type(list1))
print(type(list2))
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

# get tuple length
tuple4 = ('a', 'p', 'papaya', 'l', 'e', 'l', 3, 0)
print(len(tuple4))

# get number of occurence of an element
print(tuple4.count('p'))

# first index of an element
print(tuple4.index('p'))

# tuple slicing
tuple5 = tuple4[2:5:2] # see "list" for details on step index
print(tuple5)
"""

# unpacking a tuple
# while unpacking, the number of external elements must match 
# the number of elements in the tuple
tuple6 = "John", 32, "Muncie"
name, age, city = tuple6
print(name,"\n",age,"\n",city)

# unpack multiple elements with a star (*)
tuple7 = (1, 2, 4, 5, 6, 9)
a, *b, c, d = tuple7 # the star operator collects multiple values and stores them in list "b"
print(a,"\n",b,"\n",c,"\n",d)

# compare the size of tuple and list in "bytes"
import sys
tuple8 = ("what", "is", "your", "name?", 373, "watermelon")
list3 = ["what", "is", "your", "name?", 373, "watermelon"]
print(sys.getsizeof(tuple8), "bytes")
print(sys.getsizeof(list3), "bytes")
# the results show that a tuple is more memory efficient