"""
Improve exercise 96 by creating, in addition to the average() function, another function
call situation(), which will return to the main program if the student is
APPROVED, in RECOVERY or FAILED. This new function will receive as
parameter the result returned by the average() function.
"""


def average(g1, g2):
    avg = (g1 + g2) / 2
    return avg


def situation(avg):
    if avg <= 5.0:
        return "Student Failed."
    elif 6.0 <= avg < 7.0:
        return "Student in Recovery."
    else:
        return "Student Approved."


grade1 = float(input("Enter the grade number one: "))
grade2 = float(input("Enter the grade number two: "))

res = average(grade1, grade2)

sit = situation(res)

print(f"Average: {res}")

print(f"Student situation: {sit}")
