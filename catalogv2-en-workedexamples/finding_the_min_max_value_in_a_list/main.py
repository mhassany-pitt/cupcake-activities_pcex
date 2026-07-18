#Step 1: Define and initialize the list
values = [5, 8, 4, 78, 95, 12, 1, 0, 6, 35, 46]
#Step 2: Set the first value to be the maximum value so far.
max_value = values[0]
#Step 3: Iterate through the remaining values in the list and decide which one is the maximum value
for i in range(1, len(values)):
        # Step 3.1: Determine if the element at index i is the maximum value so far
        if (values[i] > max_value):
                max_value = values[i]
#Step 4: Print the maximum value in the list
print("Maximum value:", max_value)
