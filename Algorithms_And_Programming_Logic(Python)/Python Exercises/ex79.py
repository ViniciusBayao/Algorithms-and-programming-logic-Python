"""
Develop a program that reads 10 integers and stores them in an array.
At the end, show which are the even numbers that were entered and in which
positions they are stored.
"""

count = 0

arr_num = []
odd_numbers = []
even_numbers = []

while count < 10:
    number = int(input("Enter an integer number: "))
    count += 1
    arr_num.append(number)

print(arr_num)

for n in arr_num:
    if n % 2 == 0:
        even_numbers.append(n)
    else:
        odd_numbers.append(n)


print("Even numbers entered: ")
print(even_numbers)
print("Odd numbers entered: ")
print(odd_numbers)
