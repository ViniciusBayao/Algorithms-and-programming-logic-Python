"""
Write a program that reads an integer and prints whether it is even or odd.
"""
number = int(input("Type a integer number: "))
if number % 2 == 0:
    print(f"The number {number} is even.")
else:
    print(f"The number {number} is odd.")
