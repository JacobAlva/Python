# Dictionary: key-value paris, unordered, mutable

# A dictionary is created with braces with each value pair separated by a comma ,
dict1 = {"name": "Jane", "age": 28, "city": "Maine"}
print(type(dict1))
print(dict1)

# create dictionary using the "dict" constructor. Here, you don't have
# to use quotes for your key.

dict2 = dict(name="Suner", age = 28, city = "Rhodes") 
print(dict2) 
print(type(dict2))

# to access the values in a dictionary
value = dict1["name"]
print(value)