"""
Create a program that reads 6 integers and at the end shows how many of them
are even and how many are odd.
"""
sum_even = 0
sum_odd = 0
for i in range(1, 8, 1):
    num = int(input(f"\nInsert a {i}° number: "))
    if num % 2 == 0:
        print(f"Even: {num}", end=" ")
        sum_even += 1
    else:
        print(f"Odd: {num}", end=" ")
        sum_odd += 1
print(f"\nThere are {sum_even} even numbers and {sum_odd} odd numbers.")
