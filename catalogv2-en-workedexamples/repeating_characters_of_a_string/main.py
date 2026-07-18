#Step 1: Define the function
def double_char(s):
        #Step 1.1: Assign initial value to the variable that we need for the new string
        new_s = ""
        #Step 1.2: Iterate through the characters in the given string
        for char in s:
                #Step 1.2.1: Add the repeated character to the the new string
                new_s += char * 2
        #String 1.3: Print the new string
        print(new_s)
#Step 2: Call the function
double_char("Hi There")
