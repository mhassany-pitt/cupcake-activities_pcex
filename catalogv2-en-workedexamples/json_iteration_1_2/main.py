# Modified from ChatGPT
import json

# Sample JSON data (structure with year, team, and stats)
nfl_data = '''
[
        {"year": 2022, "team": "Los Angeles Rams", "stats": {"wins": 12, "losses": 5, "points_scored": 460}},
        {"year": 2023, "team": "Kansas City Chiefs", "stats": {"wins": 14, "losses": 3, "points_scored": 496}},
        {"year": 2024, "team": "San Francisco 49ers", "stats": {"wins": 13, "losses": 4, "points_scored": 478}},
        {"year": 2025, "team": "Buffalo Bills", "stats": {"wins": 15, "losses": 2, "points_scored": 510}}
]
'''

# Load JSON data
data = json.loads(nfl_data)

# Print stats for Super Bowl-winning teams from 2022 to 2025
for entry in data:
        print("Year:", entry['year'])
        print(f"Team:",entry['team'])
        print("Stats:")
        for stat, value in entry['stats'].items():
                print(stat,value)
        print("-")
