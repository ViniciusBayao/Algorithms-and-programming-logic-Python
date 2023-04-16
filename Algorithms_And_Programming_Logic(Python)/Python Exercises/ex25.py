"""
Create a program that reads the length of three-line segments.
Analyze their lengths and say if it is possible to form a triangle with these
straight. Mathematically, for three segments to form a triangle, the length
on each side must be less than the sum of the other two.

"""
length_1 = int(input("Type the length of the first line segment: "))
length_2 = int(input("Type the length of the second line segment: "))
length_3 = int(input("Type the length of the third line segment: "))
if length_1 < length_2 + length_3 and length_2 < length_1 + length_3 and length_3 < length_2 + length_1:
    print("It's a triangle.")
else:
    print("It's not a triangle.")
