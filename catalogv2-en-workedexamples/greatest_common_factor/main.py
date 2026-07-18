# Step 1: Define the starting condition
def Recurgcf(a, b):
        low = min(a, b)
        high = max(a, b)
# Step 2: Define the terminating condition
        if low == 0:
                return high
        elif low == 1:
                return 1
        # Step 3: Recursion
        else:
                return Recurgcf(low, high%low)
print(Recurgcf(12,14))
