"""
Write a program that reads the width and length of a field
rectangular, calculating and displaying its area in m². the program also needs to show
the classification of this land, according to the list below:
 - Below 100m² = POPULAR LAND
 - Between 100m² and 500m² = MASTER LAND
 - Above 500m² = VIP LAND
"""
width = float(input("Enter the width of a field in meters: "))
length = float(input("Enter the length of a field in meters: "))
area = width * length
if area < 100:
    print(f"Area of {area} meters squared. Popular Land!")
elif 100 <= area < 500:
    print(f"Area of {area} meters squared. Master Land!")
else:
    print(f"Area of {area} meters squared. Vip Land!")
