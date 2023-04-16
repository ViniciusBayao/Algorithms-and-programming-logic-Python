"""
Create a program that reads the ages of 8 people and stores them in an array. At the
end, show:
a) What is the average age of the people registered;
b) In which positions do we have people over 25 years old;
c) What was the oldest age entered (there may be repetitions);
d) In which positions do we type the highest age.
"""
n = 0
age_arr = []
age_25 = []

while n < 8:
    age_arr.append(input("Enter your age: "))
    n += 1

for a in age_arr:
    if a > "25":
        age_25.append(age_arr.index(a))

print(f"Average ages: {sum(age_arr) / len(age_arr)}")
print(f"Positions with people over 25 years old: {age_25}")
print(f"The oldest age entered: {max(age_arr)}")
print(f"Position entered the oldest age: {age_arr.index(max(age_arr))}")
