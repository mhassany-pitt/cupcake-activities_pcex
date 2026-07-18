#Step 1: Read the temperature for today and yesterday
text = input("Enter the yesterday's temperature: ")
yesterday = float(text)
text = input("Enter the today's temperature: ")
today = float(text)
#Step 2: Read the humidity for today and yesterday
text = input("Enter yesterday's humidity: ")
humidity_yesterday = float(text)
text = input("Enter today's humidity: ")
humidity_today = float(text)
#Step 3: Warn the user about the changes in the temperature
if today < yesterday :
        print("It is getting colder!")
else :
        if today > yesterday :
                #Step 3.1: Determine and warn the user about the changes in humidity when it is getting warmer
                if humidity_today < humidity_yesterday :
                        print("It is getting warmer but less humid!")
                elif humidity_today > humidity_yesterday :
                        print("It is getting warmer and more humid!")
                else :
                        print("It is getting warmer but humidity has not changed!")
        else :
                print("Temperature is the same as yesterday!")
