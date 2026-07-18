#Step 1: Assign initial values to the variables which we need for this program
num = 15
divisor = num-1
#Step 2: Find the largest divisor of the number
while num % divisor != 0 :
        divisor -= 1
print("The largest divisor of", num, "is", divisor)
