"""
Create a program that improves the function hello_world()from the previous question
to show a personalized message, passed as a parameter.
Ex: When calling the function hello_world("Learning Python!") appears:
+-------=======------+
 Learning Python
+-------=======------+
"""

msg = "Learning Python"


def hello_world(message):
    print(message)


print("+-------=======------+")
hello_world(msg)
print("+-------=======------+")
