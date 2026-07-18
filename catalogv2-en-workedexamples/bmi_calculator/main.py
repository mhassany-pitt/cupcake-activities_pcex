#Step 1: Receive the weight and height from the user
text = input("Enter the weight in pounds:")
weight = float(text)
text = input("Enter the height in inches:")
height = float(text)
#Step 2: Calculate BMI
bmi = weight / height ** 2 * 703
#Step 3: Print the result
print("The BMI is:", bmi)
