"""
Create a Rock-Paper-Scissors game
"""
import random
"""
# First Example:

print("----Rock-Paper-Scissors Game----")
player1_option = input("Player 1 Choose: Rock, paper or Scissors: ").upper()
player2_option = input("Player 2 Choose: Rock, paper or scissors: ").upper()
if player1_option == "ROCK" and player2_option == "PAPER":
    print("Player 2 wins.")
elif player1_option == "PAPER" and player2_option == "ROCK":
    print("Player 1 Wins.")
elif player1_option == "ROCK" and player2_option == "SCISSORS":
    print("Player 1 Wins.")
elif player1_option == "SCISSORS" and player2_option == "ROCK":
    print("Player 2 Wins.")
elif player1_option == "PAPER" and player2_option == "SCISSORS":
    print("Player 2 Wins.")
elif player1_option == "SCISSORS" and player2_option == "PAPER":
    print("Player 1 Wins.")
else:
    print("Invalid entry. Try again.")
"""
"""
# Second Example:

print("----Rock-Paper-Scissors Game----")
player_option = input("Please, choose an option: Rock, paper or Scissors: ").upper()
list_game = ["ROCK", "PAPER", "SCISSORS"]
computer_option = random.choice(list_game)
print(f"You chose: {player_option} and computer chose: {computer_option}")
if player_option == computer_option:
    print(f"Both players selected {player_option}. It's a tie.")
elif player_option == "ROCK":
    if computer_option == "SCISSORS":
        print("Rock smashes scissors! You Win!")
    else:
        print("Paper covers rock! You lose.")
elif player_option == "PAPER":
    if computer_option == "ROCK":
        print("Paper covers rock! You Win!")
    else:
        print("Scissors cuts paper! You lose.")
elif player_option == "SCISSORS":
    if computer_option == "PAPER":
        print("Scissors cuts paper! You Win!")
    else:
        print("Rock smashes scissors! You lose.")
"""
