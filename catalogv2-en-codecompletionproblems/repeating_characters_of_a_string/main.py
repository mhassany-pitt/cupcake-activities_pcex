#Step 1: Define the function
def double_char(s):
        #Step 1.1: Assign initial value to the variable that we need for the new string
        new_s = ""
        #Step 1.2: Iterate through every other characters in the given string
        for i in range(0, len(s), 2) :
                #Step 1.2.1: Add the repeated character to the the new string
                new_s += s[i] * 2
        #String 1.3: Print the new string
        print(new_s)
#Step 2: Call the function
double_char("Hi There")
