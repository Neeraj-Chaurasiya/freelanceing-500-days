import numpy as np

# arr = np.array([1,2,3,4,5,6])
# print(arr)
# print(type(arr))
# print(arr.shape)

# --------------Array creation methods --------------------

# a = np.zeros((2,3))
# # print(a)
# b = np.ones((3,3))
# # print(b)
# c = np.eye(3)
# # print(c)
# d = np.arange(0,10,3)
# # print(d)
# e = np.linspace(0,2,5)
# print(e)

# -------------------Indexing and slicing(1D)----------------------

# arr = np.array([10,20,30,40,50,60])

# print(arr[0])
# print(arr[-1])
# print(arr[1:4])

# ---------------2D array--------------------------

# arr = np.array([[1,2,3],[4,5,6],[7,8,9]])

# # print(arr)
# print(arr[0,0])
# print(arr[1,:])
# print(arr[:,2])


# -----------------test---------------------

# arr = np.arange(1,21)
# print(arr)
# even = arr[arr%2==0]
# print(even)

mat = np.array([[1,2,3,4,5],[6,7,8,9,10],[11,12,13,14,15],[16,17,18,19,20]])
# print(mat)
print(mat[1,:])
print(mat[:,3])
print(mat[3,4])