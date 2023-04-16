"""
Write an algorithm that asks the user for a positive integer
any and show a count up to that value:
Ex: Enter a value: 35
Count: 0 1 2 3 4 5 6 7 ... 33 34 35 It's over!
"""
number = int(input("Input a positive integer: "))
print(f"Number entered: {number}")
for i in range(0, number + 1):
    print(i, end=" ")
print("It's over!")
