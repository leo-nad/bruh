import random

# Function to get the computer's choice
def computer_choice():
    return random.choice(['rock', 'paper', 'scissors'])

# Function to determine the winner
def determine_winner(player, computer):
    if player == computer:
        return "It's a draw!"
    elif (player == 'rock' and computer == 'scissors') or \
         (player == 'paper' and computer == 'rock') or \
         (player == 'scissors' and computer == 'paper'):
        return "You win!"
    else:
        return "Computer wins!"

# Function to update the statistics in a file
def update_results(result):
    with open("results.txt", "a") as file:
        file.write(result + "\n")

# Function to read and display player statistics
def display_statistics():
    try:
        with open("results.txt", "r") as file:
            results = file.readlines()
            wins = results.count("You win!")
            losses = results.count("Computer wins!")
            draws = results.count("It's a draw!")
            total_games = len(results)

            print("\nPlayer Statistics:")
            print(f"Total games played: {total_games}")
            print(f"Wins: {wins}")
            print(f"Losses: {losses}")
            print(f"Draws: {draws}")
    except FileNotFoundError:
        print("\nNo statistics available. Play some games first.")

# Main game loop
def play_game():
    print("Welcome to Rock, Paper, Scissors!")
    while True:
        print("\nEnter your choice: rock, paper, or scissors (or 'quit' to exit).")
        player = input().lower()

        if player == 'quit':
            print("Thanks for playing!")
            break
        elif player not in ['rock', 'paper', 'scissors']:
            print("Invalid choice, please try again.")
            continue

        computer = computer_choice()
        print(f"\nComputer chose: {computer}")

        result = determine_winner(player, computer)
        print(result)
        
        update_results(result)

        display_statistics()

# Start the game
if __name__ == "__main__":
    play_game()
