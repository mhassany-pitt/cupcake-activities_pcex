#Step 1: Define the variables that we need for this program
total = 0
count = 0
#/Step 2: Read the first number that the user enters
text = input("Enter a number: ")
num = float(text)
#Step 3: Process the number that the user has entered, then receive and process the next numbers as long as the user enters a non-negative number; otherwise stop
while num >= 0.0 :
        count += 1
        total += num
        print("The sum so far is", total, ", count =", count)
        text = input("Enter a number: ")
        num = float(text)
#Step 4: Calculate and print the average of the numbers entered by the user
if count == 0 :
        print("No numbers were entered.")
else :
        average = total / count
print("The average is:", average)
