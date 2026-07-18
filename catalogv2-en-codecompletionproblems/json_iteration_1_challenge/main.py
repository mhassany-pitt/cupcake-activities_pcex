restaurant_json = [
        {"name": "Taqueria","menu":['Tacos','Quesedillas','Fajitas']},
        {"name": "Romanos","menu":['Pizzas','Pastas']},
        {"name": "Bao", "menu":['orange chicken','spicy ramen']}
]

for item in restaurant_json:
        print(item['name'])
