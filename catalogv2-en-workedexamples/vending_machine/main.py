#Step 1: Assign initial values to the variables which we need for this program
pennies_per_dollar = 100
pennies_per_quarter = 25
#Step 2: Read the bill value and item price
text = input("Enter bill value in dollars (1 = $1 bill, 5 = $5 bill, etc.): ")
bill_value = int(text)
text = input("Enter item price in pennies: ")
item_price = int(text)
#Step 3: Compute the change due
change_due = pennies_per_dollar * bill_value - item_price
#Step 4: Compute the number of dollars and update the change due after taking away the dollars
dollars = change_due // pennies_per_dollar
change_due = change_due % pennies_per_dollar
#Step 5: Compute the number of quarters in the remaining change due
quarters = change_due // pennies_per_quarter
#Step 6: Display the result
print("Your change consists of:")
print(dollars, "dollars")
print(quarters, "quarters")
