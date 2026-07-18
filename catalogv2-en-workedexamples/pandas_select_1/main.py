# Source: ChatGPT
import pandas as pd

# Load the dataset
df = pd.read_csv('science_class.csv')  # Replace with your actual CSV file

# Select only student IDs and their letter grades
df_selected = df[['student_id', 'letter_grade']]

# Filter students in 'Section 1'
df_section1 = df[df['section'] == 'Section 1']

# Display the result
print(df_section1)
