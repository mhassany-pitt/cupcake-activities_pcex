#Step 1: Define the function
def count_hi(s):
        #Step 1.1: Assign initial value to the variable that we need for the counts
        count = 0
        #Step 1.2: Iterate through the characters in the given string
        for i in range(len(s)-3):
                #Step 1.2.1: Increment the counts by 1 if we find a match
                if s[i:i+2].lower() == "hi" and s[i+3].lower() == "t":
                        count += 1
        #Step 1.3: Return the counts
        return count
#Step 2: Call the function
print(count_hi("hiatc?Hi ho hIx"))
