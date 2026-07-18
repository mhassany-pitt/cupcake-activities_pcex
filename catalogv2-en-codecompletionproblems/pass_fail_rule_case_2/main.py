#Step 1: Read the instructor inputs
text = input("Enter the exam score:")
exam_score = int(text)
text = input("Enter 1 if the student has cheated, otherwise enter 0:")
input_num = int(text)
#Step 2: Determine whether the student has cheated
if input_num == 1 :
        has_cheated = True
else:
        has_cheated = False
#Step 3: Write the boolean expression to determine whether the student fails the course
is_failing = exam_score < 55 or has_cheated
#Step 4: Print the result
if is_failing == True :
        print("Yes! The student fails the course.")
else:
        print("No! The student does not fail the course.")
