#Step 1: Read the user input for determining whether the phone is broken
text = input("Enter 1 if the phone is broken, otherwise enter 0:")
input_num = int(text)
#Step 2: Determine whether the phone is broken
if input_num == 1 :
        is_broken = True
else:
        is_broken = False
#Step 3: Read the user input for determining whether the phone screen is good
text = input("Enter 1 if the phone screen is good, otherwise enter 0:")
input_num = int(text)
#Step 4: Determine whether the phone screen is good
if input_num == 1 :
        screen_is_good = True
else:
        screen_is_good = False
#Step 5: Read the user input for determining whether the phone has random shutdown problem
text = input("Enter 1 if the phone has the random shutdown problem, otherwise enter 0:")
input_num = int(text)
#Step 6: Determine whether the phone has random shutdown problem
if input_num == 1 :
        random_shutdown = True
else:
        random_shutdown = False
#Step 7: Write the boolean expression to determine whether it is time to buy a new phone
need_phone = is_broken or not screen_is_good or random_shutdown
#Step 8: Print the result
if need_phone == True :
        print("Yes! It is time to buy a new phone.")
else:
        print("No! It is not yet the time to buy a new phone.")
