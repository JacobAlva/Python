# Tuples: ordered, immutable data structures, allow duplicate elements

mytuple = ("Max", 28, "Bread") #this is a tuple
print(type(mytuple))

#this is a string
tuple1 = "Max" # a single element tuple like this is recognised as a string. To make it a tuple, add a comma ("Max",)
print(type(tuple1))

#this is a tuple | Parenthesis () are optional for tuples
tuple2 = "Max", #the ending comma changes this string to a tuple
print(type(tuple2)) 

# you can also create a tuple from an iterable such as a list using the tuple() function
tuple3 = tuple(["may", 45, "Bread"])
print(type(tuple3))
