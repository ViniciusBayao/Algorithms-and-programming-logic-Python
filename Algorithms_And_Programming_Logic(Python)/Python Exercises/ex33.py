"""
Write a program to approve or reject the bank loan for the purchase
of a house. The program will ask for the value of the house, the buyer's salary and
in how many years he will pay. Calculate the amount of the monthly installment, knowing that
it cannot exceed 30% of salary or else the loan will be denied.
"""
value_of_house = float(input("What is the value of the house? "))
sal = float(input("Input your salary? "))
years_payment = float(input("How many years you gonna pay the loan? "))
month = years_payment * 12
installment = value_of_house / month
if installment > sal * 0.3:
    print(f"Salary: ${sal:.2f} dollars, value of the house: ${value_of_house:.2f} dollars;")
    print(f"The mortgage payment exceeded 30% of your salary. Sorry, bank loan rejected.")
else:
    print(f"Salary: ${sal:.2f} dollars, value of the house: ${value_of_house:.2f} dollars;")
    print(f"The mortgage payment does not exceeded 30% of your salary. Your bank loan is approved.")
    print(f"Amount of the monthly installment: ${installment:.2f} dollars.")
