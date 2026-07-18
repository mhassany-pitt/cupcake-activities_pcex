#Step 1: Read the first integer that the user enters
text = input("Enter an integer: ")
num = int(text)
#Step 2: Read the rest of the integers that the user enters and check for adjacent consecutive numbers
while num != -1 :
        previous = num
        text = input("Enter an integer: ")
        num = int(text)
        if num != -1 and num - previous == 1 :
                print(previous, "and", num, "are consecutive.")
