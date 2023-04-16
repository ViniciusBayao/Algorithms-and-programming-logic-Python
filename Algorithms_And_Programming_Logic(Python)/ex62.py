"""
Write a program that reads the age of
many people. At each loop, you must ask the user if he wants or
do not continue to enter data. In the end, when the user decides to stop, show
on the screen:
a) How many ages were entered;
b) What is the average between the ages entered;
c) How many people are 21 or older.
"""
count = 0
avg_age = 0
age_21 = 0

while True:
    age = int(input("Enter your age: "))
    opt = input("Do you want to continue? Y or N (type using uppercase): ").upper()
    count += 1
    avg_age += age
    if age >= 21:
        age_21 += 1
    if opt == "N":
        break

print(f"Number of ages entered: {count}")
print(f"Average age: {avg_age / count}")
print(f"Number of people aged twenty-one years or older: {age_21}")
