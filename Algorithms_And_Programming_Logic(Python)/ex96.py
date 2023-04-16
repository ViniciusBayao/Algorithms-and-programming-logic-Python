"""
Create a program that has a average() function, which will receive the 2 grades from
a student and return their average to the main program.
"""


def average(g1, g2):
    return (g1 + g2) / 2


grade1 = float(input("Enter the grade number one: "))
grade2 = float(input("Enter the grade number two: "))

n = average(grade1, grade2)

print(n)
