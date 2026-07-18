# Step 1: Define the terminating condition
def gcd2(a, b):
        if b == 0:
                return a
                # Step 3: Recursion
        else:
                return gcd2(b, a%b)
print(gcd2(12,14))
