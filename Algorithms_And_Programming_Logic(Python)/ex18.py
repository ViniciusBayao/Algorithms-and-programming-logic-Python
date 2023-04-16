"""
Write a program that reads a person's year of birth, calculate the age
of the person and then show whether the person can vote or not.
"""
import datetime  # import module datetime to get the current year

birth_year = int(input("What is the year of your birth? "))
date = datetime.date.today()
current_year = date.strftime("%Y")
age = int(current_year) - birth_year
if age > 16:
    print(f"You are {age} years old. You can vote!")
else:
    print(f"You are {age} years old. You can't vote yet.")
