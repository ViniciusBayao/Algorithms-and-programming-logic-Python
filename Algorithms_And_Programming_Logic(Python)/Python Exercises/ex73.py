"""
Create a program that autocompletes a numerical vector with 10 positions, as follows:
    9 8 7 6 5 4 3 2 1 0
    0 1 2 3 4 5 6 7 8 9
"""
arr = []

for i in range(9, -1, -1):
    arr.append(i)

for n in arr:
    print(n, end=" ")

print("\n--------------------")

for i in arr:
    print(arr.index(i), end=" ")
