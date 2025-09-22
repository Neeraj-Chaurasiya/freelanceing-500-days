# 📅 Day 21 – SQL Views, Indexes & Stored Procedures

---

## 🗂️ Database Context
We continue working in the **SalesDB** database with tables:
- `customers` → CustomerId, Name, City
- `sale` → SaleId, Product, Category, Price, Quentity, CustomerId

Today focuses on **Views, Indexes, and Stored Procedures**.

---

## 1️⃣ Views

### Create a City-wise Revenue View
```sql
CREATE VIEW CityRevenues AS
SELECT c.City, SUM(s.Price * s.Quentity) AS TotalRevenue
FROM sale s
INNER JOIN customers c ON c.CustomerId = s.CustomerId
GROUP BY c.City;
```
- **CREATE VIEW** → Creates a virtual table based on a query.  
- **INNER JOIN** → Combines sale with customer data.  
- **GROUP BY c.City** → Groups revenue per city.  
- **SUM(s.Price * s.Quentity)** → Calculates total revenue.  
👉 After this, `CityRevenues` can be queried like a table.

### Query the View
```sql
SELECT * FROM CityRevenues;
```
- Returns **city-wise total revenue** stored in the view.

---

## 2️⃣ Indexes

### Create Index on Customers.City
```sql
CREATE INDEX idx_city ON Customers(City);
```
- **CREATE INDEX** → Speeds up search/filtering.  
- Index on `City` column → Faster queries filtering by city.

### Create Index on sale.Product
```sql
CREATE INDEX idx_product ON sale(Product);
```
- Index on `Product` column → Faster product search/aggregation.

---

## 3️⃣ Stored Procedures

### Drop old procedure (if exists)
```sql
DROP PROCEDURE IF EXISTS GetTopProducts;
GO
```
- Ensures **no conflict** when creating new procedure.

### Create Procedure to Get Top N Products by Revenue
```sql
CREATE PROCEDURE GetTopProducts 
    @TopN INT
AS
BEGIN
    SELECT TOP (@TopN) Product, SUM(Price * Quentity) AS TotalRevenue
    FROM sale
    GROUP BY Product
    ORDER BY TotalRevenue DESC;
END;
GO
```
- **CREATE PROCEDURE** → Defines reusable SQL code.  
- `@TopN INT` → Input parameter to control number of products.  
- **TOP (@TopN)** → Returns only top N rows.  
- **GROUP BY Product** → Aggregates revenue per product.  
- **ORDER BY TotalRevenue DESC** → Sort by revenue, highest first.  

### Execute the Procedure
```sql
EXEC GetTopProducts @TopN = 3;
```
- Runs the procedure with **TopN = 3**.  
- Returns **top 3 products by total revenue**.

---

## 📌 Summary
- **Views** → Virtual tables for reusable queries.  
- **Indexes** → Speed up searches/aggregations on large tables.  
- **Stored Procedures** → Encapsulate queries, reusable with parameters.  
- Use **DROP PROCEDURE IF EXISTS** to avoid errors.  
- Combining these features improves **query performance and code reusability**.

---
