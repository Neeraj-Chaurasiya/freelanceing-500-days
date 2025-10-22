# Import Libraries

import pyodbc
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Connect to Database

conn = pyodbc.connect(
   'Driver={ODBC Driver 17 for SQL Server};'
   'Server=LAPTOP-HM1JSKBB\\SQLEXPRESS;'
   'Database=ECommerceDB;'
   'Trusted_Connection=yes;'
)

print("Connected Successfully !")

# Fetch Data

quary = """
Select c.CustomerName, c.City, p.ProductName, p.Category, (p.Price * s.Quantity) As TotalAmount
From Sales s
Join Customers c On s.CustomerID = c.CustomerID
Join Products p On s.ProductID = p.ProductID
"""

df = pd.read_sql(quary, conn)
print(df.head())

# Clean & Analyze Data

# Check for missing values
print(df.isnull().sum())/

# City-wise revenue
City_revenue = df.groupby('City')['TotalAmount'].sum().sort_values(ascending=False)
print(City_revenue)

# Category-wise sales
Category_sales = df.groupby('Category')['TotalAmount'].sum().sort_values(ascending=False)
print(Category_sales)

# Visualize Insights
# City-wise Revenue Chart

plt.figure(figsize=(8,5))
sns.barplot(x=City_revenue.index, y=City_revenue.values)
plt.title("City-wise Total Revenue")
plt.xlabel("City")
plt.ylabel("Revenue")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# Category-wise Sales Chart

plt.figure(figsize=(7,4))
sns.barplot(x=Category_sales.index, y=Category_sales.values)
plt.title("Category-wise Total Sales ")
plt.xlabel("Category")
plt.ylabel("Total Sales ")
plt.tight_layout()
plt.show()

# Export Results to Excel

with pd.ExcelWriter(r"C:\Freelanceing (500 days)\Month_01\day_32\Outputs\day32_sales_analysis.xlsx") as writer :
  df.to_excel(writer, sheet_name="Raw Data", index=False)
  City_revenue.to_excel(writer, sheet_name="City Revenue")
  Category_sales.to_excel(writer, sheet_name="Category Sales")

print(" Excel report exported successfully !")