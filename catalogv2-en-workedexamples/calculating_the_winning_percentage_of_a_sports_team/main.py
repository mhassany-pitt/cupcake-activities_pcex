#Step 1: Assign initial values to the variables which we need for this program
total_games = 12
#Step 2: Read the number that the user enters
text = input("Enter the number of games that the sports team won in the tournament: ")
wins = int(text)
#Step 3: Validate the user input, ask for a valid input as long as the user enters an invalid number; otherwise stop
while wins < 0 or wins > total_games :
        text = input("Enter the number of games that the sports team won in the tournament: ")
        wins = int(text)
#Step 4: Calculate and print the percentage of games won by a team
ratio = wins / total_games
print("Winning percentage:", ratio)
