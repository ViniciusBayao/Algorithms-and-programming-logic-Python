"""
Write an algorithm that reads the age of several students in a class. the program
will stop when age 999 is entered. At the end, show how many students
exist in the class and what is the average age of the group.
"""

count_students = 0
avg_age = 0

while True:
    age = int(input("Enter student's age: "))
    if age != 999:
        count_students += 1
        avg_age += age
    else:
        break

print(f"Total students: {count_students}")
if count_students > 0:
    print(f"Average age of the students: {avg_age / count_students}")
