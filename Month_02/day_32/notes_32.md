
# 📅 Day 32 – SQL + Python Data Visualization Project (E-Commerce Analytics)

---

## 🎯 Objective

Python ke through SQL Server se connect karke **data extract**, **analyze**, aur **visualize** karna using Matplotlib & Seaborn — a complete SQL-Python visualization pipeline.

---

## 🧩 Step 1: Import Libraries

```python
import pyodbc
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
```
**Explanation:**
- `pyodbc` → Connect SQL Server with Python.  
- `pandas` → For structured data handling.  
- `matplotlib.pyplot` → Basic plotting.  
- `seaborn` → Beautiful statistical plots.

---

## 🖥 Step 2: Connect to SQL Server

```python
conn = pyodbc.connect(
   'Driver={ODBC Driver 17 for SQL Server};'
   'Server=LAPTOP-HM1JSKBB\\SQLEXPRESS;'
   'Database=ECommerceDB;'
   'Trusted_Connection=yes;'
)
print("Connected Successfully !")
```
**Explanation:**
- Connects to **ECommerceDB** database on local SQL Server instance.  
- Uses Windows authentication (`Trusted_Connection=yes`).  
- Confirms connection with success message.

---

## 📊 Step 3: Fetch Data from SQL Server

```python
query = """
Select c.CustomerName, c.City, p.ProductName, p.Category, (p.Price * s.Quantity) As TotalAmount
From Sales s
Join Customers c On s.CustomerID = c.CustomerID
Join Products p On s.ProductID = p.ProductID
"""

df = pd.read_sql(query, conn)
print(df.head())
```
**Explanation:**
- Performs JOIN on three tables — Sales, Customers, Products.  
- Computes **TotalAmount = Price × Quantity**.  
- Loads result into Pandas DataFrame.

---

## 🧹 Step 4: Data Cleaning & Analysis

### 🔹 Check Missing Values
```python
print(df.isnull().sum())
```
Checks for null or missing values in dataset.

### 🔹 City-wise Revenue
```python
City_revenue = df.groupby('City')['TotalAmount'].sum().sort_values(ascending=False)
print(City_revenue)
```
Calculates total revenue for each city, sorted highest first.

### 🔹 Category-wise Sales
```python
Category_sales = df.groupby('Category')['TotalAmount'].sum().sort_values(ascending=False)
print(Category_sales)
```
Summarizes total sales by product category.

---

## 📈 Step 5: Visualization (Matplotlib + Seaborn)

### 🔹 City-wise Revenue Chart
```python
plt.figure(figsize=(8,5))
sns.barplot(x=City_revenue.index, y=City_revenue.values)
plt.title("City-wise Total Revenue")
plt.xlabel("City")
plt.ylabel("Revenue")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
```
Creates a horizontal bar chart comparing total revenue by city.

---

### 🔹 Category-wise Sales Chart
```python
plt.figure(figsize=(7,4))
sns.barplot(x=Category_sales.index, y=Category_sales.values)
plt.title("Category-wise Total Sales")
plt.xlabel("Category")
plt.ylabel("Total Sales")
plt.tight_layout()
plt.show()
```
Displays category-wise total sales visualization.

---

## 📤 Step 6: Export Results to Excel

```python
with pd.ExcelWriter(r"C:\Freelanceing (500 days)\Month_01\day_32\Outputs\day32_sales_analysis.xlsx") as writer :
  df.to_excel(writer, sheet_name="Raw Data", index=False)
  City_revenue.to_excel(writer, sheet_name="City Revenue")
  Category_sales.to_excel(writer, sheet_name="Category Sales")

print("Excel report exported successfully !")
```
**Explanation:**
- `ExcelWriter()` → Exports multiple sheets in one Excel file.  
- Each sheet stores relevant analysis output.  
- Exports complete data-driven report automatically.

---

## 🧠 Summary

| Step | Task | Tools Used |
|------|------|-------------|
| Import | Load required libraries | pyodbc, pandas, seaborn |
| Connection | Connect Python ↔ SQL Server | pyodbc |
| Data Fetch | Retrieve sales & customer data | SQL Query |
| Cleaning | Check and group data | pandas |
| Visualization | Create plots for insights | seaborn, matplotlib |
| Export | Save report to Excel | ExcelWriter |

---

## 💼 Outcome

By the end of Day-32:
- Built a full SQL → Python → Visualization → Excel pipeline.  
- Automated business report generation.  
- Ready-to-show project for portfolio or resume.

💡 **Resume Tip:**  
> “Built an automated SQL-Python visualization pipeline for e-commerce data, generating insights and Excel reports using Pandas, Seaborn, and SQL Server.”

---
