"""
Develop an algorithm that counts down from 30 to 1,
marking the numbers that are divisible by 4, exactly as shown below:
30 29 [28] 27 26 25 [24] 23 22 21 [20] 19 18 17 [16]...
"""
for i in range(30, 1, -1):
    if i % 4 == 0:
        print(f"[{i}]", end=" ")
    else:
        print(i, end=" ")
