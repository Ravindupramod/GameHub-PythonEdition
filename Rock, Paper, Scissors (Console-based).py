import random

def get_computer_choice():
    return random.choice(["rock", "paper", "scissors"])

def get_winner(player, computer):
    if player == computer:
        return "Draw"
    if (player == "rock" and computer == "scissors") or \
       (player == "paper" and computer == "rock") or \
       (player == "scissors" and computer == "paper"):
        return "Player"
    return "Computer"

def play_rps():
    player_choice = input("Enter rock, paper, or scissors: ").lower()
    computer_choice = get_computer_choice()
    print(f"Computer chose: {computer_choice}")
    
    winner = get_winner(player_choice, computer_choice)
    if winner == "Draw":
        print("It's a draw!")
    else:
        print(f"{winner} wins!")

play_rps()
