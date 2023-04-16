"""
The Body Mass Index (BMI) is a calculated value based on height and body weight.
a person's weight. According to the BMI value, we can classify the
individual within certain ranges.
 - under 18.5: Underweight
 - between 18.5 and 25: ideal weight
 - between 25 and 30: Overweight
 - between 30 and 40: Obesity
 - over 40: Morbid obesity
Note: BMI is calculated using the expression weight/height² (weight divided by the square
from height)
"""
weight = float(input("What is you weight in Kg: "))
height = float(input("What is you height in meters: "))
BMI = weight / (height ** 2)
if BMI < 18.5:
    print(f"Your BMI is: {BMI:.2f}. Classification: Underweight.")
elif 18.5 <= BMI < 25:
    print(f"You BMI is: {BMI:.2f}. Classification: Ideal Weight.")
elif 25 <= BMI < 30:
    print(f"Your BMI is :{BMI:.2f}. Classification: Overweight.")
elif 30 <= BMI < 40:
    print(f"Your BMI is: {BMI:.2f}. Classification: Obesity.")
else:
    print(f"Your BMi is: {BMI:.2f}. Classification: Morbid Obesity.")
