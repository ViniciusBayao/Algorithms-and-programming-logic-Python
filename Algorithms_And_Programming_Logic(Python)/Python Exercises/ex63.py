"""
Create a program that reads several numbers.
At each loop, ask if the user wants to continue or not. No ending, show on
screen:
a) The sum of all values;
b) What was the smallest amount entered;
c) The mean of all values;
d) How many values are even?
"""
sum_values = 0
min_value = 0
avg_values = 0
count = 0
even = 0
while True:
    n = float(input("Enter a number: "))
    opt = input("Continue? Y or N (type using uppercase): ")
    count += 1
    sum_values += n
    avg_values += n
    if n % 2 == 0:
        even += 1
    if count == 1:
        min_value = n
        if min_value < n:
            min_value = n
    if opt == "N":
        break

print(f"The sum of all values: {sum_values}")
print(f"The smallest value entered: {min_value}")
print(f"Average of values: {avg_values / count}")
print(f"Even values: {even}")
