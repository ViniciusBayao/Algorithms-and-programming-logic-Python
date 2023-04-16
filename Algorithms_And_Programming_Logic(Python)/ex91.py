"""
Develop an algorithm that reads two values from the keyboard and passes them
values for a larger() function that will check which one is the largest and
show it on the screen. If the two values are the same, show a message
reporting this feature.
"""


def larger(number1, number2):
    if number1 > number2:
        print(number1)
    else:
        print(number2)


num1 = int(input("Enter an integer number: "))
num2 = int(input("Enter another integer number: "))
print(f"Greatest Number: ")
larger(num1, num2)
