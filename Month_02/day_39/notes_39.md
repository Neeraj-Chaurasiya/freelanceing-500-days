
# 📅 Day 39 – NumPy Deep Dive: Arrays, Math & Performance

---

## 🎯 Objective

Python ke **NumPy (Numerical Python)** library ka use karke array creation, mathematical operations, and performance optimization seekhna.  
NumPy is the foundation for **Pandas**, **Machine Learning**, and **Data Science** computations.

---

## ✅ Topics Covered

- NumPy setup and version check  
- Array creation methods  
- Indexing and slicing  
- Vectorized math operations  
- Broadcasting concepts  
- Statistical functions  
- Performance comparison (List vs NumPy)  
- Mini project: Profit margin simulation  

---

## 🧩 Step 1 – NumPy Setup

```python
import numpy as np
import time
print(np.__version__)
```

**Explanation:**  
- `import numpy as np` → Imports NumPy library.  
- `np.__version__` → Checks the installed version.  
- `time` module → Used to measure performance.  

💡 NumPy arrays are much faster than regular Python lists.

---

## 📊 Step 2 – Basic Arrays

```python
a = np.array([1,2,3,4,5])
b = np.zeros((2,3))
c = np.ones(4)
d = np.arange(0,10,2)
e = np.linspace(0,1,5)

print(a,b,c,d,e)
```

**Explanation:**  
| Function | Description |
|-----------|--------------|
| `np.array()` | Converts Python list to NumPy array |
| `np.zeros()` | Creates an array of zeros |
| `np.ones()` | Creates an array of ones |
| `np.arange()` | Creates range with step size |
| `np.linspace()` | Creates evenly spaced numbers |

💡 These are the building blocks for numerical computations.

---

## 🧮 Step 3 – Array Indexing & Slicing

```python
arr = np.array([10,20,30,40,50])
print(arr[1:4])
print(arr[-1])
print(arr[:3])
print(arr[3:])
```

**Explanation:**  
- Works exactly like list slicing.  
- `arr[1:4]` → Elements from index 1 to 3.  
- `arr[-1]` → Last element.  
- `arr[:3]` → First 3 elements.  

💡 Slicing in NumPy doesn’t copy data — it provides a *view* (faster!).

---

## ⚡ Step 4 – Vectorized Math Operations

```python
x = np.array([10,20,30])
y = np.array([5,10,15])

print(x*y)
print(x/y)
print(x+y)
print(np.sqrt(x))
```

**Explanation:**  
- NumPy performs **element-wise** operations automatically.  
- No need for loops like Python lists.  
- `np.sqrt()` → Calculates square root for each element.  

💡 This is called **vectorization**, and it’s the reason NumPy is so fast.

---

## 🧠 Step 5 – Broadcasting (Smart Operations)

```python
A = np.arange(6).reshape(2,3)
B = np.array([[10],[20]])
print(A + B)
```

**Explanation:**  
- Broadcasting automatically adjusts smaller arrays to match dimensions.  
- `reshape(2,3)` → Converts 1D array into 2x3 matrix.  
- Here, B (2x1) expands to match A (2x3).  

💡 Avoids writing nested loops → saves time and memory.

---

## 📈 Step 6 – Statistical Functions

```python
arr = np.random.randint(10, 100, size=10)
print("Mean :", arr.mean())
print("Max :", arr.max())
print("Min :", arr.min())
print("Sum :", arr.sum())
```

**Explanation:**  
| Function | Description |
|-----------|--------------|
| `.mean()` | Average of elements |
| `.max()` | Maximum value |
| `.min()` | Minimum value |
| `.sum()` | Total sum of elements |

💡 NumPy’s statistical methods are highly optimized for large arrays.

---

## ⚙️ Step 7 – Performance Comparison (List vs NumPy)

```python
list_data = list(range(1000000))
np_data = np.arange(1000000)

start = time.time()
sum(list_data)
print("List time : ", time.time() - start)

start = time.time()
np_data.sum()
print("Numpy time : ", time.time() - start)
```

**Explanation:**  
- Tests speed difference between normal list operations and NumPy arrays.  
- `np_data.sum()` is much faster than `sum(list_data)`.

💡 NumPy uses **C-based optimization** → ~10–100x faster than pure Python.

---

## 💼 Step 8 – Practice Task (Mini Project)

```python
price = np.random.randint(100,4999,size = 100)
quantity =  np.random.randint(1,11,size = 100)
discount = np.random.uniform(0, 0.3, size=100) 

total_sale = price * quantity
final_sale = total_sale - (total_sale * discount)
profit_margin = final_sale * 0.15

print(profit_margin)
print(profit_margin.mean())
print(profit_margin.max())
print(profit_margin.sum())
```

**Explanation:**  
- Simulates 100 random sales records.  
- `randint()` → Random integer values for price & quantity.  
- `uniform()` → Random float discount between 0–0.3.  
- Calculates total sale, discount adjustment, and profit margin.  

💡 Perfect example of NumPy’s vectorized computation in real-world scenarios.

---

## 🧠 Summary

| Step | Concept | Description |
|------|----------|--------------|
| 1 | Setup | Import NumPy & check version |
| 2 | Array Creation | Create arrays using various methods |
| 3 | Indexing | Access and slice arrays efficiently |
| 4 | Math Operations | Perform vectorized calculations |
| 5 | Broadcasting | Handle operations between different shapes |
| 6 | Statistics | Calculate mean, min, max, sum |
| 7 | Performance | Compare Python vs NumPy speed |
| 8 | Practice | Apply NumPy for business sales data |

---

## 🌟 Outcome

By end of Day 39:  
You’ve mastered **NumPy fundamentals** — arrays, broadcasting, math operations, and performance analysis.  
These concepts are **foundation of Machine Learning, Pandas, and Data Science**.

💼 **Resume Tip:**  
> “Utilized NumPy for numerical computations, data transformations, and performance optimization in large-scale datasets.”

---
