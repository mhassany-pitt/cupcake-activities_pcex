import json

data = [
        {"name": "John", "salary": 35000},
        {"name": "Sarah", "salary": 25000},
        {"name": "James", "salary": 45000},
        {"name": "Emily", "salary": 45000}
]


highest_salary = 0
count = 0
for employee in data:
        if employee["salary"] > highest_salary:
                highest_salary = employee["salary"]
                count += 1


print(count)
