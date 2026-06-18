import numpy as np

# Convert 1D to 2D
arr1d = np.array([1, 2, 3, 4, 5, 6])
arr2d = arr1d.reshape(2, 3)
print("1D to 2D:\n", arr2d)

# Array attributes
print("\nShape:", arr2d.shape)
print("Dimensions:", arr2d.ndim)
print("Data type:", arr2d.dtype)
print("Item size:", arr2d.itemsize)

# 3x3 array of all 9
nines = np.full((3, 3), 9)
print("\n3x3 array of 9s:\n", nines)

# 1D array of 10 evenly spaced values between 25 and 125
spaced = np.linspace(25, 125, 10)
print("\nEvenly spaced (25 to 125):", spaced)

# Python list to NumPy array
py_list = [10, 20, 30, 40]
np_arr = np.array(py_list)
print("\nList to NumPy array:", np_arr)

# Reverse 1D array
rev = np_arr[::-1]
print("Reversed:", rev)

# 4x4x3 array, extract value at second set, first row, last column
arr3d = np.arange(48).reshape(4, 4, 3)
val = arr3d[1, 0, -1]
print("\n4x4x3 array value at [1,0,-1]:", val)

# 4x4 array, extract odd rows and even columns
arr4x4 = np.arange(16).reshape(4, 4)
print("\n4x4 array:\n", arr4x4)
odd_rows_even_cols = arr4x4[1::2, ::2]
print("Odd rows, even columns:\n", odd_rows_even_cols)

# Slice first 2 rows and first 2 columns from second set of 4x4x3
arr443 = np.arange(48).reshape(4, 4, 3)
sliced = arr443[1, :2, :2]
print("\nSlice from second set, first 2 rows, first 2 cols:\n", sliced)

# Replace odd numbers with -1 using for loop
arr2d_vals = np.array([[23, 56, 78, 93], [71, 82, 13, 24]])
for i in range(arr2d_vals.shape[0]):
    for j in range(arr2d_vals.shape[1]):
        if arr2d_vals[i, j] % 2 != 0:
            arr2d_vals[i, j] = -1
print("\nAfter replacing odd numbers with -1:\n", arr2d_vals)

# Get indices of non-zero elements
arr_nz = np.array([1, 0, 2, 0, 3, 0, 4])
indices = np.nonzero(arr_nz)
print("\nNon-zero indices:", indices[0])

# Arithmetic operations element-wise
a = np.array([2, 4, 6])
b = np.array([1, 2, 3])
print("\nAdd:", a + b)
print("Multiply:", a * b)

# Dot product
arr1 = np.array([15, 20, 25])
arr2 = np.array([10, 40, 37])
dot = np.dot(arr1, arr2)
print("\nDot product:", dot)
