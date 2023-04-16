"""
Create a program that has a superAdder() function, which will receive two
numbers as a parameter, and then it will return the sum of all values in the
interval between received values.
Ex:
superAdder(1, 6) will add 1 + 2 + 3 + 4 + 5 + 6 and will return 21
superAdder(15, 19) will add 15 + 16 + 17 + 18 + 19 and will return 85
"""


def superAdder(n1, n2):
    sum_num = 0
    for i in range(n1, n2 + 1):
        sum_num += i
    return sum_num


x1 = int(input("Enter a first integer number: "))
x2 = int(input("Enter a second integer number: "))

s = superAdder(x1, x2)

print(s)
