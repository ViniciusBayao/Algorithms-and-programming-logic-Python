"""
Create a program that autocompletes a numerical vector with 10 positions, as follows:
    5  10 15 20 25 30 35 40 45 50
    0  1  2  3  4  5  6  7  8  9
"""
arr = []
for i in range(5, 51, 5):
    arr.append(i)

print(arr)
