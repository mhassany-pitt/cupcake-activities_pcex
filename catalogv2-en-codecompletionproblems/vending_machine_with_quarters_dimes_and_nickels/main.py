#Step 1: Assign initial values to the variables which we need for this program
pennies_per_dollar = 100
pennies_per_quarter = 25
pennies_per_dime = 10
pennies_per_nickel = 5
#Step 2: Read the bill value and item price
text = input("Enter bill value in dollars (1 = $1 bill, 5 = $5 bill, etc.): ")
bill_value = int(text)
text = input("Enter item price in pennies: ")
itemPrice = int(text)
#Step 3: Compute the change due
change_due = pennies_per_dollar * bill_value - itemPrice
#Step 4: Compute the number of quarters in the change due and update the change due after taking away the quarters
quarters = change_due // pennies_per_quarter
change_due = change_due % pennies_per_quarter
#Step 5: Compute the number of dimes in the remaining change due and update the change due after taking away the dimes
dimes = change_due // pennies_per_dime
change_due = change_due % pennies_per_dime
#Step 6: Compute the number of nickels in the remaining change due
nickels = change_due // pennies_per_nickel
#Step 7: Display the result
print("Your change consists of:")
print(quarters, "quarters")
print(dimes, "dimes")
print(nickels, "nickels")
