"""
Create an algorithm that reads the start value of the count, the end value and the
increment, then showing all the values in the range:
Ex: Enter the first Value: 3
Enter the last Value: 10
Enter the increment: 2
Count: 3 5 7 9 It's over!
"""
first_value = int(input("Input a positive integer: "))
second_value = int(input("Input another positive integer: "))
increment = int(input("Input an increment: "))
for i in range(first_value, second_value, increment):
    print(i, end=" ")
print("It's over!")
