import numpy as np

data = np.array([[1, 2, 3],
                 [4, 5, 6],
                 [7, 8, 9]])

print(np.sum(data))

print(np.sum(data, axis=0))

print(np.sum(data, axis=1))

print(np.mean(data, axis=0))

print(np.mean(data, axis=1))

print(np.max(data, axis=0))

print(np.min(data, axis=1))