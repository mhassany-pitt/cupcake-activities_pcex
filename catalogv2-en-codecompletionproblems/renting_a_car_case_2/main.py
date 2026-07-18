#Step 1: Read the input for the customer's age
text = input("Enter the customer's age:")
age = int(text)
#Step 2: Read the input for determining whether the customer has driver's license
text = input("Enter 1 if the customer has driver's license, otherwise enter 0:")
input_num = int(text)
#Step 3: Determine whether the customer has driver's license
if input_num == 1 :
        has_license = True
else:
        has_license = False
#Step 4: Read the input for determining whether the customer has had an accident
text = input("Enter 1 if the customer has had an accident, otherwise enter 0:")
input_num = int(text)
#Step 5: Determine whether the customer has had an accident
if input_num == 1 :
        had_accidents = True
else:
        had_accidents = False
#Step 6: Write the boolean expression to determine whether a customer could rent a car
can_rent_car = age >= 21 and has_license and not had_accidents
#Step 7: Print the result
if can_rent_car == True :
        print("Yes! The customer could rent a car.")
else:
        print("No! The customer could not rent a car.")
