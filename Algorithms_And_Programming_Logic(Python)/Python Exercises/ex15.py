"""
Create a program that reads the number of days worked in a month and displays the
salary of an employee, knowing that he works 8 hours a day and earns R$25
per hour worked.
"""
work_days = int(input('Type How many days you worked this month: '))
print(f'The salary of this month, with {work_days} days worked is: ${200 * work_days}')
