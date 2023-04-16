"""
Develop an algorithm that reads two values from the keyboard and passes the values
for an adder() function that will calculate and display the sum between them.
"""


def adder(num1, num2):
    print(num1 + num2)


number_1 = int(input("Enter an integer number: "))
number_2 = int(input("Enter another integer number:  "))

print(f"The sum between {number_1} and {number_2} is: ")
adder(number_1, number_2)
