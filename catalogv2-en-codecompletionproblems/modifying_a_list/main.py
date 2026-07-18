#Step 1: Define and initialize the list
lst = [1, 2, 3, 4, 5, 6]
#Step 2: Iterate through the pairs of adjacent elements in the list
for i in range(0, len(lst), 2):
        #Step 2.1: Swap the element at index i with the element at index i+1
        temp = lst[i]
        lst[i] = lst[i+1]
        lst[i+1] = temp
#Step 3: Print the list
print(lst)
