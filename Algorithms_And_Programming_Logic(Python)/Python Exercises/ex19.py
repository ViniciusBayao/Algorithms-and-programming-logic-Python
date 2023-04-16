"""
Create an algorithm that reads a student's name and two grades, calculates their
average and show on the screen. At the end, analyze the average and show if the student had or
not a good performance (if it was above average 7.0).
"""
student_name = input("What is your name? ")
grade_1 = float(input("Type the grade number one: "))
grade_2 = float(input("Type the grade number two: "))
average = (grade_1 + grade_2) / 2
if average > 7:
    print(f"You had a good performance at the exams. Your average is {average}.")
else:
    print(f"You not had a good performance at the exams. Your average is {average}.")
