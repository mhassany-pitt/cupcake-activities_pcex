#Step 1: Assign initial values to the variables which we need for this program
rate = 8.25
standard = 40
weekend_pay_min = 30
weekend_pay_max = 50
#Step 2: Read the input data
text = input("Enter the number of hours that the employee has worked: ")
hours = int(text)
text = input("Enter the number of days that the employee has worked during weekends: ")
no_weekend_days = int(text)
#Step 3: Pay overtime at "time and a half" of the regular rate of pay
if hours > standard :
        wage = standard * rate + ( hours-standard ) * ( rate * 1.5 )
else :
        wage = hours * rate
#Step 4: Take into account the extra pay for the work during weekends days
if no_weekend_days < 5 :
        wage += (no_weekend_days * weekend_pay_min)
else :
        wage += (no_weekend_days * weekend_pay_max)
#Step 5: Print the calculated wage
print("Wage:", wage)
