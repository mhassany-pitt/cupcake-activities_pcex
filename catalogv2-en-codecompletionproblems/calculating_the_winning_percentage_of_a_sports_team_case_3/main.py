#Step 1: Assign initial values to the variables which we need for this program
total_games = 12
#Step 2: Read the number of games that the sports team won in the tournament
text = input("Enter the number of games that the sports team won in the tournament: ")
wins = int(text)
#Step 3: Validate the user input for the number of wins, ask for a valid input as long as the user enters an invalid number; otherwise stop
while wins < 0 or wins > total_games :
        text = input("Enter the number of games that the sports team won in the tournament: ")
        wins = int(text)
#Step 4: Read the number of games that the sports team tied in the tournament
text = input("Enter the number of games tied: ")
ties = int(text)
#Step 5: Validate the user input for the number of ties, ask for a valid input as long as the user enters an invalid number; otherwise stop
while ties < 0 or total_games < (ties + wins) :
        text = input("Enter the number of games tied: ")
        ties = int(text)
#Step 6: Calculate and print the percentage of games won by a team, counting ties as half wins
ratio = ( wins + ties // 2) / total_games
print("Winning percentage:", ratio)
