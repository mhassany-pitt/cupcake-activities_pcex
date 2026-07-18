#Step 1: Read the first integer that the user enters
text = input("Enter an integer:")
num = int(text)
#Step 2: Print the integer that the user has entered, then receive the next integers as long as the user enters an integer that is not negative;; otherwise stop
while num >= 0 :
        print("The integer entered is:", num)
        text = input("Enter an integer:")
        num = int(text)
print("End of input.")
