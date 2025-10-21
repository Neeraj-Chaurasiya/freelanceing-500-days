
# 📅 Day 30 – Mini Project: E-Commerce Database Analysis (End-to-End SQL Case Study)

---

## 🎯 Objective

E-commerce sales data ka use karke real-world business insights nikalna using **advanced SQL concepts** — joins, subqueries, views, functions, procedures, and triggers.

---

## 🧱 Step 1️⃣ – Create Database

```sql
CREATE DATABASE ECommerceDB;
GO
USE ECommerceDB;
GO
```

**Explanation:**
- `CREATE DATABASE` → Creates a new database named **ECommerceDB**.
- `USE ECommerceDB` → Switches context to the new database for further operations.

---

## 🧩 Step 2️⃣ – Create Tables

```sql
CREATE TABLE Customers (
    CustomerID INT PRIMARY KEY IDENTITY,
    CustomerName VARCHAR(100),
    City VARCHAR(50),
    Email VARCHAR(100)
);
```

👉 Stores customer details.

```sql
CREATE TABLE Products (
    ProductID INT PRIMARY KEY IDENTITY,
    ProductName VARCHAR(100),
    Category VARCHAR(50),
    Price DECIMAL(10,2)
);
```

👉 Contains product information such as category and price.

```sql
CREATE TABLE Sales (
    SaleID INT PRIMARY KEY IDENTITY,
    CustomerID INT FOREIGN KEY REFERENCES Customers(CustomerID),
    ProductID INT FOREIGN KEY REFERENCES Products(ProductID),
    Quantity INT,
    SaleDate DATE
);
```

👉 Holds transaction-level data — linking customers with purchased products.

---

## 📤 Step 3️⃣ – Insert Sample Data

```sql
INSERT INTO Customers (CustomerName, City, Email) VALUES
('Ravi Kumar', 'Delhi', 'ravi@gmail.com'),
('Neha Sharma', 'Mumbai', 'neha@gmail.com'),
('Amit Singh', 'Pune', 'amit@gmail.com'),
('Priya Das', 'Kolkata', 'priya@gmail.com');
```

```sql
INSERT INTO Products (ProductName, Category, Price) VALUES
('Laptop', 'Electronics', 60000),
('Phone', 'Electronics', 30000),
('Shoes', 'Fashion', 2500),
('Watch', 'Accessories', 4000);
```

```sql
INSERT INTO Sales (CustomerID, ProductID, Quantity, SaleDate) VALUES
(1, 1, 2, '2025-09-10'),
(2, 2, 1, '2025-09-11'),
(3, 3, 3, '2025-09-12'),
(4, 4, 1, '2025-09-13'),
(1, 2, 1, '2025-09-14');
```

**Explanation:**
- Inserts test data to simulate a real e-commerce business scenario.
- Each sale links a customer to a product with purchase quantity and date.

---

## 🧮 Step 4️⃣ – Business Queries

### 🔹 1. Total Revenue per City
```sql
SELECT c.City, SUM(p.Price * s.Quantity) AS TotalRevenue
FROM Sales s
JOIN Customers c ON s.CustomerID = c.CustomerID
JOIN Products p ON s.ProductID = p.ProductID
GROUP BY c.City;
```
✅ Joins all 3 tables → calculates total revenue per city.

---

### 🔹 2. Top-Selling Product
```sql
SELECT TOP 1 p.ProductName, SUM(s.Quantity) AS TotalSold
FROM Sales s
JOIN Products p ON s.ProductID = p.ProductID
GROUP BY p.ProductName
ORDER BY TotalSold DESC;
```
✅ Finds the most-sold product using `ORDER BY DESC`.

---

### 🔹 3. Customer Who Spent the Most
```sql
SELECT TOP 1 c.CustomerName, SUM(p.Price * s.Quantity) AS TotalSpent
FROM Sales s
JOIN Customers c ON s.CustomerID = c.CustomerID
JOIN Products p ON s.ProductID = p.ProductID
GROUP BY c.CustomerName
ORDER BY TotalSpent DESC;
```
✅ Aggregates revenue spent by each customer → finds the highest spender.

---

### 🔹 4. Category-wise Sales Summary
```sql
SELECT p.Category, SUM(p.Price * s.Quantity) AS TotalSales
FROM Sales s
JOIN Products p ON s.ProductID = p.ProductID
GROUP BY p.Category;
```
✅ Calculates sales grouped by product category.

---

### 🔹 5. Date Range Filter Example
```sql
SELECT s.SaleDate, SUM(p.Price * s.Quantity) AS DailyRevenue
FROM Sales s
JOIN Products p ON s.ProductID = p.ProductID
WHERE s.SaleDate BETWEEN '2025-09-10' AND '2025-09-14'
GROUP BY s.SaleDate
ORDER BY s.SaleDate;
```
✅ Filters data for specific date range and shows daily sales trends.

---

## ⚙️ Step 5️⃣ – Create a View

```sql
CREATE VIEW v_CustomerSalesSummary AS
SELECT c.CustomerName, c.City, SUM(p.Price * s.Quantity) AS TotalSpent
FROM Sales s
JOIN Customers c ON s.CustomerID = c.CustomerID
JOIN Products p ON s.ProductID = p.ProductID
GROUP BY c.CustomerName, c.City;
```

**Explanation:**
- A **view** stores a saved query.
- Simplifies repeated reporting and data visualization.

---

## 🧰 Step 6️⃣ – Create a Stored Procedure

```sql
CREATE PROCEDURE GetSalesByCity @CityName VARCHAR(50)
AS
BEGIN
    SELECT c.CustomerName, SUM(p.Price * s.Quantity) AS TotalSpent
    FROM Sales s
    JOIN Customers c ON s.CustomerID = c.CustomerID
    JOIN Products p ON s.ProductID = p.ProductID
    WHERE c.City = @CityName
    GROUP BY c.CustomerName;
END;
```

➡️ Run:
```sql
EXEC GetSalesByCity 'Delhi';
```

**Explanation:**
- Parameterized procedure → dynamic report generation by city.
- Promotes reusability and cleaner query management.

---

## ⚡ Step 7️⃣ – Add Trigger Example

```sql
CREATE TRIGGER trg_SaleInsert
ON Sales
AFTER INSERT
AS
BEGIN
    PRINT '✅ New Sale Recorded Successfully!';
END;
```
**Explanation:**
- Trigger fires **automatically** after a new sale record is inserted.
- Used for logging, validation, or notification logic.

---

## 📊 Step 8️⃣ – Test Everything

```sql
INSERT INTO Sales (CustomerID, ProductID, Quantity, SaleDate)
VALUES (2, 3, 2, '2025-09-15');
```

✅ Trigger message will appear.  
✅ You can re-run view and stored procedure to verify results.

---

## 🧠 Concepts Covered

✔️ Joins  
✔️ Aggregation  
✔️ Subquery  
✔️ View  
✔️ Stored Procedure  
✔️ Trigger  
✔️ Real-world business logic

---

## 💼 Outcome

By end of Day-30, you will have built a **complete SQL project** for portfolio.

You can add this to GitHub or resume as:  
> “Built an end-to-end SQL case study analyzing e-commerce sales using advanced database concepts (joins, procedures, triggers, and performance optimization).”

---
