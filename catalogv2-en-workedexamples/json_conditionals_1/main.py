

import json


restaurant_data = [
        {"_id": 1, "name": "Taco", "cuisine": "Mexican", "ingredients": ["beef", "tortilla", "cheese"]},
        {"_id": 2, "name": "Burrito", "cuisine": "Mexican", "ingredients": ["chicken", "rice", "beans"]},
        {"_id": 3, "name": "Quesadilla", "cuisine": "Mexican", "ingredients": ["beef", "cheese", "tortilla"]},
        {"_id": 4, "name": "Pasta", "cuisine": "Italian", "ingredients": ["tomato", "cheese"]},
]



for _item in restaurant_data:
        if _item["cuisine"] == "Mexican" and "beef" in _item["ingredients"]:
                beef_mexican_items.append(_item["name"])


print(beef_mexican_items)
