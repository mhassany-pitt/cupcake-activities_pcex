#Step 1: Define the function
def calculate_list_average(lst):
        #Step 1.1: Assign initial value to the variable which we need for this program
        total = 0
        #Step 1.2: Iterate through the list values and add each value to the running total
        for x in lst:
                total += x
        #Step 1.3: Calculate and print the average of the list values
        if len(lst) == 0 :
                print("The list has no values.")
        else :
                average = total / len(lst)
                print("Average is:", average)
#Step 2: Call the function
values = [6, 15, 9, 12, 1, 8]
calculate_list_average(values)
