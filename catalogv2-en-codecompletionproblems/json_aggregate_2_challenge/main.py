import json

data = [
        {"name": "Alice", "age": 25},
        {"name": "Bob", "age": 30},
        {"name": "Charlie", "age": 22},
        {"name": "David", "age": 28},
        {"name": "Eve", "age": 35}
]

min_age = None
name = None

# Loop through the list to calculate aggregations
for person in people:
        age = person["age"]

        if max_age is None or age < min_age:
                min_age = age
                name = person["name"]


print("Youngest Person", name)
