#Step 1: Assign initial values to the variables which we need for this program
total = 0
count = 0
#Step 2: Read the first integer that the user enters
text = input("Enter an integer (0 to quit): ")
num = int(text)
#Step 3: Process the integer that the user has entered, then receive and process the next integers as long as the user enters a non-zero integer; otherwise stop
while num != 0 :
        if num % 2 == 0 :
                count += 1
                total += num
        print("The sum of even numbers so far is", total, ", count of even numbers =", count)
        text = input("Enter an integer (0 to quit): ")
        num = int(text)
#Step 4: Calculate and print the average of the even integers entered by the user
if count == 0 :
        print("No even integers were entered.")
else :
        average = total / count
print("The average is:", average)
