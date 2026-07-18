#Step 1: Define the function
def check_product_code():
        #Step 1.1: Assign initial values to the variables that we need for counts
        valid = 0
        banned = 0
        #Step 1.2: Ask for a valid input as long as the user does'nt enter STOP; otherwise stop
        code = input("Enter product code: ")
        while ( code != "STOP") :
                #Step 1.2.1: Enclose the code that might throw an exception within the try block
                try :
                        zone = code[9]
                        valid += 1
                        if zone == "R" :
                                banned += 1
                #Step 1.2.2: Handle all possible exceptions that may be thrown in the try block
                except IndexError :
                        print("Improper code length.")
                code = input("Enter product code: ")
        #Step 1.3: Print the result
        print("# of valid codes entered:", valid)
        print("# of banned codes entered:", banned)
#Step 2: Call the function
check_product_code()
