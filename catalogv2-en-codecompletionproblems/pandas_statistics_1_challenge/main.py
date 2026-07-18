import pandas as pd

# Read dataset
df = pd.read_csv("students.csv")


section_2_counts = df[df["grade"] == 'A']
section_2_counts.sort_values(by=['name'])
# Print first 10 entries
print("Top 10 student names with grade A")
print(section_2_counts.head(10))
