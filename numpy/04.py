# numpy copy vs view
import numpy as y
import numpy as hii
import numpy as np
a = np.array([1, 2, 3])
b = a.copy()  # this is the copy method
b[0] = 99
# here we will copy from the array a it can't update the existing where here #[1,2,3]
print("a:", a)
# here we will print the value from b axact as it is it will change the existing value #[99,2,3]
print("b:", b)

y = np.array([4, 5, 6])
q = y.view()
q[0] = 99
print("y:", y)  # here it will change the updating value also # 99,5,6
print("q:", q)  # same as q

# check if arrays own its data
arr = np.array([3, 3, 3])
# x.base prints None because copy() creates new, independent memory. x owns its data.
# x.base prints None because copy() creates new, independent memory. x owns its data.
# y.base prints arr because view() shares the same memory with arr. The .base attribute shows the original array whose memory is being shared.
# it copies the o/p thats why it show none creates new, independent memory. x owns its data.
x = arr.copy()
# it shows only the o/p shares the same memory with arr. The .base attribute shows the original array whose memory is being shared.
y = arr.view()
print(x.base)
print(y.base)

# shape of the array
# it define the shape of the o/p if u choose the 5 bracket will become 5 and if u choose other number till 64 it will deside the shape
arr = np.array([1, 2, 3, 4, 5], ndmin=5)

print(arr)
print('shape of the array :', arr.shape)


# numpy array reshaping

arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])

newarr = arr.reshape(3, 4)
print(newarr)
# reshape from 1-D to 3-D
# the outermost dimension will  have 2 arrays that contains 3 arrays each with 2 elements
arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])

newarr = arr.reshape(3, 2, 2)

print(newarr)

# converting multiple array into 1d array

arr = np.array([[1, 2, 3], [4, 5, 6]])
newarr = arr.reshape(-1)
print(newarr)

# numpy array iterating
hello = np.array([1, 2, 3])
for x in hello:
    print(x)

# iterating 2d array
arr = np.array([[1, 2, 3], [4, 5, 6]])
# will use the for loop for that
for x in arr:
    print(x)


arr = np.array([[1, 2, 3], [1, 2, 3]])
for x in arr:
    for y in x:
        print(y)


# for 3rd array

arr = np.array([[[1, 2, 3], [1, 2, 3]], [[4, 5, 6], [7, 8, 9]]])
for x in arr:
    print(x)

# this is for the 3d array
arr = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])
for x in arr:
    for y in x:
        for z in y:
            print(z)

# joining the array like a+b
# conncatenate will join the two array without adding them
arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])
arr = np.concatenate((arr1, arr2))
print(arr)

# splitting numpy array
arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
newarr = np.array_split(arr, 4)
print(newarr)


# another example
arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
newarr = np.array_split(arr, 4)  # how much u have to divide the grp
print(newarr)
# searching the array
arr = np.array([7, 9, 10, 22, 43, 50, 89, 100])
x = np.where(arr == 43)
print(x)


# find the indexing where the values are odd:
arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9])
x = np.where(arr % 2 == 1)
print(x)
#sorting array 
arr=np.array([10,11,12,13,14,15,16,17,18,19,20])
