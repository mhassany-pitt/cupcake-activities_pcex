#Step 1: Read the first integer that the user enters
text = input("Enter an integer:")
num = int(text)
#Step 2: Print the integer that the user has entered, then receive the next integers as long as the user enters an integer that is not even or is not less than 10; otherwise stop
while num % 2 != 0 or num >= 10 :
        print("The integer entered is:", num)
        text = input("Enter an integer:")
        num = int(text)
print("End of input.")
