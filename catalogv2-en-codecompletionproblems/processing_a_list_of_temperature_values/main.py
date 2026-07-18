#Step 1: Read the number of days that we have to enter their temperature data
num_days = int(input("Enter the number of temperature values that will be entered: "))
#Step 2: Read the temperature values
temps = []
for i in range(num_days):
        val = float(input("Enter the temperature: "))
        temps.append(val)
#Step 3: Create a list that contains the days that are above 32 degrees Fahrenheit
days_above_32 = []
for i in range(len(temps)) :
        if temps[i] > 32:
                days_above_32.append("Day " + str(i+1))
#Step 4: Print the result
print("Days above 32 degrees Fahrenheit:", days_above_32)
