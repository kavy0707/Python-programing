import numpy as np

arr = np.array([1,2,3,4,5,6,7,8,9,10,11,12])
slice_arr = arr[1:10]
print(slice_arr)

s_arr = np.array([[1,2,3],[4,5,6],[7,8,9]])
slice1_arr = s_arr[0:2,1:3]
print(slice1_arr)

print()
dicing_arr = arr[1:9:3]
print("dicing arr = ",dicing_arr)

print()
arr1 = np.array([100,8,9,45,65,31,74])
sort_arr = np.sort(arr1)
print("Sorted array = ",sort_arr)

arr2 = np.array([[[1, 2], [3, 4], [5, 6]]])
print("Before shuffle:", arr2)
print()
shuffle_arr = np.random.permutation(arr2[0])
print()
print("shuffled_arr=",shuffle_arr)