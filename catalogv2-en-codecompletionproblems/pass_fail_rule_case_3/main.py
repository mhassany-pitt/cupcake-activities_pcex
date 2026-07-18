#Step 1: Read the instructor inputs
text = input("Enter the student's score:")
student_score = int(text)
text = input("Enter the class average:")
class_average = int(text)
#Step 2: Write the boolean expression to determine whether the student fails the course
is_failing = not ( student_score > class_average )
#Step 3: Print the result
if is_failing == True :
        print("Yes! The student fails the course.")
else:
        print("No! The student does not fail the course.")
