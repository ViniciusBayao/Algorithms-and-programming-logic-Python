"""
In an exclusive promotion for Women's Day, a store wants to give discounts
for everyone, but especially for women. Make a program that reads name,
gender and the amount of the customer's purchases and calculate the discounted price. Knowing
that:
 - Men get 5% of discount.
 - Women get 13% of discount.
"""
name = input("What's your name? ")
gender = input("What's you gender? M or F: ").upper()
purchase_price = float(input("What's the final price of your shopping? "))
men_disc = purchase_price - (purchase_price * 5) / 100
women_disc = purchase_price - (purchase_price * 13) / 100
if gender == "M":
    print(f"The discount for men is 5% and the total of your purchase is ${purchase_price:.2f}. The final total "
          f"value of your purchase, with the discount, is ${men_disc:.2f} dollars.")
elif gender == "F":
    print(f"The discount for women is 13% and the total of your purchase is ${purchase_price:.2f}. The final total "
          f"value of your purchase, with the discount, is ${women_disc:.2f} dollars.")
