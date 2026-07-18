# Step 1: Define the function
def square(list):
#Step 1.1 :Iterate through the list and compute each value’s square value
        for i in range(len(list)):
                list[i] *= list[i]
        print(list)
#Step 2: Initiate the list
num_list = [2,3,4,5]
#Step 3: Call the function
square(num_list)
#Step 4: Print the list
print(num_list)
