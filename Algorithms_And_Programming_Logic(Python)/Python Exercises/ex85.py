"""
Write an algorithm that reads the name, gender and salary of 5 employees and
store this data in three arrays. At the end, show a listing containing
only the data of female employees earning more than R$5,000.
"""

name_arr = []
gender_arr = []
salary_arr = []
w_name = []
w_salary = []

for i in range(5):
    name = input("Enter your name: ")
    name_arr.append(name)
    gender = input("Enter your gender: M or F(type using uppercase)").upper()
    gender_arr.append(gender)
    salary = float(input("Enter your salary: "))
    salary_arr.append(salary)
    if salary > 5000 and gender == "F":
        w_name.append(name)
        w_salary.append(salary)

print(f"Women who earn more than 5$.000: name: ")
for name in w_name:
    print(name)

print(f"earn: ")
for salary in w_salary:
    print(f"$ {w_salary} dollars.")
