#Step 1: Define the function
def search_lists(lst1, lst2):
        #Step 1.1: Iterate through the values in the 2nd list
        for val2 in lst2:
                #Step 1.1.1: Print the value in the 2nd list if it exists in the 1st list
                if val2 in lst1:
                        print(val2, "exists in both list.")
#Step 2: Call the function
values_1 = [2.0, 11, 4, 5, 3, 3.5, 4, 10, 16]
values_2 =  [7, 11, 3]
search_lists(values_1, values_2)
