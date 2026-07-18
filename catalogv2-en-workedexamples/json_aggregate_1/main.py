import json
data = [
        {"name": "John", "salary": 35000},
        {"name": "Sarah", "salary": 25000},
        {"name": "James", "salary": 45000},
        {"name": "Emily", "salary": 29000}
]


count = 0


for employee in data:
        if employee["salary"] > 30000:
                count += 1


print(count)
