
# 📅 Day 37 – Pandas Deep Dive (Part 2): Data Analysis & Aggregations

---

## 🎯 Objective

Python Pandas ka use karke **data filtering, grouping, aggregation, aur sorting** seekhna.  
Is day me tum real business insights nikaloge from your e-commerce dataset.

---

## ✅ Topics Covered

- Data filtering with conditions  
- Sorting values  
- Grouping data (`groupby()`)  
- Aggregations (sum, mean, count, max, min)  
- Multiple aggregations using `agg()`  
- Unique value analysis  
- Exporting results to CSV  

---

## 🧩 Step 1 – Import & Load Data

```python
import pandas as pd

df = pd.read_csv("c:/Freelanceing (500 days)/Month_02/day_37/data/ecommerce_sales_34500.csv")

print(df.info())
print(df.head(3))
```

**Explanation:**  
- `pd.read_csv()` → Loads CSV file into DataFrame.  
- `df.info()` → Shows column data types and null counts.  
- `df.head()` → Prints first 3 rows to confirm data loading.  

---

## 🔍 Step 2 – Filtering Data

```python
high_sales = df[df["total_amount"] > 1000]  # Filter sales above ₹1,000
print(high_sales.head())

North_Sales = df[df["region"] == 'North']   # Filter for North region
print("North sales count: ", len(North_Sales))
```

**Explanation:**  
- `df[df["column"] > value]` → Filter based on condition.  
- `len()` → Gives total number of rows that match condition.  

💡 Combine filters using `&` (AND) or `|` (OR) for complex filtering.

---

## 🔢 Step 3 – Sorting

```python
df_sort = df.sort_values(by='total_amount', ascending=False)
print(df_sort.head(5))
```

**Explanation:**  
- Sorts rows by total_amount (descending order).  
- Helps find top transactions or customers.

---

## 📊 Step 4 – GroupBy (Like SQL Group By)

```python
Region_revenue = df.groupby('region')['total_amount'].sum().reset_index()
print(Region_revenue.head(4))

category_avg = df.groupby('category')['total_amount'].mean().reset_index()
print(category_avg)
```

**Explanation:**  
- `groupby('region')` groups rows by region.  
- `.sum()` adds all total_amount per region.  
- `.mean()` finds average sales per category.

💡 `reset_index()` converts the group result back into a clean DataFrame.

---

## 🧮 Step 5 – Multiple Aggregations

```python
report = (
    df.groupby(["region", "category"])
    .agg(
        total_sales=("total_amount", "sum"),
        avg_sales=("total_amount", "mean"),
        max_sales=("total_amount", "max"),
        total_qty=("quantity", "sum")
    )
    .reset_index()
    .sort_values(by="total_sales", ascending=False)
)

print(report.head())
```

**Explanation:**  
- `agg()` lets you apply **multiple aggregations** in one line.  
- Creates a summary table of total, average, max, and quantity sold.  
- Sorted by total sales (highest first).

---

## 🏆 Step 6 – Top N Analysis

```python
top_Product = df.groupby("category")["total_amount"].sum().reset_index().sort_values(by="total_amount", ascending=False)
print(top_Product.head(5))
```

**Explanation:**  
- Groups data by category → sums total amount → sorts in descending order.  
- `head(5)` → shows top 5 categories.

---

## 🔢 Step 7 – Unique & Count Analysis

```python
print("Unique Regions : ", df["region"].nunique())
print("Unique Categories : ", df["category"].unique())
print(df["category"].value_counts())
```

**Explanation:**  
- `nunique()` → Counts distinct values.  
- `unique()` → Lists unique category names.  
- `value_counts()` → Shows category-wise record counts.

---

## 💾 Step 8 – Export Final Report

```python
report.to_csv(r"c:/Freelanceing (500 days)/Month_02/day_37/Outputs/region_category_sales.csv", index=False)
print("Report exported successfully")
```

**Explanation:**  
- Saves final grouped report as CSV.  
- `index=False` removes index column from output file.

---

## 🧠 Summary

| Step | Description |
|------|--------------|
| 1 | Load dataset with Pandas |
| 2 | Filter and subset data |
| 3 | Sort data by values |
| 4 | Group by region/category |
| 5 | Perform multiple aggregations |
| 6 | Identify top categories |
| 7 | Analyze unique and count values |
| 8 | Export summary report to CSV |

---

## 🌟 Outcome

By end of Day 37:  
You can perform **data summarization and analysis** similar to SQL `GROUP BY`, `ORDER BY`, and `WHERE` queries using Pandas.

💼 **Resume Tip:**  
> “Performed end-to-end e-commerce data analysis using Python Pandas including filtering, sorting, grouping, and exporting reports for business insights.”

---
