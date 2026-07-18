#Step 1: Define a 7x4 matrix that stores the number of medals won by seven countries
medal_counts = [[ "CAN", 1, 0, 1 ],
                                [ "CHN", 1, 1, 0 ],
                                [ "GER", 0, 0, 1 ],
                                [ "KOR", 1, 0, 0 ],
                                [ "JPN", 0, 1, 1 ],
                                [ "RUS", 0, 1, 1 ],
                                [ "USA", 1, 1, 0 ]]
#Step 2: Print the header of the output table
print("{:>4s}{:>3s}{:>3s}{:>3s}{:>4s}".format("Name","G","S","B","All"))
#Step 3: Iterate through the rows in the medal counts matrix
for i in range(len(medal_counts)):
        #Step 3.1: Assign initial values to variables we need for printing row i
        line = "{:>4s}".format(medal_counts[i][0])
        row_total = 0
        #Step 3.2: Iterate through the columns that have medal counts
        for j in range(1, len(medal_counts[0])):
                #Step 3.2.1: Append medal counts to the content of row i
                line += "{:>3d}".format(medal_counts[i][j])
                #Step 3.2.2: Update the row total for row i
                row_total += medal_counts[i][j]
        #Step 3.3: Add the row total to the content of the output table for row i
        line += "{:>3d}".format(row_total)
        #Step 3.4: Print the content of the output table for row i
        print(line)
