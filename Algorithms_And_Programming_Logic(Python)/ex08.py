"""
Write a program that reads a distance in meters and displays the values.
relative to other measures.
Ex:
Enter a distance in meters: 185.72
The distance of 85.7m corresponds to:
0.18572Km
1.8572Hm
18,572 Dam
1857.2dm
18572.0cm
185720.0mm
"""

meters = float(input("Type any distance in meters: "))
print(f"The distance of {meters} meters is equivalent to: ")
print(f"{meters / 1000} Km")
print(f"{meters / 100} Hm")
print(f"{meters / 10} Dam")
print(f"{meters * 10} dm")
print(f"{meters * 100} cm")
print(f"{meters * 1000} mm")