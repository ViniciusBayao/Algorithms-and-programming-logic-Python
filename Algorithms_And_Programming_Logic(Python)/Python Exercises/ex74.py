"""
Create a program that autocompletes (using logic, not just
assigning directly) a numerical vector with 10 positions, as follows:
    5 3 5 3 5 3 5 3 5 3
    0 1 2 3 4 5 6 7 8 9
"""
from random import choice

count = 0

arr = []

l = [3, 5]

while count < 10:
    arr.append(choice(l))
    count += 1

# print(arr)

n = 0

for n in arr:
    print(n, end="  ")

print(f"\n-----------------------------")

for i in range(0, 10):
    print(i, end="  ")
