

import json


restaurants_json = [
        {
                "name": "Taco Fiesta",
                "reviews": 5,
                "cuisine": "Mexican",
                "spicy_food": True,
                "seating": [2, 4, 6],
                "max_reservation": 30
        },
        {
                "name": "Burrito King",
                "reviews": 10,
                "cuisine": "Mexican",
                "spicy_food": False,
                "seating": [2, 4],
                "max_reservation": 30
        },
        {
                "name": "Salsa Heaven",
                "reviews": 3,
                "cuisine": "Mexican",
                "spicy_food": True,
                "seating": [2, 4, 8],
                "max_reservation": 30
        },
        {
                "name": "Pasta Palace",
                "reviews": 8,
                "cuisine": "Italian",
                "spicy_food": False,
                "seating": [2, 4],
                "max_reservation": 20
        }
]

filtered_restaurants = []

for r in restaurants_json:
        if r["reviews"] >= 1:
                if r["cuisine"].lower() == "mexican":
                        if r["spicy_food"]:
                                if 2 in r["seating"]:
                                                if r["max_reservation"] <= 30:
                                                        filtered_restaurants.append(r)




print(filtered_restaurants)
