"""
Make an algorithm that reads a given year and shows whether it is a
LEAP year or not.
"""

year = int(input("Type one year: "))
if (year % 4 == 0) or (year % 400 == 0) and (year % 100 != 0):
    print(f"The year {year} is a Leap year.")
else:
    print(f"The year {year} is not a Leap year.")
