"""
Create a game where the computer will draw a number between 1 and 5 and the
player will try to find out what was the amount drawn.
"""
import random
number_computer = random.randint(1, 5)
players_guess = int(input("Try to guess a number from 1 to 5: "))
if players_guess == number_computer:
    print(f"Number drawn by computer: {number_computer}. Your guess is correct!")
else:
    print(f"Number drawn by computer: {number_computer}. Your guess is incorrect. Please try again.")
