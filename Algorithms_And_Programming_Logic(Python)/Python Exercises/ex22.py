"""
Write an algorithm to read a person's age and tell if can take driver's license or not.
"""
age = int(input("How old are you? "))
if age >= 16:
    print(f"You are {age} years old and you can take drivers license.")
else:
    print(f"You are {age} years old and you can't take your drivers license.")
