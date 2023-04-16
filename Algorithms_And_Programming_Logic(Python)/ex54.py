"""
Develop an application that reads the weight and height of 7 people, showing
at the end:
a) What was the average height of the group?
b) How many people weigh more than 90 kg;
c) How many people who weigh less than 50 kg are shorter than 1.60 m;
d) How many people who measure more than 1.90 m weigh more than 100 kg;
"""
i = 1
more_90 = 0
less_50_and_160 = 0
more_100_and_190 = 0
h_average = 0
while i < 7:
    print(f"Person number {i}:")
    height = float(input("Enter your height in meters: "))
    weight = float(input("Enter your weight: "))
    if weight > 90:
        more_90 += 1
    elif weight < 50 and height < 1.60:
        less_50_and_160 += 1
    elif height > 1.90 and weight > 100:
        more_100_and_190 += 1

    h_average += height
    i += 1

print(f"Height average of the group: {(h_average / 7):.2f} meters.")
print(f"Number of people who weigh more than 90Kg: {more_90}")
print(f"Number of people who weigh less than 50 kg are shorter than 1.60 m: {less_50_and_160} ")
print(f"Number of people who weigh more than 100Kg and measure more than 1.90m: {more_100_and_190} ")
