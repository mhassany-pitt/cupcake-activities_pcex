#Step 1: Read the number of rows in the inverted right triangle star pattern
N = int(input("Enter the number of rows in the inverted right triangle star pattern:"))
#Step 2: Print the rows in the star pattern, one by one
for i in range(1, N+1):
        #Step 2.1: Generate the asterisks in the i-th row
        row = ""
        for j in range(1, N-i+2):
                row = row + "*"
        #Step 2.2: Print the asterisks in the i-th row
        print(row)
