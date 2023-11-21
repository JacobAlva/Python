''' JSON format is used for data exchange (mostly in web apps)'''

import json

"""
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
"""

class User:
    def __init__(self, name, age):
        self.name = name
        self.age = age

user = User('Max', 27)

# custome encoding to make class object JSON serializable
def encode_user(o):
    if isinstance(o, User):
        return {'name': o.name, 'age': o.age, o.__class__.__name__: True}
    else:
        raise TypeError('Object of type User is not JSON serializable')

# without the fxn above ... it will return an error as the User's object type (class) is not JSON serializable
userJSON = json.dumps(user, default=encode_user)
print(userJSON)


# another option by implementing a custom JSON Encoder
from json import JSONEncoder
class UserEncoder(JSONEncoder):
    def default(self, o):
        if isinstance(o, User):
            return {'name': o.name, 'age': o.age, o.__class__.__name__: True}
        return JSONEncoder.default(self, o)
    
userJSON_1 = json.dumps(user, cls=UserEncoder)
print(userJSON_1)

# you could also say
userJSON_2 = UserEncoder().encode(user)
print(userJSON_2)