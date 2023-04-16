"""
Write a program to calculate the reduction in the lifetime of a
smoker. Ask the number of cigarettes smoked per day and how old he/she is.
already smoked. Consider that a smoker loses 10 minutes of life with each cigarette. Calculate
how many days of life a smoker will lose and display the total in days.
"""
qtd_cig = int(input('How many cigarettes do you smoke per day?:  '))
qtd_years_smoke = int(input('How many years you smoke: '))
calc_years = 365 * qtd_years_smoke
calc_days = (qtd_cig * 10) * 1440 / calc_years
print(f'You already lost{calc_days} days by smoking cigarettes')
