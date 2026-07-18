#Step 1: Receive the weight and height from the user
text = input("Enter the weight in pounds:")
weight = float(text)
text = input("Enter the height in inches:")
height = float(text)
#Step 2: Calculate BMI
bmi = weight / height ** 2 * 703
#Step 3: Round up BMI
bmi = round(bmi)
#Step 4: Print results
print("The BMI rounded to the nearest integer is:", bmi)
