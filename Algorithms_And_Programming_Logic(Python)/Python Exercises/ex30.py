"""
Redo algorithm 25, adding the feature of showing what type
of triangle will be formed:
 - EQUILATERAL: all sides equal
 - ISOSCELES: two equal sides
 - Scalene: all different sides
"""
length_1 = int(input("Type the length of the first line segment: "))
length_2 = int(input("Type the length of the second line segment: "))
length_3 = int(input("Type the length of the third line segment: "))
if length_1 < length_2 + length_3 and length_2 < length_1 + length_3 and length_3 < length_2 + length_1:
    print("It's a triangle.")
    if length_1 == length_2 == length_3:
        print("And it's equilateral.")
    elif length_1 == length_2 or length_2 == length_3 or length_3 == length_1:
        print("And it's isosceles.")
    else:
        print("And it's scalene.")
else:
    print("It's not a triangle.")
