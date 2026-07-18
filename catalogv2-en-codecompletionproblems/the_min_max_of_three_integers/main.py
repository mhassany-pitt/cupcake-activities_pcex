#Step 1: Read the three integers
text = input("Enter the first integer: ")
num1 = int(text)
text = input("Enter the second integer: ")
num2 = int(text)
text = input("Enter the third integer: ")
num3 = int(text)
#Step 2: Determine the maximum integer
if num1 > num2 :
        if num1 > num3 :
                max_num = num1
        else :
                max_num = num3
else :
        if num2 > num3 :
                max_num = num2
        else :
                max_num = num3
#Step 3: Print the maximum integer
print("Maximum value:", max_num)
