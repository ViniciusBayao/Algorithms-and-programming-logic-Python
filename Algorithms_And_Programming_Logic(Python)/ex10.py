"""
Write an algorithm that reads the width and height of a wall, calculates and
show the area to be painted and the amount of paint needed for the job,
knowing that each liter of paint paints an area of 2 square meters.
"""
print("Calculating The area to be painted")
width = float(input("Type any width of a wall: "))
height = float(input("Type any height of a wall: "))
area = width * height
print(f"Area to be painted: {area}")
print(f"Amount of paint needed: {area / 2} liters")
