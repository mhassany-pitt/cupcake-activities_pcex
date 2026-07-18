#Step 1: Define the function
def create_dictionary(std_lst, test_lst):
        #Step 1.1: Create an empty dictionary
        res_dict={}
        #Step 1.2: Update the dictionary entries as we iterate through the indexes in the given lists
        for i in range(len(std_lst)):
                if std_lst[i]  in res_dict:
                        res_dict[ std_lst[i] ].append( test_lst[i] )
                else:
                        res_dict[ std_lst[i] ] = [ test_lst[i] ]
        return res_dict
#Step 2: Call the function
names = ['Joe', 'Tom', 'Barbara', 'Sue', 'Sally', 'Joe', 'Sue']
scores=[10, 23, 13, 18, 12, 9, 15]
print(create_dictionary(names, scores))
