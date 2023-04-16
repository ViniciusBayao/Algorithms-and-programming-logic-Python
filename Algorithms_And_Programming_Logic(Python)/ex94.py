"""
Develop an application that has a procedure called
Fibonacci() which takes a single integer value as a parameter, indicating how many
terms of the sequence will be shown on the screen. Your procedure must receive
this value and show the quantity of requested elements.
Note: Use exercises 70 and 75 to help you with the solution
Ex:
Fibonacci(5) will generate 1 >> 1 >> 2 >> 3 >> 5 >> END
Fibonacci(9) will generate 1 >> 1 >> 2 >> 3 >> 5 >> 8 >> 13 >> 21 >> 34 >> END
"""

fibo_arr = []

n = 1


def fibonacci(terms):
    n1 = 0
    n2 = 1
    for i in range(terms):
        n3 = n1 + n2
        n1 = n2
        n2 = n3
        fibo_arr.append(n3)
    for number in fibo_arr:
        print(number, end=" ")


t = int(input("How many terms of Fibonacci sequence do you want to see?:  "))

fibonacci(t)

print("END", end=" ")
