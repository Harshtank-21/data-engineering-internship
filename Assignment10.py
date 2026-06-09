# Assignment 10
import numpy as np

arr = np.array([[6,-8,73,-110],[np.nan,-8,0,94]])
print(np.nan_to_num(arr, nan=0))
print(arr.T[:3,:2])

arr2 = np.array([[1,np.nan],[3,4],[np.nan,6]])
col_mean = np.nanmean(arr2, axis=0)
inds = np.where(np.isnan(arr2))
arr2[inds] = np.take(col_mean, inds[1])
print(arr2)

arr3 = np.array([1,-2,3,-4])
arr3[arr3<0] = 0
print(arr3)

arr4 = np.random.rand(2,3,4)
print(np.moveaxis(arr4,0,-1).shape)
