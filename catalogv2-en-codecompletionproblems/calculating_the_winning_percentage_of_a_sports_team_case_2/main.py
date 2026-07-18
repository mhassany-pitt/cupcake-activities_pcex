#Step 1: Read the number of games in the tournament
text = input("Enter the number of games in the tournament: ")
total_games = int(text)
#Step 2: Validate the user input for the number of games in the tournament, ask for a valid input as long as the user enters an invalid number; otherwise stop
while total_games <= 0 :
        text = input("Enter the number of games in the tournament: ")
        total_games = int(text)
#Step 3: Read the number of games that the sports team won in the tournament
text = input("Enter the number of games that the sports team won in the tournament: ")
wins = int(text)
#Step 4: Validate the user input for the number of games that the sports team won in the tournament, ask for a valid input as long as the user enters an invalid number; otherwise stop
while wins < 0 or wins > total_games :
        text = input("Enter the number of games that the sports team won in the tournament: ")
        wins = int(text)
#Step 5: Calculate and print the percentage of games won by a team
ratio = wins / total_games
print("Winning percentage:", ratio)
