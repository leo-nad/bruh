import random
def get_user_choice():
    while True:
        user_choice = input ("Enter rock, paper or scissors").lower()
        if user_choice in ['rock', 'paper', 'scissors']; return user_choice
else: print("invalid input. please enter 'rock', 'paper', or 'scissors'.") 
