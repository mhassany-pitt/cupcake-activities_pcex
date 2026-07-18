import pandas as pd


df = pd.read_csv('students_data.csv')


grouped_by_section_grade = df.groupby(['Section', 'Grade']).size()


print("Grouped by Section and Grade:", grouped_by_section_grade)
