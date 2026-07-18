#Step 1: Define the function
def rotate_right_by_2(lst):
        #Step 1.1: Store the last two values of the list in local variables
        last = lst[len(lst)-1]
        second_last = lst[len(lst)-2]
        #Step 1.2: Rotate the remaining values of the list to the right by 2 position
        for i in range(len(lst)-1, 1, -1):
                lst[i] = lst[i - 2]
        #Step 1.3: Move the last two values of the list to the front of the list
        lst[0] = second_last
        lst[1] = last
        return lst
#Step 2: Call the function
values = [3, 8, 9, 8, 7, 5]
print("Original list:", values)
print("Rotated list: ", rotate_right_by_2(values))
