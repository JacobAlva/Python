''' JSON format is used for data exchange (mostly in web apps)'''

import json

# Serialization / Encoding - The process of converting a Python dict to JSON format
person = {"name": "Alice", "age": 30, "city": "New York", "hasChildren": False, "hobbies": ["reading", "hiking", "painting"]}

# to convert to JSON
personJSON = json.dumps(person, indent=4, sort_keys=True) # separators=(';', ' = ')) # separators are not recommended, just use the default.
print(person)
print(personJSON)

# working with files
# this writes the content of the person dictionary to file in json format
with open ('person.json', 'w') as file:
    json.dump(person, file, indent=4)


# Deserialization / Decoding
# The process of coverting a json data to python object
person1 = json.loads(personJSON)
print(person1)      # python object.

# to covnert froma JSON file
with open ('person.json', 'r') as file:
    person = json.load(file)
    print(person)