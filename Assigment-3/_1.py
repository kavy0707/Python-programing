#    To perform numpy operation by using sample data.
# a.     Create a 4X2 integer array and Prints its attributes
#       The shape of an array.
#   Array dimensions.
#   The Length of each element of the array.

# b.     Return array of items in the third column from all rows
        # Array1 = numpy.array([[11 ,22, 33], [44, 55, 66], [77, 88, 99]])


# c.     Following is the given numpy array return array of odd rows and even columns


# numpy.array(

# [[1 ,2, 3, 4], 

# [5 ,6, 7, 8],

# [9 ,10, 11, 12], 

# [13 ,14, 15, 16], 

# [17 ,18, 19,20]])


# d.     Print max from axis 0 and min from axis 1

# numpy.array([[34,43,73],[82,22,12],[53,94,66]])

import numpy as np
arr = np.array([[[[1,2],[4,5],[7,8],[10,11]]]])
print("dimension=",arr.ndim)
print("array=",arr)
print("shape=",arr.shape)
print("size=",arr.size)
print(arr[0,0,2].size)
print()

print("length of each element in array:")
for i in range(0,len(arr[0][0])):
    print(arr[0][0][i].size,end=",")

print()
print()
print()
print("Return array of items in the third column from all rows")
Array1 = np.array([[11 ,22, 33], [44, 55, 66], [77, 88, 99]])
for i in range(0,len(Array1)):
    print("in column:",i,"value=",Array1[i][2],end=",   ")

print()
print()
print()
print("given numpy array return array of odd rows and even columns:")
array2 = np.array(
[[1 ,2, 3, 4], 
[5 ,6, 7, 8],
[9 ,10, 11, 12], 
[13 ,14, 15, 16], 
[17 ,18, 19,20]])

for i in range(0,len(array2)-1):
    if(i%2!=0):
        for j in range(0,len(array2)-1):
            if(j%2==0):
                print(array2[i][j],end=",")
