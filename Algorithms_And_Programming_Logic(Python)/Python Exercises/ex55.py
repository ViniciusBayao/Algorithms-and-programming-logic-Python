"""
Let's improve the game we played in exercise 32.
now, the computer will draw a number between 1 and 10 and the player will have 4
attempts to try to get it right.
"""
import random
computer_choose = random.randint(1, 10)
for i in range(1, 5):
    number = int(input("Enter a number(Try to guess a number from one to ten): "))
    if number == computer_choose:
        print(f"Your guess is correct. The number draw by computer was {number}")
        break
    else:
        print(f"You guess is incorrect. Try again(You have {4 - i} chances left).")

print(f"The number drawn by computer was {computer_choose}")
