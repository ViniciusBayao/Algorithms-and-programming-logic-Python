"""
Develop an application that displays the result of the following expression on the screen:
450 + 400 + 350 + 300 + ... + 50 + 0
"""
sum_numbers = 0
for i in range(500, 0, -50):
    print(i, end=" ")
    sum_numbers += i
print(f"The result of the expression above is: {sum_numbers}")
