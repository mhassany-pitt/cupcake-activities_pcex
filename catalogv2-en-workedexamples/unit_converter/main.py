#Step 1: Assign initial values to the variables which we need for this program
base = 32
conversion_factor = 9 / 5
#Step 2: Read the input Celsius value
text = input("Enter the Celsius value: ")
celsius_temp = int(text)
#Step 3: Compute the  Fahrenheit equivalent of the Celsius value
fahrenheit_temp = celsius_temp * conversion_factor + base
print("Celsius Temperature:" , celsius_temp)
print("Fahrenheit Equivalent:" , fahrenheit_temp)
