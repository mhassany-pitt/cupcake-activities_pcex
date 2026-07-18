#Step 1: Assign initial values to the variables which we need for this program
num = 15
divisor = 2
#Step 2: Find the smallest divisor of the number
while num % divisor != 0 :
        divisor += 1
print("The smallest divisor of", num, "is", divisor)
