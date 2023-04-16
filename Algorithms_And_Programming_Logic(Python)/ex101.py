"""
Create a Matrix(Mathematics) using Python(Nested list).
"""

matrix = [[1, 2, 3],
          [4, 5, 6],
          [7, 8, 9]]

for i in range(1, 4):
    for j in range(1, 4):
        x = float(input(f"Enter the number of position [{i},{j}]:"))
        matrix.append(x)

"""
for i in range(1, 4):
    for j in range(1, 4):
        print(matrix)
"""

for i in matrix:
    print('\t'.join(map(str, i)))

