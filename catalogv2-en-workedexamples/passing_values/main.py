# Step 1: Define the function
def increment(x):
        # Step 1.1: Print x’s original memory address
        print(f"Initial address of x: {id(x)}")
        # Step 1.2: Increase x by 1
        x += 1
        # Step 1.3: Print x’s current memory address
        print(f"Final address of x: {id(x)}")
#Step2: Initiate n
n = 9001
print(f"Initial address of n: {id(n)}")
#Step2: Call the funtion
increment(n)
print(f"Final address of n: {id(n)}")
