"""
Redo exercise 90, only now in the form of the adder() function, which will
receive two parameters and will return the result of the sum between them to the
main program.
"""


def adder(n1, n2):
    return n1 + n2


number1 = int(input("Enter a positive integer: "))
number2 = int(input("Enter another positive integer: "))

x = adder(number1, number2)
print(x)
