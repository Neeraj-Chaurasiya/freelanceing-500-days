import numpy as np

arr = np.array([1, 2, 3, 4, 5, 6])
print(type(arr))
print(arr.shape)

# --------------Array creation methods --------------------

a = np.zeros((2, 3))
b = np.ones((3, 3))
c = np.eye(3)
d = np.arange(0, 10, 3)
e = np.linspace(0, 2, 5)
print(e)

# -------------------Indexing and slicing(1D)----------------------

arr1 = np.array([10, 20, 30, 40, 50, 60])

print(arr1[0])
print(arr1[-1])
print(arr1[1:4])

# ---------------2D array--------------------------

arr2 = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

print(arr2[0, 0])
print(arr2[1, :])
print(arr2[:, 2])


# -----------------test---------------------

arr4 = np.arange(1, 21)
even = arr4[arr4 % 2 == 0]
print(even)

mat = np.array(
    [[1, 2, 3, 4, 5], [6, 7, 8, 9, 10], [11, 12, 13, 14, 15], [16, 17, 18, 19, 20]]
)
print(mat[1, :])
print(mat[:, 3])
print(mat[3, 4])
