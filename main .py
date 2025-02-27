import random

# Function to get the computer's choice
def get_computer_choice():
    choices = ['rock', 'paper', 'scissors']
    return random.choice(choices)

# Function to determine the winner
def determine_winner(player_choice, computer_choice):
    if player_choice == computer_choice:
        return "It's a tie!"
    elif (player_choice == 'rock' and computer_choice == 'scissors') or \
         (player_choice == 'paper' and computer_choice == 'rock') or \
         (player_choice == 'scissors' and computer_choice == 'paper'):
        return "You win!"
    else:
        return "You lose!"

# Function to save results in a file
def save_results(player_choice, computer_choice, result):
    with open('game_results.txt', 'a') as file:
        file.write(f"Player: {player_choice}, Computer: {computer_choice}, Result: {result}\n")

# Function to show player statistics
def show_statistics():
    try:
        with open('game_results.txt', 'r') as file:
            lines = file.readlines()
            wins = lines.count("You win!")
            losses = lines.count("You lose!")
            ties = lines.count("It's a tie!")
            
            total_games = len(lines)
            print("\nPlayer Statistics:")
            print(f"Total games played: {total_games}")
            print(f"Wins: {wins}")
            print(f"Losses: {losses}")
            print(f"Ties: {ties}")
    except FileNotFoundError:
        print("No game results found.")

# Main function to play the game
def play_game():
    print("Welcome to Rock, Paper, Scissors!")
    
    while True:
        print("\nEnter your choice: rock, paper, or scissors (or 'quit' to exit)")
        player_choice = input().lower()
        
        if player_choice == 'quit':
            print("Goodbye!")
            break
        
        if player_choice not in ['rock', 'paper', 'scissors']:
            print("Invalid choice. Please choose rock, paper, or scissors.")
            continue
        
        computer_choice = get_computer_choice()
        print(f"Computer chose: {computer_choice}")
        
        result = determine_winner(player_choice, computer_choice)
        print(result)
        
        save_results(player_choice, computer_choice, result)
        
        show_statistics()

# Start the game
play_game()
