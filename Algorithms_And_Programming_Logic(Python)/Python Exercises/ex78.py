"""
Write a program that reads 15 numbers and stores them in an array. At the end,
show the entire array on the screen and then show in which positions they were
enter values that are multiples of 10.
"""

n = 0
arr_num = []

while n < 15:
    num = float(input("Enter a number: "))
    arr_num.append(num)
    n += 1

print(arr_num)

print(f"\nMultiples of ten: ")

for number in arr_num:
    if number % 10 == 0:
        print(number, end=" ")
