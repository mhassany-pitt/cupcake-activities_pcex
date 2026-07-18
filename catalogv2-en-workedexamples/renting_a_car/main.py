#Step 1: Read the inputs from the car rental agent
text = input("Enter the customer's age:")
age = int(text)
text = input("Enter 1 if the customer has driver's license, otherwise enter 0:")
input_num = int(text)
#Step 2: Determine whether the customer has driver's license
if input_num == 1 :
        has_license = True
else:
        has_license = False
#Step 3: Write the boolean expression to determine whether a customer could rent a car
can_rent_car = age >= 21 and has_license
#Step 4: Print the result
if can_rent_car == True :
        print("Yes! The customer could rent a car.")
else:
        print("No! The customer could not rent a car.")
