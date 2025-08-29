📘 Notes: NumPy Basics (Day-1)

🔹 Import & Basic Array

import numpy as np

arr = np.array([1, 2, 3, 4, 5, 6])

print(type(arr))      # <class 'numpy.ndarray'>  
print(arr.shape)      # (6,) → 1D array of length 6

👉 np.array se NumPy array banta hai.  
👉 .shape array ke dimension & size batata hai.

🔹 Array Creation Methods

a = np.zeros((2, 3))     # 2x3 matrix of all 0  
b = np.ones((3, 3))      # 3x3 matrix of all 1  
c = np.eye(3)            # Identity matrix (3x3)  
d = np.arange(0, 10, 3)  # [0, 3, 6, 9] → start=0, stop<10, step=3  
e = np.linspace(0, 2, 5) # 5 numbers evenly spaced between 0 and 2

👉 zeros, ones, eye, arange, linspace ka use array banane ke liye hota hai.

🔹 Indexing & Slicing (1D)

arr1 = np.array([10, 20, 30, 40, 50, 60])  
print(arr1[0])      # 10 → first element  
print(arr1[-1])     # 60 → last element  
print(arr1[1:4])    # [20, 30, 40] → slicing (index 1 se 3 tak)

🔹 2D Array Access

arr2 = np.array([[1,2,3],[4,5,6],[7,8,9]])  
print(arr2[0, 0])   # 1 → (row0, col0)  
print(arr2[1, :])   # [4 5 6] → row 1  
print(arr2[:, 2])   # [3 6 9] → column 2

👉 arr[row, col] se element access hota hai.  
👉 : ka matlab "poora row/column".

🔹 Boolean Indexing (Filter)

arr4 = np.arange(1, 21)  
even = arr4[arr4 % 2 == 0]  
print(even)   # [ 2  4  6  8 10 12 14 16 18 20]

👉 Boolean mask se specific condition wale elements nikal sakte ho.

🔹 2D Matrix Indexing (Practice)

mat = np.array([
 [ 1,  2,  3,  4,  5],
 [ 6,  7,  8,  9, 10],
 [11, 12, 13, 14, 15],
 [16, 17, 18, 19, 20]
])

print(mat[1, :])   # [ 6  7  8  9 10] → row 1  
print(mat[:, 3])   # [ 4  9 14 19] → column 3  
print(mat[3, 4])   # 20 → last element

✅ Summary

np.array → basic array creation.  
zeros, ones, eye, arange, linspace → array generate karne ke methods.  
Indexing & slicing same as Python lists, but 2D me [row, col].  
Boolean indexing powerful hai (filter karne ke liye).


