"""
Develop a program that reads the first term and common difference of a
AP (Arithmetic Progression), showing on the screen the first 10 elements of the AP and
the sum of all values in the sequence.
"""
a1 = int(input(f"Enter the first term of an arithmetic progression: "))
d = int(input(f"Enter the common difference: "))
sum_elements = 0
arth_prog = []
for i in range(1, 11):
    an = a1 + (i - 1) * d
    arth_prog.append(an)

print(f"The first 10 elements of this AP are: ")
for a in arth_prog:
    print(a, end=" ")
print(f"The sum of the numbers is: {sum(arth_prog)}")
