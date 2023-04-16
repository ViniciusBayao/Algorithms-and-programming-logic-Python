"""
Create a program that reads the gender and age of multiple people. The program goes
ask each person whether the user wants to continue or not. At the end, show:
a) what is the greatest age read;
b) how many men were registered;
c) how old is the youngest woman;
d) what is the average age of men;
"""
oldest = 0
count = 0
count_m = 0
younger_w = 0
avg_m = 0
w_age = 0
while True:
    gender = input(f"Enter your gender: M or F (type using uppercase): ").upper()
    age = int(input("Enter your age: "))
    if gender == "F" and count == 1:
        w_age = age
        if w_age < age:
            w_age = age
    if gender == "M" or gender == "F" and count == 1:
        oldest = age
        if age > oldest:
            oldest = age
    if gender == "M":
        count_m += 1
        avg_m += age
    opt = input(f"Continue? Y or N (type using uppercase): ").upper()
    count += 1
    if opt == "N":
        break

print(f"Oldest age registered: {oldest}")
print(f"Number of men registered: {count_m}")
print(f"Younger Women age: {w_age}")
if count > 0:
    print(f"Average age of men: {avg_m / count}")
"""

"""
