"""
Write an algorithm that fills an array of 30 positions with numbers between 1 and
15 drawn by the computer. After that, ask the user to enter a
number (key) and your program should show which positions this key was
found. Also show how many times the key was drawn.
"""
import random

arr_drawn = []

position = 0

for i in range(30):
    n = random.randint(1, 15)
    arr_drawn.append(n)

print(arr_drawn)

user_num = int(input("Enter a number(key) to check if it's in the array: "))

for number in arr_drawn:
    if number == user_num:
        position = arr_drawn.index(number)
        break
print(f"The number entered {user_num} exists in the array and it was found in the position "
      f"{position}")
