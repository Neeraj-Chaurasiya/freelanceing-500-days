
# 📅 Day 36 – Pandas Deep Dive (Part 1): Data Loading & Basic Cleaning

---

## 🎯 Objective

Python ke **Pandas library** ka use karke dataset ko **load**, **inspect**, aur **clean** karna seekhna.  
Ye data analysis ka **first & most important step** hota hai — real-world data ko usable banana.

---

## ✅ Topics Covered

- Importing Pandas Library  
- Loading CSV Dataset  
- Dataset Overview (`head()`, `info()`, `shape`)  
- Renaming Columns  
- Handling Missing Values  
- Changing Data Types  
- Saving Cleaned Data  

---

## 🧩 Step 1 – Import Libraries

```python
import pandas as pd

print("Pandas Version : ", pd.__version__)  # Check Version
```

**Explanation:**
- `import pandas as pd` → Loads the Pandas library with alias `pd`.
- `pd.__version__` → Shows installed version of Pandas.

---

## 🗂 Step 2 – Load Dataset

```python
df = pd.read_csv("c:/Freelanceing (500 days)/Month_02/day_36/data/Sales_data.csv")  # Load csv file

print(df.head()) 
print(df.info())
print("Shape :", df.shape)  # Shape of dataset (rows, columns)
```

**Explanation:**
- `pd.read_csv()` → Loads CSV file into a Pandas DataFrame.
- `df.head()` → Displays first 5 rows.
- `df.info()` → Shows column names, data types, and null counts.
- `df.shape` → Returns dataset dimensions (rows, columns).

💡 **Tip:** Always check `.info()` after loading data to verify column types and missing values.

---

## 🧹 Step 3 – Basic Cleaning

```python
df.rename(columns={"category": "categroy_name", "quantity": "total_quantity"}, inplace=True)  # Rename columns
df.dropna(inplace=True)  # Drop missing values
df["price"] = df["price"].astype(int)  # Convert price column to integer
print(df.info())  
```

**Explanation:**
- `rename()` → Renames columns (for better readability or consistency).
- `dropna()` → Removes rows with missing (NaN) values.
- `astype(int)` → Converts column data type to integer.
- `inplace=True` → Applies changes directly to the DataFrame (without creating a copy).

💡 **Tip:** You can also use `df.fillna(value)` instead of dropping missing data when retention is important.

---

## 💾 Step 4 – Save Cleaned Data

```python
df.to_csv("c:/Freelanceing (500 days)/Month_02/day_36/data/Sales_cleaned_data.csv", index=False)
```
**Explanation:**
- Saves the cleaned DataFrame as a new CSV file.
- `index=False` → Prevents Pandas from writing row numbers in file.

---

## 📈 Step 5 – Quick Statistical Summary

```python
print(df.describe())
```
**Explanation:**
- `describe()` → Generates basic statistical summary (mean, std, min, max, etc.) for numeric columns.
- Helps quickly check for outliers and data consistency.

---

## 🧠 Summary

| Step | Description |
|------|--------------|
| 1 | Import Pandas library |
| 2 | Load CSV dataset using `read_csv()` |
| 3 | Inspect data using `head()`, `info()`, and `shape` |
| 4 | Clean data (rename columns, drop NaN, change types) |
| 5 | Save cleaned dataset to new CSV |
| 6 | Generate summary stats with `describe()` |

---

## 🌟 Outcome

By end of Day 36:  
You learned how to **load, clean, and prepare real-world data** for analysis using Pandas.  
This cleaned dataset will be used in **Day 37** for visualization and deeper analysis.

💼 **Resume Tip:**  
> “Performed data cleaning and preprocessing using Python Pandas, including type conversion, missing value handling, and exporting structured datasets for analysis.”

---
