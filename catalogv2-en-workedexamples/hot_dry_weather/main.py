#Step 1: Read the user input for determining whether it is too hot
text = input("Enter 1 if it is too hot, otherwise enter 0:")
input_num = int(text)
#Step 2: Determine whether it is too hot
if input_num == 1 :
        too_hot = True
else:
        too_hot = False
#Step 3: Read the user input for determining whether it is too dry
text = input("Enter 1 if it is too dry, otherwise enter 0:")
input_num = int(text)
#Step 4: Determine whether it is too dry
if input_num == 1 :
        too_dry = True
else:
        too_dry = False
#Step 5: Write the boolean expression to determine whether it is both too hot and too dry
result = too_hot and too_dry
#Step 6: Print the result
if result == True :
        print("Yes! It is too hot and too dry.")
else:
        print("No! the weather condition 'too hot and too dry' is not met.")
