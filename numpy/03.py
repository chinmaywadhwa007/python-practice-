import numpy as hi
import numpy as np
import numpy as D
import numpy as virat  # u can call it by any name here
import numpy as imp
import numpy
import numpy as np
# multiply it by 2 without using the loop
arr = np.array([1, 2, 3, 4, 4, 5])
result = arr*2
print(result)

# using list this is with loop state-ment
lst = [1, 2, 3, 4, 5]
result = [x*2 for x in lst]
print(result)

arr = numpy.array([12, 13, 14, 15, 16])
print(arr)

# we can call numpy as np
b = np.array([1, 23, 4, 5, 23, 3])
print(b)

# we can check the version of the numpy

print(virat.__version__)

# create np of ndarray object

arr = imp.array([1, 2, 3, 45, 66])  # nd means one d array
print(arr)
print(type(arr))

# using the tuple
arr = np.array((1, 2, 4, 5, 3, 2, 1))
print(arr)

# now comes with the 0 d array and how they works


arr = np.array(10)  # this is the 0d arr
print(arr)

# 1 d arrays
arr = D.array([1, 2, 3, 4, 5, 5])
print(arr)
# this is called 2d array
arr1 = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(arr1)

# 3d array
arr2 = np.array([[[1, 2, 3], [1, 2, 3]], [[1, 2, 3], [2, 3, 4]]])
print(arr2)


# check  number dimensions
a = np.array(42)
b = np.array([1, 2, 3, 4, 5])
c = np.array([[1, 2, 3], [4, 5, 6]])
d = np.array([[[1, 2, 3], [4, 5, 6]], [[1, 2, 3], [4, 5, 6]]])
print(a.ndim)  # 0d array
print(b.ndim)  # 01d array
print(c.ndim)  # 02d array
print(d.ndim)  # 03d array


# higher direction array
arr3 = np.array([1, 2, 3, 4], ndmin=4)
print("enter your array dimensions:", arr3.ndim)
print(arr3)

# nummpy array indexing
# Acessing array elements
arr4 = np.array([1, 2, 3, 4])
print(arr4[3])


# get the 2nd element from the existing array
print(arr4[1])


# accesing 2d array
# here is the catch there are 2 row  where we have to find the indexing of the element 0 means 1,2,3,4,5and and 1 means 6,7,8,9,10 from now we have to  access the element from 1 row and 3 number which is 9
arr5 = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])
print('2nd element on 1st row ', arr5[0, 1])
arr5 = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])
print('5th element on 1st row ', arr5[1, 4])

# Access 3-D Arrays
arr = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])
print(arr[0, 1, 2])
print(arr[1, 1, 1])
print(arr[0, 1, 0])


a = hi.array([1, 2, 3, 4, 5, 6, 7])
print(a[1:5])
