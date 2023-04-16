"""
A healthy living program wants to give points for physical activities that can
be exchanged for cash. The system works like this:
 - Each hour of physical activity in the month is worth points
 - up to 10 hours of activity per month: earn 2 points per hour
 - from 10h to 20h of activity in the month: earn 5 points per hour
 - over 20 hours of activity in the month: earn 10 points per hour
 - For each point earned, the customer earns R$0.05 (5 cents)
Make a program that reads how many hours of activity a person has per month,
calculate and show how many points she had and how much money she managed to earn.
"""
time_act = int(input("Enter how many hours of physical activity you did per month: "))
if time_act <= 10:
    print(f"Points you earned: {2 * time_act}; Money you earned: ${((2 * time_act) * 0.05):.2f}")
elif 10 < time_act <= 20:
    print(f"Points you earned: {5 * time_act}; Money you earned: ${((5 * time_act) * 0.05):.2f}")
else:
    print(f"Points you earned: {10 * time_act}; Money you earned: ${((10 * time_act) * 0.05):.2f}")
