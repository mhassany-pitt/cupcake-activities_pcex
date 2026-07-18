#Step 1: Read the three integers
text = input("Enter the first integer: ")
num1 = int(text)
text = input("Enter the second integer: ")
num2 = int(text)
text = input("Enter the third integer: ")
num3 = int(text)
#Step 2: Determine the minimum integer
if num1 < num2 :
        if num1 < num3 :
                min_num = num1
        else :
                min_num = num3
else :
        if num2 < num3 :
                min_num = num2
        else :
                min_num = num3
#Step 3: Print the minimum integer
print("Minimum value:", min_num)
