#Step 1: Read the user input for the value of the first boolean variable (variable a)
text = input("Enter 1 if the value of the first boolean variable (variable a) is True, otherwise enter 0:")
input_num = int(text)
#Step 2: Determine whether the value of the first boolean variable (variable a) is True
if input_num == 1 :
        a = True
else:
        a = False
#Step 3: Read the user input for the value of the second boolean variable (variable b)
text = input("Enter 1 if the value of the second boolean variable (variable b) is True, otherwise enter 0:")
input_num = int(text)
#Step 4: Determine whether the value of the second boolean variable (variable b) is True
if input_num == 1 :
        b = True
else:
        b = False
#Step 5: Read the user input for the value of the third boolean variable (variable c)
text = input("Enter 1 if the value of the third boolean variable (variable c) is True, otherwise enter 0:")
input_num = int(text)
#Step 6: Determine whether the value of the third boolean variable (variable c) is True
if input_num == 1 :
        c = True
else:
        c = False
#Step 7: Write the boolean expression to determine whether all the three boolean variables have the same value
result = (a == b and b == c)
#Step 8: Print the result
if result == True :
        print("Yes! All the three boolean variables have the same value.")
else:
        print("No! Not all the variables have the same value.")
