# Import Libraries

import pyodbc
import pandas as pd 

# Connect to SQL Server

conn = pyodbc.connect(
    'Driver={ODBC Driver 17 for SQL Server};'
    'Server=LAPTOP-HM1JSKBB\\SQLEXPRESS;'
    'Database=ECommerceDB;'
    'Trusted_Connection=yes;'
)

print("✅ Connected Successfully!")

# Run SQL Query via Python

quary = """
Select c.CustomerName, p.ProductName, s.Quantity , p.Price, (p.Price * s.Quantity) As TotalAmount
From Sales s
join Customers c on s.CustomerID = c.CustomerID
join Products p on s.ProductID = p.ProductID
Order by TotalAmount Desc;
"""

df = pd.read_sql(quary, conn)
print(df.head())

# Basic Analysis in Python

# Top 3 customers by revenue

top_customers = df.groupby('CustomerName')['TotalAmount'].sum().nlargest(3)
print(top_customers)

# Category-wise sales summary
Category_sales = df.groupby('ProductName')['TotalAmount'].sum()
print(Category_sales)

# Export Results to Excel

df.to_excel(r'C:\Freelanceing (500 days)\Month_01\day_31\Output\ECommerce_sales_report.xlsx', index=False)
print("Report exported successfully !")
