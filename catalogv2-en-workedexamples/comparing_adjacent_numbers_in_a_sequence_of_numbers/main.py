#Step 1: Read the first number that the user enters
text = input("Enter a number: ")
num = float(text)
#Step 2: Read the rest of the numbers that the user enters and check for adjacent duplicates
while num != -1 :
        previous = num
        text = input("Enter a number: ")
        num = float(text)
        if num == previous :
                print("Duplicate input for number:", num)
