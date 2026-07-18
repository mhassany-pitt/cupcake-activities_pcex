import pandas as pd

# Read dataset
df = pd.read_csv("students.csv")

# Get sample size
sample_size = df.shape[0]
print("Sample size:",sample_size)

# Print top 5 examples
print("Top 5 rows:")
print(df.head(5))

# Get mean grade
mean_grade = df["grade"].mean()
print(f"Mean grade:", mean_grade)

# Use describe function
print("Summary statistics:")
print(df["grade"].describe())

# Get student counts by grade
print("Counts by grade:")
print(df["grade"].value_counts())

# Find students in section 2 and get counts by grade
section_2_counts = df[df["section"] == 2]["grade"].value_counts()

# Print first 10 entries
print("Top 10 grade counts for Section 2:")
print(section_2_counts.head(10))
