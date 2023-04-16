"""
Make a program that has a procedure called counter() that receives
three values as a parameter: the start, end and increment of a count. O
main program must request the typing of these values and pass them to the
procedure, which will show the count on the screen.
"""

numbers_generate = []


def counter(start, end, increment):
    for n in range(start, end, increment + 1):
        numbers_generate.append(n)
    for number in numbers_generate:
        print(number, end=" ")


s = int(input("Enter a positive integer number as the start parameter of a count: "))
e = int(input("Enter a positive integer number as the end parameter of a count: "))
i = int(input("Enter a positive integer number as the increment parameter of a count: "))

counter(s, e, i)
print("End", end=" ")
