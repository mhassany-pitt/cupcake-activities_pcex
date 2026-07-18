import pandas as pd

# Load the dataset
df = pd.read_csv('students_data.csv')

# Step 1: Find max score for each homework
max_scores = {}
for i in range(1, 11):
        max_scores[f'Homework_{i}'] = df[f'Homework_{i}'].max()

# Step 2: Identify students who scored the highest in at least 5 homeworks
top_homework_scorers = []
for index, row in df.iterrows():
        count = 0
        for i in range(1, 11):
                if row[f'Homework_{i}'] == max_scores[f'Homework_{i}']:
                        count += 1
        top_homework_scorers.append(count >= 5)

df.loc[:,'Top_Homework_Scorer'] = top_homework_scorers

# Step 4: Filter students who got a final grade greater than 'B' and scored highest in at least 5 homeworks
filtered_students = []
for ind, row in df.iterrows():
        if (df.loc[ind,'Grade'] > 80) & (df.loc[ind,'Top_Homework_Scorer']):
                filtered_students.append(True)
        else:
                filtered_students.append(False)

df['Filtered'] = filtered_students
top_students = df[df['Filtered']]

# Step 5: Group by Section and Final Grade
grouped_students = top_students.groupby(['Section', 'Grade']).size()

# Display results
print("Students scoring highest in at least 5 homeworks & having final grade > B:\n", grouped_students)
