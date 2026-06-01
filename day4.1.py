import numpy as np

arr = np.array([[1,  2,  3,  4],
                [5,  6,  7,  8],
                [9, 10, 11, 12]])

# Task 1
print(arr[1, 2])   

# Task 2
print(arr[1])    

# Task 3
print(arr[:, 2])   

# Task 4
print(arr[:2])     

# Task 5
print(arr[:, -2:])

# Task 6
print(arr[1:3, 1:3]) 
# Task 7
print(arr[arr > 6])

# Task 8
arr[arr > 6] = 0
print(arr)