"""
Write a program that automatically fills a numeric array with 8
positions as below:
    999 999 999 999 999 999 999 999
    0    1   2   3    4  5   6   7
"""
arr = []

for i in range(8):
    arr.append(999)

for n in arr:
    print(n, end="   ")

print(f"\n")

for i in range(8):
    print(i, end="     ")
