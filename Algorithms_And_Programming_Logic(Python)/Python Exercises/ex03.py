"""
Create a program that reads the name and the salary of the employee showing a final message.
Example:
Name of the employee: Josh
Salary: $2000.00
The employee Josh has a salary of $2000.00 dollars.
"""

name = input('What is your name? ')
salary = float(input('How much is your salary? '))
print(f"Name of the employee: {name}")
print(f"Salary: {salary}")
print(f"The employee {name}, had a salary of ${salary} dollars.")
