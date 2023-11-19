''' JSON format is used for data exchange (mostly in web apps)'''

import json

# Serialization / Encoding - The process of converting a Python dict to JSON format
person = {"name": "Alice", "age": 30, "city": "New York", "hasChildren": False, "hobbies": ["reading", "hiking", "painting"]}

# to convert to JSON
personJSON = json.dumps(person, indent=4, sort_keys=True) # separators=(';', ' = ')) # separators are not recommended, just use the default.
print(person)
print(personJSON)