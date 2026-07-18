# Step 1: Import math library
import math
# Step 2: Take the first input from the user
input_a = input("Enter the first integer:")
a = int(input_a)
# Step 3: Take the second input from the user
input_b = input("Enter the second integer:")
b = int(input_b)
# Step 3: Division
c = a/b
d = int(c)
# Check if d's type is integer and store the boolean result into the variable f
f = isinstance(d,int)
print(d)
print(f)
print(math.fabs(c))
