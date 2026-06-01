import numpy as np

matrix = np.array([[1, 2, 3],
                   [4, 5, 6],
                   [7, 8, 9]])

row = np.array([10, 20, 30])
col = np.array([[10], [20], [30]])

# Task 1
print(matrix + row)

# Task 2
print(matrix + col)

# Task 3
print(matrix * 2)

# Task 4
print(matrix - row)

# Task 5
result = col * row
print(result)
print(result.shape)

# Task 7
a = np.array([[1, 2, 3],
              [4, 5, 6]])

b = np.array([[1, 2],
              [3, 4],
              [5, 6]])

# print(a + b)