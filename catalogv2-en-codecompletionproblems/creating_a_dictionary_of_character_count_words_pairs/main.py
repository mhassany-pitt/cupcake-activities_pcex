#Step 1: Define the function
def create_dictionary(s):
        #Step 1.1: Create an empty dictionary
        res_dict = {}
        #Step 1.2: Split the given string into words
        s = s.lower()
        words = s.split()
        #Step 1.3: Update the dictionary entries as we iterate through the words
        for word in words:
                if word[0] in res_dict:
                        if word not in res_dict[ word[0] ] :
                                res_dict[ word[0] ].append(word)
                else:
                        res_dict[ word[0] ] = [ word ]
        #Step 1.4: Print the dictionary
        for char in res_dict:
                print(char, ":", res_dict[char])
#Step 2: Call the function
s = input("Enter a string: ")
create_dictionary(s)
