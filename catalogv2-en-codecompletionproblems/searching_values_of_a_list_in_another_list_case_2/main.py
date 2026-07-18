#Step 1: Define the function
def search_lists(lst1, lst2):
        #Step 1.1: Iterate through the values in the 2nd list
        count = 0
        for val2 in lst2:
                #Step 1.1.1: Iterate through the values in the 1st list
                for val1 in lst1:
                        #Step 1.1.1.1: Increment the number of matches if we find a match
                        if val2 == val1:
                                count += 1
        print("Total number of times the elements in the 2nd list appear in the 1st list is", count)
#Step 2: Call the function
values_1 = [2.0, 11, 11, 4, 5, 3, 3, 3.5, 4, 10, 16]
values_2 =  [7, 11, 3]
search_lists(values_1, values_2)
