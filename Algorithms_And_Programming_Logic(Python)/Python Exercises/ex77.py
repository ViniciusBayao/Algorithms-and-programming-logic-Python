"""
Write a program that reads 7 people's names and stores them in an array. At the end, show a
list with all the names entered, in reverse order the one in which they were informed.
"""
n = 0
names = []

while n < 7:
    name = input("Enter your name: ")
    names.append(name)
    n += 1

# print(names)

print(list(reversed(names)))
