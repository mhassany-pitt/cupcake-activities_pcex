#Step 1: Define the function
def calculate_list_sum(lst):
        #Step 1.1: Assign initial value to the variable which we need for this program
        total = 0
        #Step 1.2: Iterate through the list values and add each value to the running total
        for x in lst:
                total += x
        #Step 1.3: Print the sum of the list values
        print("The sum of all values in the list:", total)
#Step 2: Call the function
values = [6, 15, 9, 12, 1, 8]
calculate_list_sum(values)
