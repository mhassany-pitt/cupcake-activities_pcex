#Step 1: Read the first number that the user enters
text = input("Enter a number: ")
num = float(text)
#Step 2: Read the rest of the numbers that the user enters and check for adjacent numbers in ascending order
while num != 0 :
        previous = num
        text = input("Enter a number: ")
        num = float(text)
        if num != 0 and num > previous :
                print(previous,"and", num, "are in ascending order.")
