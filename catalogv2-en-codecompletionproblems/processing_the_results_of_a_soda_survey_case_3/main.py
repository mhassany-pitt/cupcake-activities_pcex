#Step 1: Define a 4x10 two-dimensional list
ratings_data = [[3, 4, 5, 2, 1, 4, 3, 2, 4, 4],
                                [2, 4, 3, 4, 3, 3, 2, 1, 2, 2],
                                [3, 5, 4, 5, 5, 3, 2, 5, 5, 5],
                                [1, 1, 1, 3, 1, 2, 1, 3, 2, 4]]
#Step 2: Get the dimensions of the list that stores the ratings data
num_sodas = len(ratings_data)
num_respondents = len(ratings_data[0])
#Step 3: Create a list to store the sum of rating of each soda flavor
soda_sum = [0] * num_sodas
#Step 4: Create a list to store the sum of rating of each respondent
respondent_sum = [0] * num_respondents
#Step 5: Iterate through the sodas
for i in range(num_sodas):
        #Step 5.1: Iterate through the respondents
        for j in range(num_respondents):
                #Step 5.1.1: Update sum of ratings given to soda i+1
                soda_sum[i] += ratings_data[i][j]
                #Step 5.1.2: Update sum of ratings from respondent j+1
                respondent_sum[j] += ratings_data[i][j]
#Step 6: Calculate and print the average rating for each soda
print("Averages:")
for i in range(num_sodas):
        print("Soda # {:d} : {:.2f}".format((i+1), soda_sum[i]/num_respondents))
#Step 7: Calculate and print the average rating for each respondent
for j in range(num_respondents):
        print("Respondent # {:d} : {:.2f}".format((j+1), respondent_sum[j]/num_sodas))
