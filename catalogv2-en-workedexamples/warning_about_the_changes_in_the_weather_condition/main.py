#Step 1: Read the temperature for today and yesterday
text = input("Enter the yesterday's temperature: ")
yesterday = float(text)
text = input("Enter the today's temperature: ")
today = float(text)
#Step 2: Warn the user about the changes in the temperature
if  today < yesterday :
        print("It is getting colder!")
else :
        if  today > yesterday :
                print("It is getting warmer!")
        else :
                print("Temperature is the same as yesterday!")
