"""
Create a program that reads two grades from a student and calculates their average,
showing a message at the end, according to the average reached:
 - Average up to 4.9: FAILED
 - Average between 5.0 and 6.9: RECOVERY
 - Average 7.0 or higher: PASSED
"""
grade_1 = float(input("Enter the grade of the first exam: "))
grade_2 = float(input("Enter the grade of the second exam: "))
average_grade = (grade_1 + grade_2) / 2
if average_grade <= 4.9:
    print(f"Average grade: {average_grade:.1f} Result: failed.")
elif 5 <= average_grade <= 6.9:
    print(f"Average grade: {average_grade:.1f} Result: Recovery.")
else:
    print(f"Average grade: {average_grade:.1f} Result: Passed.")
