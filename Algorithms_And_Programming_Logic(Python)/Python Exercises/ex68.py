"""
Create a program that reads the sex and weight of 8 people, using the structure
"for". At the end, show on screen:
a) How many women were registered;
b) How many men weigh more than 100 kg;
c) Average weight among women;
d) The highest weight among men.
"""
Avg_w = 0
M_weight = []
count_w = 0
count_m = 0
for i in range(8):
    gender = input("Enter your gender: M or F (type using upper scale): ").upper()
    weight = float(input("Enter your weight in Kg: "))
    if gender == "F":
        count_w += 1
        Avg_w += weight
    if gender == "M":
        count_m += 1
        M_weight.append(weight)

print(f"Number o Women registered: {count_w} ")
print(f"Number of men registered: {count_m}")
print(f"Average weight of Women registered: {Avg_w / count_w}")
print(f"Highest weight among men: {max(M_weight)} ")
