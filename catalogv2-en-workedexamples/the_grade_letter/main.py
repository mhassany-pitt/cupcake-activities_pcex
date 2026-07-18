#Step 1: Read the score
text = input("Enter a score: ")
score = int(text)
#Step 2: Determine the grade for the score
if score >= 90 :
        grade = "A"
elif score >= 80 :
        grade = "B"
elif score >= 70 :
        grade = "C"
elif score >= 60 :
        grade = "D"
else :
        grade = "F"
#Step 3: Print the grade
print("Grade =", grade)
