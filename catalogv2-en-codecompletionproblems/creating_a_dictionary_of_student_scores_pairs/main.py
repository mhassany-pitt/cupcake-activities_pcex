#Step 1: Define the function that creates the dictionary
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
#Step 2: Define the function that calculates the average of each student's scores
def average(new_dict):
        #Step 2.1: Iterate through the students in the dictionary
        for std_name in new_dict :
                #Step 2.1.1: Iterate through the list of student's scores, add each score to the running total
                total = 0;
                for score in new_dict[std_name]:
                        total+= score
                #Step 2.1.2: Calculate and print the average of student's scores
                average = total/len(new_dict[std_name])
                print(std_name, average)
#Step 3: Call the functions
names = ['Joe', 'Tom', 'Barbara', 'Sue', 'Sally', 'Joe', 'Sue']
scores=[10, 23, 13, 18, 12, 9, 15]
average( create_dictionary(names, scores) )
