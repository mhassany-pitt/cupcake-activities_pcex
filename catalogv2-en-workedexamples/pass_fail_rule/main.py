#Step 1: Read the instructor inputs
text = input("Enter the exam score:")
exam_score = int(text)
text = input("Enter number of missing homework:")
number_of_missing_hw = int(text)
#Step 2: Write the boolean expression to determine whether the student fails the course
is_failing = exam_score < 55 or number_of_missing_hw > 2
#Step 3: Print the result
if is_failing == True :
        print("Yes! The student fails the course.")
else:
        print("No! The student does not fail the course.")
