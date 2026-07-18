#Step 1: Assign initial values to the variables which we need for this program
num = 1234
reverse = 0
#Step 2: Reverse the digits of the integer mathematically
while num > 0 :
        #Step 2.1: Get the last digit in the integer
        last_digit = num % 10
        #Step 2.2:?Append the last digit to reverse
        reverse = (reverse * 10) + last_digit
        #Step 2.3: Remove the last digit from the integer
        num = num // 10
        print("last digit:", last_digit, ", reverse:", reverse, ", integer:", num)
print("The reversed integer is:", reverse)
