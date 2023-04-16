"""
Create a program that reads the name and age of 9 people and stores these
values in two arrays, in related positions. At the end, show a listing
containing only the data of underage.
"""

arr_name = []
arr_age = []
under_age = []
under_name = []
count = 0
c = 1

while count < 9:
    print(f"Person n{c}: ")
    name = input("Enter your name: ")
    arr_name.append(name)
    age = int(input("Enter your age: "))
    arr_age.append(age)
    count += 1
    c += 1
    if age < 18:
        under_name.append(name)
        under_age.append(age)

print(f"Underage information's: ")

print(f"Underage entered: {under_age}")
print(f"Names: {under_name}")
