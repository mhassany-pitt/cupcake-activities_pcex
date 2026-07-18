# Step 1: Read the size of the square star pattern
size = int(input("Enter size of side of square :"))
# Step 2: Print the rows in the star pattern, one by one
for i in range(size):
        # Step 2.1: Generate the asterisks in the corresponding row
        for j in range(size):
                # Step 2.2: Print the asterisks in each row
                print("*", end = "")
        # Step 3: Print the next line
        print()
