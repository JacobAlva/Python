# Dictionary: key-value paris, unordered, mutable

# A dictionary is created with braces with each value pair separated by a comma ,
dict1 = {"name": "Jane", "age": 28, "city": "Maine"}
#print(type(dict1))
#print(dict1)

# create dictionary using the "dict" constructor. Here, you don't have
# to use quotes for your key.

dict2 = dict(name="Suner", age = 28, city = "Rhodes") 

"""
print(dict2) 
print(type(dict2))

# to access the values in a dictionary
# referencing a key not in the dic returns a KeyError
value = dict1["age"]
print(value)

# adding more items to a dict
dict1["email"] = "e@u.com"
print(dict1)

# a repeat of this overwrites the current value of the 'email' key
dict1["email"] = "elen@raz.com"
print(dict1)


# to delete items
del dict1["name"]
print(dict1)

# using the pop method
dict2.pop("age")
print(dict2)

# pops from any arbitrary point in the dict, 
# but since Python3, it pops the last added entry
# to remove a specific key item, use "pop"
print(dict2.popitem()) 

# to check if a key is in a dict
# you can use an if/else statement 
if "name" in dict1:
    print(dict1["name"])

# or use a try/except statement
try:
    print(dict2["name"])
except:
    print("Error") # returns an error is the key isn't found

# iterate over a dict and return all the values 
for key in dict1:
    print(key)

# returns all the keys also
for keys in dict2.keys():
    print(keys)

# to return all values
for val in dict2.values():
    print(val)

# for both keys and values
for key, val in dict1.items():
    print(key,":", val)
"""
# to copy a dictionary
# Similar to a list, copying a dictionary directly references a pointer.
# Thus, modifying the copy modifies the original list
dict1_cpy = dict1
print(dict1)
print(dict1_cpy)

dict1_cpy["email"] = "ja@cyb.com"
print(dict1)
print(dict1_cpy)

# to avoid this, use either the .copy() function, dict(...) or for loop

# using copy
dict3 = dict1.copy()
dict3["tel"] = "453-782"
print(dict3)
print(dict1)

# you can also use the dict function
dict4 = dict(dict2)
dict4["tel"] = "453-782"
print(dict4)
print(dict2)

# using a for loop to create a new dictionary
    # dict5 = {(key, val) for key, val in dict2.items()} # returned a SET
dict5 = {key:val for key, val in dict2.items()}
dict5["zip"] = "47208"
print(dict5)
print(dict2)
print(type(dict5))