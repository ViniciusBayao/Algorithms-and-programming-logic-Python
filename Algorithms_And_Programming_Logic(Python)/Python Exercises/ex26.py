"""
Write an algorithm that reads two integers and compares them, showing
one of the messages below:
 - The first value is the largest
 - The second value is the largest
 - There is no greater value, both are equal
"""
num_1 = int(input("Type a integer number: "))
num_2 = int(input("Type another integer number: "))
if num_1 > num_2:
    print(f"{num_1} is greater than {num_2}")
elif num_2 > num_1:
    print(f"{num_2} is greater than {num_1}")
else:
    print(f"{num_1} is equal to {num_2}")
