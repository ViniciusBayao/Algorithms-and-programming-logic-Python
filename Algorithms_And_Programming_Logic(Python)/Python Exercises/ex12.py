"""
Create a program that reads the price of a product, calculates and displays your
PROMOTIONAL PRICE, with 5% discount.
"""

price = float(input("Type the price of a product: "))
discount = price - (price * 5) / 100 
print(f"The product with a discount of 5% costs: ${discount} dollars")
