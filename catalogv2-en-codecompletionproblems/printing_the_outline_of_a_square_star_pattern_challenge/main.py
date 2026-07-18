# Step 1: Read the size of the square star pattern
size = int(input("Enter size of side of square :"))
# Step 2: Print the rows in the star pattern, one by one
for i in range(size):
        # Step 2.1: Check if the current row is the first or the last one
        if i == 0 or i == size - 1:
                for k in range(size):
                        print("*", end = "")
        else:
                print("*", end = "")
                # Step 2.2: Print other rows pattern.
                for j in range(size - 2):
                        print(" ", end = "")
                print("*", end="")
        # Step 3: Print the next line
        print()
