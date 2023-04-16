"""
Create a program that reads several numbers from the keyboard and shows at the end the
sum between them.
Note: The program will be interrupted when the number 1111 is typed
"""
sum_num = 0
while True:
    number = int(input("Enter a number: "))
    if number == 1111:
        break
    else:
        sum_num += number

print(f"The sum on the entered numbers is: {sum_num}")
