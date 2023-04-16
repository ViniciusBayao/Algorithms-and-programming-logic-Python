"""
Develop an application that reads salary and gender for multiple employees.
At the end, show the total wages paid to men and the total paid to women. The program will ask the user if it wants to continue or not,
whenever you read an employee's data input.
"""
from itertools import count

avg_sal_m = 0
avg_sal_w = 0

for i in count():
    gender = input(f"Enter your gender: M or F (type using uppercase): ").upper()
    sal = float(input(f"Enter you salary: "))
    opt = input("Do you want to continue? Y or N(type in uppercase): ").upper()
    if opt == "Y":
        if gender == "M":
            avg_sal_m += sal
        elif gender == "F":
            avg_sal_w += sal
        else:
            print(f"Entry not recognized. Try Again.")
    elif opt == "N":
        break

print(f"Men total salary paid: ${avg_sal_m}")
print(f"Women total salary paid: {avg_sal_w}")
