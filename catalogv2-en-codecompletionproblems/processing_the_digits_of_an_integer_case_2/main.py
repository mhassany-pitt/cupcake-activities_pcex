#Step 1: Assign initial values to the variables which we need for this program
num = 1234
total = 0
#Step 2: Sum up the digits of the integer
while num > 0 :
        #Step 2.1: Get the last digit in the integer
        last_digit = num % 10
        #Step 2.2:?Add the last digit to the sum of digits so far
        total = total + last_digit
        #Step 2.3: Remove the last digit from the integer
        num = num // 10
        print("last digit:", last_digit, ", sum:", total, ", integer:", num)
print("The sum of the digits:", total)
