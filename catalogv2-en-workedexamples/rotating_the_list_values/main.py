#Step 1: Define the function
def rotate_left(lst):
        #Step 1.1: Store the value at the front in a local variable
        first = lst[0]
        #Step 1.2: Rotate the remaining values of the list to the left
        for i in range(len(lst)-1):
                lst[i] = lst[i + 1]
        #Step 1.3: Move the value at the front to the back of the list
        lst[len(lst)-1] = first
        return lst
#Step 2: Call the function
values =  [3, 8, 9, 8, 7, 5]
print("Original list:", values)
print("Rotated list: ", rotate_left(values))
