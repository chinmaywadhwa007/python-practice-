import numpy as np
import numpy
arr = numpy.array([1, 2, 3, 4, 5])
print(arr)
print(type(arr))

arr = np.array([1, 2, 3, 4, 5, 6])
print(arr)

# diff bw numpy and python list
# Why does lst + lst concatenate?
# A Python list is a general-purpose container that can hold any type of object.
# When you use the + operator on lists, Python interprets it as joining two lists together, not adding their elements.
lst = [1, 2, 3, 4]
arr = np.array([1, 2, 3, 4])
print(lst+lst)  # will be concatinate
print(arr+arr)  # this will be adddition


#indexing in 2d arr
arr = np.array([[1, 2, 3],
                [4, 5, 6]])
print(arr[1][0])

#indexing in 3d array
arr = np.array([
    [[1, 2, 5], [3, 4, 5]],
    [[5, 6, 7], [11, 34, 22]],
    [[1, 3, 8], [2, 4, 5]]
])
print(arr[0][0][0])


# array creation of function

print(np.zeros([5,2]))

print(np.ones((3,2)))

print(np.full((4,5),3))


# arranging the words 
print(np.arange(2,19))