"""
Create an algorithm that reads the age of 10 people, showing at the end:
a) What is the average age of the group?
b) How many people are over 18 years old;
c) How many people are under 5 years old;
d) What was the oldest age read;
"""
average_age = 0
people_over = 0
people_under = 0
oldest = 0
for i in range(1, 11):
    age = int(input(f"People {i} - How old are you?: "))
    if i == 1:
        oldest = age
    if age > oldest:
        oldest = age
    if age > 18:
        people_over += 1
    if age < 5:
        people_under += 1
    average_age += age

average_age = average_age / 10
print(f"Average age of the group: {average_age}")
print(f"People over eighteen years old: {people_over}")
print(f"People under five years old: {people_under}")
print(f"Oldest age entered: {oldest}")
