"""
Write a program using the “for” structure that reads an integer
positive and display a count from 0 to the typed value on the screen:
Ex: Enter a value: 9
Count: 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, END!
"""
n = int(input("Enter a positive integer number:  "))
for i in range(0, n + 1):
    print(i, end=" ")
