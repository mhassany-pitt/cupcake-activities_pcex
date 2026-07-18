#Step 1: Define the function
def rotate_left_by_2(lst):
        #Step 1.1: Store the first two values of the list in local variables
        first = lst[0]
        second = lst[1]
        #Step 1.2: Rotate the remaining values of the list to the left by 2 position
        for i in range(len(lst)-2):
                lst[i] = lst[i + 2]
        #Step 1.3: Move the first two values of the list to the back of the list
        lst[len(lst)-2] = first
        lst[len(lst)-1] = second
        return lst
#Step 2: Call the function
values = [3, 8, 9, 8, 7, 5]
print("Original list:", values)
print("Rotated list: ", rotate_left_by_2(values))
