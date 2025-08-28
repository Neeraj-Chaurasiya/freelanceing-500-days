#------------------Arithmetic Operations------------------

import numpy as np

arr = np.array([1,2,3,4,5,6])

print(arr+5) 
print(arr*2) 
print(arr**2)
print(arr-1)
print(arr/2)

#----------Mathematical & Statistical Functions-----------

arr1 = np.array([10,20,30,40,50,60])

print(np.min(arr1))
print(np.max(arr1))
print(np.mean(arr1))
print(np.median(arr1))
print(np.std(arr1))
print(np.sum(arr1))

#--------------Reshape & Axis Operations-----------------

mat = np.arange(1,13).reshape(3,4)

print(mat)
print(mat.shape)
print(mat.sum(axis=0))  # column-wise sum → [15 18 21 24]
print(mat.sum(axis=1))  # row-wise sum → [10 26 42]

# ------------Random Number----------------

rand_arr = np.random.rand(3,3) # 3x3 matrix (values between 0–1)
# print(rand_arr)
rand_int = np.random.randint(1,100,5)
# print(rand_int)
np.random.seed(42)
print(np.random.rand(2,2))

# -----------------Tast (self try)------------------

rand_int1 = np.random.randint(1,50,(2,3))
print(rand_int1)
print(rand_int1.min(axis = 0))
print(rand_int1.max(axis = 1))

arr_1D = np.arange(1,17)
mat = arr_1D.reshape(4,4) 
print(mat)
print(mat.sum(axis=1))
print(mat.sum(axis=0))