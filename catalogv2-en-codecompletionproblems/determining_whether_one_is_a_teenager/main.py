#Step 1: Define the function
def check_age():
        #Step 1.1: Ask for a valid input as long as the input could not be processed; otherwise stop
        processed = False
        while not processed :
                s = input("Enter the name and age, separated by a colon:")
                #Step 1.1.1: Split the given string into the name and age
                lst = s.split(":")
                #Step 1.1.2: Enclose the code that might throw an exception within the try block
                try:
                        name = lst[0]
                        age = int(lst[1])
                        if age >= 13 and age <= 19 :
                                print(name + " is a teenager.")
                        else:
                                print(name + " is not a teenager.")
                        processed = True
                #Step 1.1.3: Handle all possible exceptions that may be thrown in the try block
                except IndexError :
                        print("Error! Separate the name and age by a colon.")
                except ValueError :
                        print("Error! Age must be an integer.")
#Step 2: Call the function
check_age()
