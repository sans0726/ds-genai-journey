import numpy as np

# Task 1
arr1 = np.arange(1, 11)

# Task 2
arr2 = np.arange(1, 10).reshape(3, 3)

# Task 3
arr3 = np.zeros((4, 4))

# Task 4
arr4 = np.ones((3, 5))

# Task 5
arr5 = np.linspace(0, 1, 10)

# Task 6
arr6 = np.random.rand(3, 3)

# Task 7
arr7 = np.random.randint(1, 101, (3, 3))

# Task 8
np.random.seed(42)
arr8 = np.random.rand(4, 4)

# Task 9
arrays = [arr1, arr2, arr3, arr4, arr5, arr6, arr7, arr8]

for i, arr in enumerate(arrays, 1):
    print(f"\nArray {i}:")
    print(arr)
    print("Shape:", arr.shape)
    print("Size:", arr.size)
    print("Dtype:", arr.dtype)