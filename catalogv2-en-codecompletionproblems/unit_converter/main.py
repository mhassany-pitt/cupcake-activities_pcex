#Step 1: Assign initial values to the variables which we need for this program
base = 32
conversion_factor = 5 / 9
#Step 2: Read the input Fahrenheit value
text = input("Enter the Fahrenheit value: ")
fahrenheit_temp = int(text)
#Step 3: Compute the Celsius equivalent of the Fahrenheit value
celsius_temp = (fahrenheit_temp - base) * conversion_factor
print("Fahrenheit Temperature:" , fahrenheit_temp)
print("Celsius Equivalent:" , celsius_temp)
