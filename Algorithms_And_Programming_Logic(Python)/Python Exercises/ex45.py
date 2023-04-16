"""
The previous program (Ex44) will have a problem when we enter the first value
bigger than the last one. Solve this problem with code that works on any
situation.
"""
first_value = int(input("Input a positive integer: "))
second_value = int(input("Input another positive integer: "))
increment = int(input("Input an increment: "))
if first_value > second_value:
    x = first_value
    first_value = second_value
    second_value = x
    for i in range(first_value, second_value + 1, increment):
        print(i, end=" ")
print("It's over!")
