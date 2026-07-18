#Step 1: Define the function
def rotate_right(lst):
        #Step 1.1: Store the value at the end of the list in a local variable
        last = lst[len(lst)-1]
        #Step 1.2: Rotate the remaining values of the list to the right
        for i in range(len(lst)-1, 0, -1):
                lst[i] = lst[i - 1]
        #Step 1.3: Move the value at the end to the front of the list
        lst[0] = last
        return lst
#Step 2: Call the function
values = [3, 8, 9, 8, 7, 5]
print("Original list:", values)
print("Rotated list: ", rotate_right(values))
