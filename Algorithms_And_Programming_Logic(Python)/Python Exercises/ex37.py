"""
A company needs to readjust the wage of its employees, giving an
increase according to some factors. Make a program that reads the current wage,
the employee's gender and how many years the employee has been with the company.
At the end, show your new wage, based on the following table:
- Women:
 - less than 15 years with the company: +5%;
 - from 15 to 20 years with the company: +12%;
 - more than 20 years with the company: +23%;
- Men:
 - less than 20 years with the company: +3%;
 - from 20 to 30 years with the company: +13%;
 - more than 30 years in the company: +25%;
"""
current_wage = float(input("Input your current wage: "))
gender = input("Input your gender: Type M or F: ").upper()
years_worked = int(input("How long have you been working for the company? "))
if gender == "M":
    if years_worked < 15:
        print(f"Your new wage is: ${current_wage + (current_wage * 0.05)}")
    elif 15 <= years_worked < 20:
        print(f"Your new wage is: ${current_wage + (current_wage * 0.12)}")
    else:
        print(f"Your new wage is: ${current_wage + (current_wage * 0.23)}")
elif gender == "F":
    if years_worked < 20:
        print(f"Your new wage is: ${current_wage + (current_wage * 0.03)}")
    elif 20 <= years_worked < 30:
        print(f"Your new wage is: ${current_wage + (current_wage * 0.13)}")
    else:
        print(f"Your new wage is: ${current_wage + (current_wage * 0.25)}")
else:
    print(f"The input doesn't match the expected entry.")
