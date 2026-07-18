#Step 1: Read the number of days that we have to enter their temperature data
num_days = int(input("Enter the number of temperature values that will be entered: "))
#Step 2: Read the temperature values
temps = []
total = 0
for i in range(num_days):
        val = float(input("Enter the temperature: "))
        temps.append(val)
        total += val
#Step 3: Calculate the average temperature
average = 0
if num_days == 0:
        print("No temperature values were entered.")
else:
        average = total / num_days
#Step 4: Count the number of the days that are above the average temperature
above = 0
for x in temps:
        if x > average:
                above += 1
#Step 5: Display the results
print("Average temperature:", average)
print(above, "days above average.")
