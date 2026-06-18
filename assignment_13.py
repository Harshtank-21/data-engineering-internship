import numpy as np
from scipy import stats
import matplotlib.pyplot as plt

# 1) Replace NaN with 0 and interchange 3 rows and 3 columns
arr = np.array([[6, -8, 73, -110], [np.nan, -8, 0, 94]], dtype=float)
arr[np.isnan(arr)] = 0
print("After replacing NaN with 0:\n", arr)

# Interchange rows 0 and 1
arr[[0, 1]] = arr[[1, 0]]
print("After swapping rows 0 and 1:\n", arr)

# Interchange columns 0 and 1
arr[:, [0, 1]] = arr[:, [1, 0]]
print("After swapping columns 0 and 1:\n", arr)

# 2) Move axes of 3D array
arr3d = np.ones((2, 3, 4))
moved = np.moveaxis(arr3d, 0, -1)
print("\nOriginal shape:", arr3d.shape)
print("After moveaxis(0 -> -1):", moved.shape)

# 3) Replace NaN values with column average
data = np.array([[1, 2, np.nan], [4, np.nan, 6], [7, 8, 9]], dtype=float)
col_means = np.nanmean(data, axis=0)
for col in range(data.shape[1]):
    nan_rows = np.isnan(data[:, col])
    data[nan_rows, col] = col_means[col]
print("\nAfter replacing NaN with column mean:\n", data)

# 4) Replace negative values with 0
arr_neg = np.array([[3, -1, 5], [-2, 7, -4]])
arr_neg[arr_neg < 0] = 0
print("\nAfter replacing negatives with 0:\n", arr_neg)

# 5) Average, mean, median, mode of two 2D arrays
a = np.array([[3, 4], [1, 0]])
b = np.array([[5, 2], [3, 6]])
avg = (a + b) / 2
print("\nAverage:\n", avg)
print("Mean of a:", np.mean(a))
print("Mean of b:", np.mean(b))
print("Median of a:", np.median(a))
print("Median of b:", np.median(b))
print("Mode of a:", stats.mode(a, axis=None).mode)
print("Mode of b:", stats.mode(b, axis=None).mode)

# 6) Solve linear equations using linalg and inverse matrix
# x - 2y + 3z = 9
# -x + 3y - z = -6
# 2x - 5y + 5z = 17
A = np.array([[1, -2, 3], [-1, 3, -1], [2, -5, 5]], dtype=float)
B = np.array([9, -6, 17], dtype=float)

solution_linalg = np.linalg.solve(A, B)
print("\nSolution using linalg.solve:")
print("x =", solution_linalg[0], "y =", solution_linalg[1], "z =", solution_linalg[2])

A_inv = np.linalg.inv(A)
solution_inv = A_inv @ B
print("Solution using inverse matrix:")
print("x =", solution_inv[0], "y =", solution_inv[1], "z =", solution_inv[2])

# 7) Plot semester results comparison
semesters = ["Sem 1", "Sem 2", "Sem 3", "Sem 4"]
subject_scores_sem1 = [72, 68, 75, 80, 65]
subject_scores_sem2 = [78, 74, 82, 85, 70]
subjects = ["Math", "Physics", "Python", "DBMS", "OS"]

x = np.arange(len(subjects))
width = 0.35

fig, ax = plt.subplots(figsize=(9, 5))
bars1 = ax.bar(x - width/2, subject_scores_sem1, width, label="Semester 1", color="steelblue")
bars2 = ax.bar(x + width/2, subject_scores_sem2, width, label="Semester 2", color="darkorange")

ax.set_title("Semester Result Comparison", fontsize=14, fontweight="bold")
ax.set_xlabel("Subjects")
ax.set_ylabel("Marks")
ax.set_xticks(x)
ax.set_xticklabels(subjects)
ax.legend()
ax.set_ylim(0, 100)

for bar in bars1:
    ax.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 1, str(bar.get_height()), ha="center", fontsize=9)
for bar in bars2:
    ax.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 1, str(bar.get_height()), ha="center", fontsize=9)

plt.tight_layout()
plt.savefig("semester_comparison.png", dpi=100)
plt.show()
print("\nGraph saved as semester_comparison.png")
