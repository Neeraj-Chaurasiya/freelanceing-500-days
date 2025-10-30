# NumPy Setup
import numpy as np
import time
print(np.__version__)

# Basic arrays

a = np.array([1,2,3,4,5])
b = np.zeros((2,3))
c = np.ones(4)
d = np.arange(0,10,2)
e = np.linspace(0,1,5)

print(a,b,c,d,e)

# Array Indexing & Slicing

arr = np.array([10,20,30,40,50])
print(arr[1:4])
print(arr[-1])
print(arr[:3])
print(arr[3:])

# Vectorized Math Operations

x = np.array([10,20,30])
y = np.array([5,10,15])

print(x*y)
print(x/y)
print(x+y)
print(np.sqrt(x))

# Broadcasting (Smart Operations)

A = np.arange(6).reshape(2,3)
B = np.array([[10],[20]])
print(A + B)

# Statistical Functions

arr = np.random.randint(10, 100, size=10)
print("Mean :", arr.mean())
print("Max :", arr.max())
print("Min :", arr.min())
print("Sum :", arr.sum())

# Performance Comparison (Python List vs NumPy)

list_data = list(range(1000000))
np_data = np.arange(1000000)

start = time.time()
sum(list_data)
print("List time : ", time.time() - start)

start = time.time()
np_data.sum()
print("Numpy time : ", time.time() - start)

# Practice Task

price = np.random.randint(100,4999,size = 100)

quantity =  np.random.randint(1,11,size = 100)

discount = np.random.uniform(0, 0.3, size=100) 
print(discount)

total_sale = price * quantity

final_sale = total_sale - (total_sale * discount)
print(final_sale)

profit_margin =final_sale * 0.15
print(profit_margin)
print(profit_margin.mean())
print(profit_margin.max())
print(profit_margin.sum())