#Step 1: Assign initial values to the variables which we need for this program
num = 1234
#Step 2: Print the digits of the integer from right to left
while num > 0 :
        #Step 2.1: Get the last digit in the integer
        last_digit = num % 10
        #Step 2.2: Print the extracted digit
        print(last_digit)
        #Step 2.3: Remove the last digit from the integer
        num = num // 10
