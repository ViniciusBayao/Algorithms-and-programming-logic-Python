"""
Write a program that displays the following count on the screen:
    100 95 90 85 80 ... 0 It's over!
"""
for count in range(100, -4, -5):
    print(count, end=" ")
print("It's over!")
