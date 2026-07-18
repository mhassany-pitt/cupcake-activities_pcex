#Step 1: Define the function
def search_lists(lst1, lst2):
        #Step 1.1: Create a list that we need to store the number of matches
        counts = [0] * len(lst2)
        #Step 1.2: Iterate through the values in the 2nd list
        for val2 in lst2:
                #Step 1.2.1: Iterate through the values in the 1st list
                for val1 in lst1:
                        #Step 1.2.1.1: Increment the number of matches for val2 if we find a match for that
                        if val2 == val1:
                                counts[ lst2.index(val2) ] += 1
        print("The list that contains the number of times each element in the 2nd list appears in the 1st list:", counts)
#Step 2: Call the function
values_1 = [2.0, 11, 11, 4, 5, 3, 3, 3.5, 4, 10, 16]
values_2 =  [7, 11, 3]
search_lists(values_1, values_2)
