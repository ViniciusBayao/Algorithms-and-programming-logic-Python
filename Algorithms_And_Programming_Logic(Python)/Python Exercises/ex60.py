"""
Develop an algorithm that reads the name, age, and gender of multiple people.
The program will ask whether the user wants to continue or not. At the end, show:
a) The name of the oldest person;
b) The name of the youngest woman;
c) The average age of the group;
d) How many men are over 30;
e) How many women are under 18;
"""
age_usr = 0
avg_age = 0
m_over_30 = 0
w_under_18 = 0
oldest = 0
count = 0
younger_w = 0
name_usr = ""
name_young_w = ""
w_age = 0
while True:
    name = input("Enter your name: ")
    age = int(input("Enter your age: "))
    gender = input("Enter your gender: M or F(type M or F in upper scale): ").upper()
    avg_age += age
    if gender == "F":
        w_age = age
        if younger_w < w_age:
            younger_w = w_age
            name_young_w = name
            if age < 18:
                w_under_18 += 1
    elif gender == "M":
        if age > 30:
            m_over_30 += 1
    if gender == "M" or gender == "F" and count == 1:
        oldest = age
        if age > oldest:
            oldest = age
            name_usr = name

    opt = input("Continue? Y or N(type Y or N in upper scale): ").upper()
    count += 1
    if opt == "N":
        break
print(f"The oldest person registered is {oldest} years old its the name is {name_usr}.")
print(f"The youngest Woman registered is {younger_w} years old and her name is {name_young_w}")
print(f"The average age of the group is: {(avg_age / count):.2f} years old.")
print(f"Number of men over 30 years old: {m_over_30}")
print(f"Number of Women under 18 years old: {w_under_18}")
