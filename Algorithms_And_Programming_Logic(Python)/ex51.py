"""
Make an application that reads the price of 8 products. At the end, show on screen
which was the highest and which was the lowest price entered.

"""
i = 0
print("Type 9 prices of products below: ")
max_value = 0
min_value = 0
while i < 8:
    i += 1
    n = int(input(f"Type the {i}° price of a product: "))
    if i == 1:
        max_value = n
        min_value = n
    if n > max_value:
        max_value = n
    elif n < min_value:
        min_value = n

print(max_value)
print(min_value)

"""
i = 0
print("Type 8 proces of products below: ")
prices = []
while i < 8:
    i += 1
    n = int(input(f"Type the {i}° price of a product: "))
    prices.append(n)

print(f"The highest price entered was: {(max(prices)):.2f}")
print(f"The lowest price entered was: {(min(prices)):.2f}")
"""