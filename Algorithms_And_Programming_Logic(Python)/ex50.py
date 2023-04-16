"""
Develop a program that draws 20 numbers between 0 and 10 and
show on screen:
a) What were the numbers drawn?
b) How many numbers are above 5
c) How many numbers are divisible by 3?
"""
import random
drawn = []
greater_five = []
div_three = []
for i in range(1, 21):
    drawn.append(random.randint(0, 10))

print(f"Numbers drawn: ")
for n in drawn:
    print(f"{n}", end=" ")

print(f"\nNumbers greater than 5:")
for n in drawn:
    if n > 5:
        print(f"{n}", end=" ")

print(f"\nNumbers divisible by 3: ")
for n in drawn:
    if n % 3 == 0:
        print(f"{n}", end=" ")
