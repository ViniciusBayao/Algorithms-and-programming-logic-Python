"""
Write a program that asks for the speed of a car. If the driver exceeds
80Km/h, display a message saying that the traffic cop gave a ticket for running above the speed allowed. In that case,
display the value of the speed ticket, charging R$5 for each Km above the permitted speed.
"""
car_speed = float(input('Type the speed of the car: '))
speed_ticket = 200
if car_speed > 80:
    print(f'You reached above the speed limit of 80km/h. You have received a ticket for running above the allowed'
          f'zone speed . You need to pay ${speed_ticket * 5}')
else:
    print(f'You not reached the speed limit. There is no problem.')
