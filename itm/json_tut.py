''' JSON format is used for data exchange (mostly in web apps)'''

import json

# Serialization / Encoding - The process of converting a Python dict to JSON format
person = {"name": "Alice", "age": 30, "city": "New York", "hasChildren": False, "hobbies": ["reading", "hiking", "painting"]}

# to convert to JSON
personJSON = json.dumps(person)
print(type(json.dumps(person)))