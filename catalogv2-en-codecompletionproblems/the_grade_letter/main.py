#Step 1: Read the letter grade
grade = input("Enter a grade letter in uppercase: ")
#Step 2: Determine and print the numeric range for the input letter grade
if grade == "A" :
        print("Score is greater than or equal 90.")
elif grade == "B" :
        print("Score is in range [80-90).")
elif grade == "C" :
        print("Score is in range [70-80).")
elif grade == "D" :
        print("Score is in range [60-70).")
else :
        print("Score is below 60.")
