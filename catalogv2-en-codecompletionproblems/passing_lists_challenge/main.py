# Step 1: Define the function
def Fahrenheit(c_list):
#Step 1.1 :Iterate through the list and compute each value’s Fahrenheit value
        for i in range(len(c_list)):
                c_list[i] = (c_list[i]*1.8)+32
# Step 2: Initiate the list
celsius_list = [25, 3, 40, -5]
# Step 3: Call the function
Fahrenheit(celsius_list)
# Step4: Print the Fahrenheit values
print('The converted Fahrenheit temperature is:',celsius_list)
