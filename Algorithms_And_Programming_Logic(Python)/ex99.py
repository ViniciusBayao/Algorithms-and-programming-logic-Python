"""
Make a program that has a function called powNum(), which will receive
two numerical parameters (base and exponent) and will calculate the result of the
exponentiation.
Ex: powNum(5,2) will calculate 52 = 25
"""


def powNum(n1, n2):
    return pow(n1, n2)


b = int(input("Enter a positive integer number as base: "))
e = int(input("Enter a positive integer number as exponent: "))

res = powNum(b, e)

print(res)
