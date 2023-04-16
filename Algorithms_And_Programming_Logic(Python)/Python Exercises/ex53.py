"""
Make a program that reads the age and gender of 5 people, showing at the end:
a) How many men were registered;
b) How many women were registered;
c) The average age of the group;
d) The average age of men;
e) How many women are over 20 years old;
"""
m = 0
f = 0
average_group = 0
average_men = 0
w_over = 0
for i in range(1, 6):
    gender = input("Enter your gender: type M or F (both M and F are capitals): ").upper()
    age = int(input("Enter your age: "))
    if gender == "M":
        m += 1
        average_men += age
    elif gender == "F":
        f += 1
        if age > 20:
            w_over += 1
    average_group += age
print(f"Men registered: {m}")
print(f"Women registered: {f}")
print(f"Average age of the group: {average_group / 5}")
print(f"Average men age: {average_men / m}")
print(f"Number of Women over 20 years old: {w_over} ")
