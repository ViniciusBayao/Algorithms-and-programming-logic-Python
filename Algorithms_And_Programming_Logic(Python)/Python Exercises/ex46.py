"""
Create a program that calculates and displays on the screen the result of the sum between 6 +
8 + 10 + 12 + 14 + ... + 98 + 100.
"""
i = 4
sum_numbers = 0
while i < 100:
    i += 2
    sum_numbers += i
    print(i, end=" ")
print(".")
print(f"The sum of these numbers are: {sum_numbers}")
