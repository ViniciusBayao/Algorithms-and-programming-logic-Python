"""
Make a program that reads 7 integers and at the end shows the sum
between them.
"""
i = 1
sum_num = 0
while i <= 7:
    number = int(input(f"Input a {i}° number: "))
    i += 1
    sum_num += i
print(f"The sum of the 7 integer numbers inserted is: {sum_num}")
