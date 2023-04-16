"""
Create a program that autocompletes a numerical array with 15 positions with the first
elements of the Fibonacci sequence:
    1 1 2 3 5 8 13 21 34 55 89 144 233 377 610 987
    0 1 2 3 4 5  6  7  8  9 10  11  12 13  14  15
"""

f_arr = []
n1 = 0
n2 = 1

f_arr.append(n1)
f_arr.append(n2)

for i in range(0, 14):
    n3 = n1 + n2
    n1 = n2
    n2 = n3
    f_arr.append(n3)

# print(f_arr)

for n in f_arr:
    print(n, end=" - ")

print("\n--------------------------------------------")

for i in range(0, 15):
    print(i, end=" -  ")
