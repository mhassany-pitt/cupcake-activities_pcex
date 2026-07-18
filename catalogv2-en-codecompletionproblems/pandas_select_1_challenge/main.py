
import pandas as pd


df = pd.read_csv('science_class.csv')


df_selected = df[['student_id', 'letter_grade']]


df_section1 = df[(df['section'] == 'A')|(df['section'] == 'B')]


print(df_section1)
