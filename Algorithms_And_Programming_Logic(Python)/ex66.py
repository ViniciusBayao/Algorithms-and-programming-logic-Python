"""
Write a program that reads any number and prints the multiplication table of that number.
number, using the “for” structure.
Ex: Enter a value: 5
5 x 1 = 5
5 x 2 = 10
5 x 3 = 15...
"""
print(f"------Multiplication Table-------")
n = int(input("Enter a positive integer number: "))
for i in range(1, 11):
    print(f"{n} x {i} = {n * i}")
