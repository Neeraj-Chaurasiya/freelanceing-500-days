
# 📅 Day 31 – SQL + Python Integration Project (E-Commerce Data Analysis)

---

## 🎯 Objective

Python ke through SQL Server se connect karke **data extract**, **analyze**, aur **export** karna Excel me — combining SQL + Python for real-world analytics.

---

## 🧩 Step 1: Import Libraries

```python
import pyodbc
import pandas as pd
```
**Explanation:**
- `pyodbc` → Python library used to connect with SQL Server.  
- `pandas` → For data analysis and exporting results.

---

## 🖥 Step 2: Connect to SQL Server

```python
conn = pyodbc.connect(
    'Driver={ODBC Driver 17 for SQL Server};'
    'Server=LAPTOP-HM1JSKBB\\SQLEXPRESS;'
    'Database=ECommerceDB;'
    'Trusted_Connection=yes;'
)
print("✅ Connected Successfully!")
```

**Explanation:**
- `Driver` → Specifies the ODBC driver for SQL Server (v17).  
- `Server` → Name of your SQL Server instance.  
- `Database` → Database name (`ECommerceDB`).  
- `Trusted_Connection=yes` → Uses Windows authentication.  
- `pyodbc.connect()` → Creates a live connection with SQL Server.

✅ Output: “Connected Successfully!”

---

## 📊 Step 3: Run SQL Query via Python

```python
query = """
SELECT c.CustomerName, p.ProductName, s.Quantity, p.Price, (p.Price * s.Quantity) AS TotalAmount
FROM Sales s
JOIN Customers c ON s.CustomerID = c.CustomerID
JOIN Products p ON s.ProductID = p.ProductID
ORDER BY TotalAmount DESC;
"""

df = pd.read_sql(query, conn)
print(df.head())
```

**Explanation:**
- Triple quotes (`"""`) are used for multi-line SQL queries.  
- Joins three tables: `Sales`, `Customers`, and `Products`.  
- Calculates total amount per sale using `(Price * Quantity)`.  
- `pd.read_sql()` → Executes SQL query and loads result into a **DataFrame**.  
- `df.head()` → Displays first few rows.

---

## 📈 Step 4: Basic Analysis in Python

### 🔹 Top 3 Customers by Revenue

```python
top_customers = df.groupby('CustomerName')['TotalAmount'].sum().nlargest(3)
print(top_customers)
```

**Explanation:**
- Groups data by customer name.  
- Calculates total spending using `.sum()`.  
- `.nlargest(3)` → Shows top 3 high-value customers.

---

### 🔹 Product-wise Sales Summary

```python
Category_sales = df.groupby('ProductName')['TotalAmount'].sum()
print(Category_sales)
```

**Explanation:**
- Groups sales by product name.  
- Sums up the total sales amount.  
- Shows overall performance of each product.

---

## 📤 Step 5: Export Results to Excel

```python
df.to_excel(r'C:\Freelanceing (500 days)\Month_01\day_31\Output\ECommerce_sales_report.xlsx', index=False)
print("Report exported successfully!")
```

**Explanation:**
- `df.to_excel()` → Exports all data to an Excel file.  
- `index=False` → Excludes row index column in Excel.  
- The path points to the project output folder.

✅ Output: “Report exported successfully!”

---

## 🧠 Summary

| Step | Description |
|------|--------------|
| Import Libraries | Load pyodbc & pandas |
| SQL Connection | Connect Python → SQL Server |
| Query Execution | Fetch SQL data into Pandas DataFrame |
| Data Analysis | Perform analytics using pandas |
| Export | Save analysis output into Excel |

---

## 💡 Practical Outcome

By end of Day-31:
- You’ve built a **Python-SQL integrated workflow**.
- Can fetch live SQL data into Python.  
- Analyze business metrics using pandas.  
- Export automated Excel reports.  

💼 Add this to your resume:  
> “Integrated SQL Server with Python using PyODBC and Pandas to automate data analysis and reporting for an e-commerce sales dataset.”

---
