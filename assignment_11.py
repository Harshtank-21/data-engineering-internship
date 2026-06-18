import numpy as np
from scipy import stats

# 1) Combining 1D and 2D NumPy arrays
arr1d = np.array([1, 2, 3])
arr2d = np.array([[4, 5, 6], [7, 8, 9]])
combined = np.concatenate((arr1d.reshape(1, 3), arr2d), axis=0)
print("Combined 1D and 2D array:")
print(combined)

# 2) Flatten 2D array into 1D
flat = arr2d.flatten()
print("\nFlattened array:", flat)

# 3) Reverse a numpy array
arr = np.array([10, 20, 30, 40, 50])
reversed_arr = arr[::-1]
print("\nReversed array:", reversed_arr)

# 4) Practice operations
data = np.array([[3, 7, 1], [5, 9, 2]])

print("\nMax value:", np.max(data))
print("Min value:", np.min(data))
print("Rows and Columns:", data.shape)

print("\nAll elements:")
for row in data:
    for val in row:
        print(val, end=" ")
print()
print("Element at [0][1]:", data[0][1])

print("\nSum of 2D array using for loop:")
total = 0
for row in data:
    for val in row:
        total += val
print("Sum:", total)

a = np.array([2, 4, 6])
b = np.array([1, 2, 3])
print("\nAddition:", a + b)
print("Subtraction:", a - b)
print("Multiplication:", a * b)
print("Division:", a / b)

# 5) Iterate 3D array
arr3d = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])
print("\nIterating 3D array using for loop:")
for matrix in arr3d:
    for row in matrix:
        for val in row:
            print(val, end=" ")
print()
print("\nIterating using nditer:")
for val in np.nditer(arr3d):
    print(val, end=" ")
print()

# 6) Average, mean, median, mode of two 2D arrays
x = np.array([[3, 6, 9], [12, 15, 18]])
y = np.array([[1, 4, 7], [10, 13, 16]])

avg = (x + y) / 2
print("\nAverage of two 2D arrays:")
print(avg)
print("Mean of x:", np.mean(x))
print("Mean of y:", np.mean(y))
print("Median of x:", np.median(x))
print("Median of y:", np.median(y))
print("Mode of x:", stats.mode(x, axis=None).mode)
print("Mode of y:", stats.mode(y, axis=None).mode)
