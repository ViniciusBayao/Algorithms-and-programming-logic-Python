"""
A car rental company needs to charge for its services. O
Renting a car cost $90 per day for a popular car and $150 per day for a
luxury car. In addition, the customer pays per miles travelled. make a program
that reads the type of rented car (popular or luxury), how many days of rent and
how many miles have been travelled. At the end show the price to be paid according to the
following table:
 - Popular cars ($90 per day rental):
 - Up to 100 miles travelled: $ 0.20 per mile;
 - Over 100 miles travelled: $ 0.10 per mile;
 - Luxury cars (R$150 per day rental):
 - Up to 200 miles travelled: $ 0.30 per mile;
 - Over 200 miles travelled: $ 0.25 per mile;

"""
print("-----Car-Rental-----")
car_model = input("What is the model of the car you want to rent? Type P for popular and L for luxury: ").upper()
days = float(input("how many days of rent? "))
miles = float(input("how many miles were traveled? "))
if car_model != "P" and car_model != "L":
    print(f"Input does not match any  model. Try again!")
else:
    if car_model == "P" and miles <= 100:
        print(f"Total price: $ {(90 * days * (miles * 0.20)):.2f} dollars.")
    elif car_model == "P" and miles > 100:
        print(f"Total price: $ {(90 * days * (miles * 0.10)):.2f} dollars.")
    if car_model == "L" and miles <= 200:
        print(f"Total price: $ {(150 * days * (miles * 0.30)):.2f} dollars.")
    elif car_model == "L" and miles > 200:
        print(f"Total price: $ {(150 * days * (miles * 0.25)):.2f} dollars.")
