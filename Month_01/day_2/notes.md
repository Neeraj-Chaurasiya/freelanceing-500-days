📘 Notes: NumPy Operations & Matrix Handling (Day-2)

🔹 Arithmetic Operations

import numpy as np

arr = np.array([1,2,3,4,5])

print(arr + 5)   # [ 6  7  8  9 10]

print(arr * 2)   # [ 2  4  6  8 10]

print(arr ** 2)  # [ 1  4  9 16 25]

print(arr - 1)   # [0 1 2 3 4]

print(arr / 2)   # [0.5 1.  1.5 2.  2.5]


👉 NumPy me operations element-wise apply hote hain.

👉 Ye feature vectorization kehlata hai (fast computation).

🔹 Mathematical & Statistical Functions

arr = np.array([10,20,30,40,50])

print(np.min(arr))    # 10

print(np.max(arr))    # 50

print(np.mean(arr))   # 30.0

print(np.median(arr)) # 30.0

print(np.std(arr))    # 14.14...

print(np.sum(arr))    # 150


👉 Analysis ke liye min, max, mean, median, std, sum ka use hota hai.

🔹 Reshape & Axis Operations

mat = np.arange(1,13).reshape(3,4)

print(mat)

# [[ 1  2  3  4]
#  [ 5  6  7  8]
#  [ 9 10 11 12]]

print(mat.shape)        # (3,4)

print(mat.sum(axis=0))  # [15 18 21 24] → column-wise sum

print(mat.sum(axis=1))  # [10 26 42] → row-wise sum


👉 reshape(r, c) se array ka shape change hota hai.

👉 axis=0 → column-wise, axis=1 → row-wise calculation.

🔹 Random Numbers

rand_arr = np.random.rand(3,3)   # 3x3 matrix, values (0–1)

print(rand_arr)

rand_int = np.random.randint(1,100,5)  # 5 random integers (1–99)

print(rand_int)

np.random.seed(42)

print(np.random.rand(2,2))   # same output har run par


👉 rand → random floats (0–1).

👉 randint → random integers.

👉 seed → reproducibility (same result har bar).

🔹 Practice Task (Self Try 🚀)

# 3x3 random matrix (1–50)

mat = np.random.randint(1, 51, (3,3))

print(mat)

print("Row-wise max:", mat.max(axis=1))

print("Col-wise min:", mat.min(axis=0))

# 1D → 4x4 reshape

arr = np.arange(1,17).reshape(4,4)

print(arr)

print("Row sums:", arr.sum(axis=1))

print("Col sums:", arr.sum(axis=0))


✅ Summary

Arithmetic operations element-wise lagte hain.

Statistical functions (min, max, mean, median, std, sum) fast aur useful hote hain.

reshape & axis se matrix handling easy hota hai.

Random number generation (rand, randint, seed) testing & simulation me kaam aata hai.