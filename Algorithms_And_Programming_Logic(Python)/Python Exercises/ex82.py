"""
Write an algorithm that reads the grades of 10 students in a class and stores them in
an array. At the end, show:
a) What is the class average?
b) How many students are over the class average;
c) What was the highest grade typed;
d) In which positions does the highest note appear?
"""

grade_arr = []
stds_over = 0
count = 1

for i in range(10):
    grade_arr.append(float(input(f"Enter the {count}° grade: ")))
    count += 1

for g in grade_arr:
    if g > sum(grade_arr) / len(grade_arr):
        stds_over += 1


print(f"Average grade of the class: {sum(grade_arr) / len(grade_arr)}")
print(f"Number of students that are over the class average: {stds_over}")
print(f"The highest grade entered was: {max(grade_arr)}")
print(f"Position of the highest grade in the array: {grade_arr.index(max(grade_arr))}")
