"""
Create a program that improves the function hello_world from the previous question
to show a personalized message, passed as a parameter at least four times.
Ex: When calling the function hello_world("Learning python") appears:
+-------=======------+
 Learning Python
 Learning Python
 learning Python
 Learning Python
+-------=======------+
"""

msg = "Learning Python"


def hello_world(message):
    print(f"{message}\n" * 4)


print("+-------=======------+")
hello_world(msg)
print("+-------=======------+")
