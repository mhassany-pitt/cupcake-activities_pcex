#Step 1: Read the user inputs
text = input("Enter the phone age in years:")
phone_age = int(text)
text = input("Enter 1 if the phone is broken, otherwise enter 0:")
input_num = int(text)
#Step 2: Determine whether the phone is broken
if input_num == 1 :
        is_broken = True
else:
        is_broken = False
#Step 3: Write the boolean expression to determine whether it is time to buy a new phone
need_phone = is_broken or phone_age >= 3
#Step 4: Print the result
if need_phone == True :
        print("Yes! It is time to buy a new phone.")
else:
        print("No! It is not yet the time to buy a new phone.")
