"""
Develop a program that reads an employee's name, salary,
how many years he has worked at the company and show his new salary, readjusted from
according to the following table:
 - Up to 3 years with the company: 3% increase
 - between 3 and 10 years: increase of 12.5%
 - 10 years or more: 20% increase
"""
name = input("Type your name: ")
salary = float(input("What's your salary: "))
years_worked = int(input("How many years have you worked at the company: "))
if years_worked < 3:
    print(f"Your new salary is: ${(salary + (salary * 3) / 100):.2f} dollars.")
elif 3 <= years_worked < 10:
    print(f"Your new salary is: ${(salary + (salary * 12.5) / 100):.2f} dollars.")
else:
    print(f"Your new salary is: ${(salary + (salary * 20) / 100):.2f} dollars.")
