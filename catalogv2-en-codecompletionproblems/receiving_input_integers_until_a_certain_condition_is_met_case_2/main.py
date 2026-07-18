#Step 1: Read the first integer that the user enters
text = input("Enter an integer:")
num = int(text)
#Step 2: Print the integer that the user has entered, then receive the next integers as long as the user enters an integer that is in the range of 30 to 90 both inclusive; otherwise stop
while num >= 30 and num <= 90 :
        print("The integer entered is:", num)
        text = input("Enter an integer:")
        num = int(text)
print("End of input.")
