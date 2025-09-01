# LEARNING DATA ANALYST STEP-BY-STEP.
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

# 📅 Day 6 – Pandas Merge, Join & Concat

## ✅ Topics Covered
- **Concatenation**
  - `pd.concat([df1, df2])` → vertical (rows) combine
  - `pd.concat([df1, df2], axis=1)` → horizontal (columns) combine
- **Merge (SQL JOIN style)**
  - `pd.merge(df1, df2, on="col", how="inner")`
- **Different Types of Joins**
  - `how="left"` → Left Join
  - `how="right"` → Right Join
  - `how="outer"` → Full Outer Join
- **Join using Index**
  - `df1.join(df2, how="outer")`

## 💻 Code Files
- `pandas_merge_day6.ipynb`
- `code.py` (examples)

## 🎯 Practice Task
1. Ek **students DataFrame** banao with columns:  
   `RollNo, Name, Class`.  
2. Ek **marks DataFrame** banao with columns:  
   `RollNo, Subject, Marks`.  
3. Merge karke ek final DataFrame banao jisme:  
   `Student Name + Subject + Marks` ho.  
4. Concatenate karke do alag batches ka students data ek hi DataFrame me lao.  

---

# 📅 Day 7 – Pandas GroupBy & Aggregation

## ✅ Topics Covered
- **Basic GroupBy**
  - `df.groupby("col")["val"].mean()` → group-wise average
- **Multiple Aggregations**
  - `agg(["mean","sum","max","min"])` → ek group ke multiple stats
- **GroupBy on Multiple Columns**
  - `df.groupby(["col1","col2"])["val"].mean()`
- **Sorting Aggregated Results**
  - `.sort_values(ascending=False)`

## 💻 Code Files
- `pandas_groupby_day7.ipynb`
- `code.py` (examples)

## 🎯 Practice Task
1. Ek **sales DataFrame** banao jisme columns ho:  
   `Region, Product, Sales`.  
2. `groupby()` karke har **Region ka total sales** nikaalo.  
3. Har **Product ka average sales** nikaalo.  
4. Top 1 product identify karo jo sabse zyada bikta hai.  

---

# 📅 Day 8 – Pandas Data Cleaning & Preprocessing

## ✅ Topics Covered
- **Missing Values**
  - `df.isnull()` → missing check
  - `df.dropna()` → drop missing rows
  - `df.fillna(value)` → fill missing values
- **Duplicates**
  - `df.duplicated()` → duplicate check
  - `df.drop_duplicates()` → remove duplicates
- **Rename + Replace**
  - `df.rename(columns={"old":"new"})`
  - `df["col"].replace(old, new)`
- **String Cleaning**
  - `.str.strip()` → trim spaces  
  - `.str.upper()` → uppercase  
  - `.str.title()` → title case  

## 💻 Code Files
- `pandas_cleaning_day8.ipynb`
- `code.py` (examples)

## 🚀 Practice Task
1. Ek DataFrame banao jisme:
   - Kuch `NaN` values
   - Duplicate rows
   - Extra spaces in strings  
2. Data cleaning steps apply karke ek **final clean dataset** banao.  
3. GitHub pe upload karo: **pandas_cleaning_day8.ipynb**  

---

## ✅ Expected Output
Tumhe real-world **data cleaning pipeline** samajh aayega:
- Missing values handle karna
- Duplicates remove karna
- Columns rename/replace
- String strip/title/upper  

⚡ Ye freelancing aur industry projects me sabse zyada use hoti skill hai.

