#Step 1: Assign initial values to the variables which we need for this program
rate = 8.25
standard = 40
#Step 2: Read the number of hours that the employee has worked
text = input("Enter the number of hours that the employee has worked: ")
hours = int(text)
#Step 3: Pay overtime at "time and a half" of the regular rate of pay
if hours > standard :
        wage = standard * rate + ( hours - standard ) * ( rate * 1.5 )
else :
        wage = hours * rate
#Step 4: Print the calculated wage
print("Wage:", wage)
