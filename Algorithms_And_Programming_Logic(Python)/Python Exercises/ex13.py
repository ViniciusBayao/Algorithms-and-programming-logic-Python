"""
Write an algorithm that reads an employee's salary, calculates and displays the new salary with a 15% increase.
"""
sal = float(input('Type your salary: '))
new_sal = sal + ((15 * sal) / 100)
print(f'Your new Salary with 15% of increase is now: ${new_sal}')
