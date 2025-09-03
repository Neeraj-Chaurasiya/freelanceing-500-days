# LEARNING DATA ANALYST STEP-BY-STEP.

# 📅 Day 1 – NumPy Basics

## ✅ Topics Covered
- Introduction to NumPy
- Creating arrays from Python lists
- Array attributes: `type`, `shape`
- Special arrays: `zeros`, `ones`, `eye`, `arange`, `linspace`
- Indexing & slicing (1D and 2D)

## 🎯 Practice Task
1. Create an array with numbers 1–20.  
2. Print only even numbers.  
3. Create a 4x5 matrix and print:  
   - 2nd row  
   - 3rd column  
   - Last element

---

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

## 🎯 Practice Task
1. Create a 3x3 random integer matrix (values 1–50).  
2. Print row-wise maximum and column-wise minimum.  
3. Create a 1D array (1–16), reshape to 4x4, then print:  
   - Row-wise sum  
   - Column-wise sum  

---

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

---

# 📅 Day 9 – Exploratory Data Analysis (EDA – Part 1)

## ✅ Topics Covered
- **Dataset Load & Info**
  - `pd.read_csv()` → dataset import
  - `.head()`, `.info()`, `.describe()` → dataset samajhna
- **Univariate Analysis**
  - `.mean()`, `.value_counts()`, `.unique()` → single column analysis
- **Bivariate Analysis**
  - `.groupby()` → relation between two columns
- **Visualization (Matplotlib Basics)**
  - Histogram → distribution
  - Bar Plot → average comparison
  - Scatter Plot → relation between numeric columns

## 🚀 Practice Task
Dataset: **tips.csv**  
1. Find **highest tip kis day pe di gayi**  
2. Calculate **Male vs Female average bill difference**  
3. Scatter plot banao: `size` vs `total_bill`  

Upload: **eda_day9.ipynb** to GitHub.

---

## ✅ Expected Output
- Dataset ka **overview** samajh aayega  
- Univariate + Bivariate analysis clear hoga  
- Basic **EDA plots** (histogram, bar, scatter) seekh jaoge  

⚡ Ye har Kaggle project aur freelancing analysis ka **Step-1** hai.  

---

# 📅 Day 10 – Exploratory Data Analysis (EDA – Part 2, Seaborn)

## ✅ Topics Covered
- **Seaborn Setup**
  - `sns.histplot`, `sns.boxplot` → distribution + outliers
  - `sns.barplot`, `sns.countplot` → categorical comparison
  - `sns.scatterplot`, `sns.lineplot` → relationships
  - `sns.heatmap` → correlation matrix

## 📊 Visualizations
1. **Distribution Plots**
   - Histogram (total_bill)
   - Boxplot (bill per day)
2. **Categorical Plots**
   - Barplot (avg bill by day)
   - Countplot (gender count)
3. **Relationship Plots**
   - Scatterplot (bill vs tip, hue=sex)
   - Lineplot (bill by group size)
4. **Heatmap**
   - Correlation matrix

## 🚀 Practice Task
Dataset: **tips.csv**  
1. Male vs Female **average tip** ka barplot banao.  
2. Day-wise **bill distribution** ka boxplot banao.  
3. Heatmap banao aur identify karo → **tip ke saath sabse zyada correlated column** kaunsa hai.  

---

## ✅ Expected Output
- Distribution, categorical, relationship aur heatmap plots ka mastery.  
- Gender, day aur correlation-based analysis kar paoge.  
- EDA ke visualization step me confidence aayega 🚀  
