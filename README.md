# 📅 Day 1 – NumPy Basics

## ✅ Topics Covered
- Introduction to NumPy
- Creating arrays from Python lists
- Array attributes: `type`, `shape`
- Special arrays: `zeros`, `ones`, `eye`, `arange`, `linspace`
- Indexing & slicing (1D and 2D)

## 💻 Code Files
- `numpy_basics_day1.ipynb`

## 🎯 Practice Task
1. Create an array with numbers 1–20.  
2. Print only even numbers.  
3. Create a 4x5 matrix and print:  
   - 2nd row  
   - 3rd column  
   - Last element


# 📅 Day 2 – NumPy Operations & Matrix Handling

## ✅ Topics Covered
- Arithmetic operations on arrays (`+`, `-`, `*`, `/`, `**`)
- Mathematical & statistical functions:
  - `min`, `max`, `mean`, `median`, `std`, `sum`
- Reshape and axis-based operations
  - `reshape()`
  - `sum(axis=0)`, `sum(axis=1)`
- Random number generation
  - `np.random.rand`, `np.random.randint`, `np.random.seed`

## 💻 Code Files
- `numpy_operations_day2.ipynb`

## 🎯 Practice Task
1. Create a 3x3 random integer matrix (values 1–50).  
2. Print row-wise maximum and column-wise minimum.  
3. Create a 1D array (1–16), reshape to 4x4, then print:  
   - Row-wise sum  
   - Column-wise sum


# 📅 Day 3 – Pandas Basics (Series & DataFrame)

## ✅ Topics Covered
- Introduction to **pandas** library  
- **Series (1D data)**  
  - Creating from list  
  - Custom index  
- **DataFrame (2D data)**  
  - Creating from dictionary  
  - Rows & columns overview  
- Basic DataFrame functions  
  - `head()`, `tail()`, `shape`, `info()`, `describe()`

## 💻 Code Files
- `pandas_basics_day3.ipynb`
- `code.py` (examples)

## 🎯 Practice Task
1. Create a student DataFrame with 5 students → Columns: `Name, Age, Marks, City`.  
2. Print first 3 rows (`head(3)`).  
3. Check DataFrame shape and info.  
4. Calculate `Marks` ka mean aur max value.  

---

# 📅 Day 4 – Pandas Indexing, Selection & Filtering

## ✅ Topics Covered
- **Column selection**
  - `df["col"]` → single column (Series)
  - `df[["col1", "col2"]]` → multiple columns (DataFrame)
- **Row selection**
  - `iloc` → index-based (0,1,2…)
  - `loc` → label-based (row labels, specific columns)
- **Conditional filtering**
  - `df[df["Marks"] > 88]`
  - `df[(df["Age"] > 22) & (df["Marks"] >= 88)]`
- **Adding & dropping columns**
  - `df["new_col"] = ...`
  - `df.drop("col", axis=1)`

## 💻 Code Files
- `pandas_indexing_day4.ipynb`
- `code.py` (examples)

## 🎯 Practice Task
1. Ek **employee DataFrame** banao with columns: `EmpID, Name, Age, Department, Salary` (5 employees).  
2. Sirf `Name` aur `Salary` column print karo.  
3. Sirf un employees ko print karo jinki `Salary > 50,000` ho.  
4. Ek naya column **"Bonus"** add karo (Salary ka 10%).  
5. `"Department"` column drop karo.  

---

# 📅 Day 5 – Pandas GroupBy, Aggregate & Pivot Table

## ✅ Topics Covered
- **GroupBy basics**
  - `df.groupby("col")["target"].mean()`
- **Multiple aggregations**
  - `agg(["mean","max","min"])`
- **GroupBy with multiple columns**
  - `df.groupby(["col1","col2"])["target"].sum()`
- **Pivot tables**
  - `df.pivot_table(index="col", values="target", aggfunc="mean")`

## 💻 Code Files
- `pandas_groupby_day5.ipynb`
- `code.py` (examples)

## 🎯 Practice Task
1. Ek **sales DataFrame** banao with columns: `Region, Product, Sales, Profit` (8 rows).  
2. Group by `Region` → total **Sales** nikalo.  
3. Group by `Product` → average **Profit** nikalo.  
4. Ek **Pivot Table** banao jisme:
   - Rows = Region  
   - Columns = Product  
   - Values = Sales sum  

---
