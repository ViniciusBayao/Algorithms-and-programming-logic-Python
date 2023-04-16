"""
Redo exercise 91, only now in the form of a Greater() function, but make a
adaptation that will receive THREE numbers as a parameter and will return what was the
biggest among them.
"""


def greater(num1, num2, num3):
    return max(num1, num2, num3)


n1 = float(input("Enter a number: "))
n2 = float(input("Enter another number: "))
n3 = float(input("Enter another number: "))

res = greater(n1, n2, n3)
print(res)
