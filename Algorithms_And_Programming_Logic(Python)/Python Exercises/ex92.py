"""
Create a logic that reads an integer and passes it to a procedure
evenorodd() that will check and show on the screen if the value passed as
parameter is EVEN or ODD.
"""


def evenorodd(number):
    if number % 2 == 0:
        print("The number {number} is Even!")
    else:
        print("The number {number} is Odd!")


num = int(input("Enter an integer number: "))
evenorodd(num)
