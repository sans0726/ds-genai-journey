import numpy as np

# EDGE CASE 1 — Mixed data types
data1 = np.array([1, 2, "3"])
print(data1)
print(data1.dtype)

# 1 and 2 are converted to strings because NumPy requires all elements
# to be of the same type. Presence of a string forces entire array to string.


# EDGE CASE 2 — Integer vs Float
data2 = np.array([1, 2, 3])
data3 = np.array([1.0, 2.0, 3.0])

print(data2 / 2)
print(data3 / 2)

# Integer array gets converted to float during division.
# Float array remains float.
# In ML, float is required for precision (weights are float).


# EDGE CASE 3 — Shape mismatch
a = np.array([1, 2, 3])
b = np.array([1, 2])

# print(a + b)

# ValueError: operands could not be broadcast together with shapes (3,) (2,)
# Shapes are incompatible and cannot be expanded for broadcasting.


# EDGE CASE 4 — Copy vs View
original = np.array([1, 2, 3, 4, 5])

view = original[1:4]
copy = original[1:4].copy()

view[0] = 999
print(original)

# Reset original
original = np.array([1, 2, 3, 4, 5])

copy = original[1:4].copy()
copy[0] = 888
print(original)

# View shares memory with original array, so changes affect original.
# Copy creates a new array, so changes do not affect original.