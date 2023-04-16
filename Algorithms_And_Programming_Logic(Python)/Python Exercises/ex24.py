"""
Make an algorithm that asks the distance a passenger wants
travel in Km. Calculate the ticket price, charging $0.50 per km to
trips up to 200Km and $0.45 for longer trips.

"""
distance = float(input("What's the distance you want to travel in kilometers? "))
if distance >= 200:
    print(f"Distance in Kilometers: {distance:.2f} The ticket price is: ${0.50 * distance:.2f} dollars.")
else:
    print(f"Distance in kilometers: {distance:.2f} The ticket price is: ${0.50 * distance:.2f} dollars.")
