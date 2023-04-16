"""
The car rental company needs your help to charge for its services. Write
a program that asks for the number of kilometers traveled by a rented car and the
number of days for which it was rented. Calculate the total price to be paid,
knowing that the car costs R$90 per day and R$0.20 per km driven.
"""
km = float(input('Type the distance in km which the car has been driven: '))
days = int(input('How many days this car was rent? : '))
print(f'The total price to pay is: ${(km * 0.20) + (days * 90)}')
