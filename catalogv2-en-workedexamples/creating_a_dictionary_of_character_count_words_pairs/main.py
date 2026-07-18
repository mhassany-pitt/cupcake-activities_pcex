#Step 1: Define the function
def create_dictionary(s):
        #Step 1.1: Create an empty dictionary
        counts = {}
        #Step 1.2: Update the dictionary entries as we iterate through the string characters
        for char in s:
                if char in counts:
                        counts[char] += 1
                else:
                        counts[char] = 1
        #Step 1.3: Print the dictionary
        print("The character counts for", s)
        for char in counts:
                print(char, ":", counts[char])
#Step 2: Call the function
s = input("Enter a string: ")
create_dictionary(s)
