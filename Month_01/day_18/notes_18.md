# 📅 Day 18 – SQL Intermediate (Joins & Aggregations)

## ✅ Topics Covered
- Create `Customers` & `Sale` Tables
- Insert Data into Tables
- INNER JOIN (matching data)
- LEFT JOIN (all from left + matching from right)
- Aggregation (SUM, GROUP BY)
- ORDER BY & TOP clause
- Practice: City-wise revenue & Top products

---

## 1️⃣ Use Database
```sql
USE SalesDB;
GO
```
👉 Work inside the existing `SalesDB` database.

---

## 2️⃣ Create Customers Table
```sql
CREATE TABLE Customers (
  CustomerId INT PRIMARY KEY IDENTITY(1,1),
  Name NVARCHAR(50),
  City NVARCHAR(50)
);
```
- `CustomerId` → Auto increment primary key  
- Stores customer **name & city**  

### Insert Sample Customers
```sql
INSERT INTO Customers (Name, City) VALUES
('Amit','Delhi'),
('Neha','Mumbai'),
('Ravi','Kolkata'),
('Priya','Delhi'),
('Karan','Bangalore');
```

---

## 3️⃣ Create Sale Table
```sql
CREATE TABLE Sale (
  SaleID INT PRIMARY KEY IDENTITY(1,1),
  Product NVARCHAR(50),
  Category NVARCHAR(50),
  Price DECIMAL(10,2),
  Quentity INT,
  CustomerId INT FOREIGN KEY REFERENCES Customers(CustomerId)
);
```
- Stores product sales details  
- Linked with **Customers** table using `CustomerId` (foreign key)  

### Insert Sample Sales
```sql
INSERT INTO Sale (Product, Category, Price, Quentity, CustomerId) VALUES
('Laptop','Electronics',50000,1,1),
('Phone','Electronics',20000,2,2),
('Tablet','Electronics',15000,1,3),
('Headphones','Accessories',3000,3,1),
('Keyboard','Accessories',2000,2,4),
('Monitor','Electronics',12000,1,5),
('Mouse','Accessories',1000,5,2);
```

---

## 4️⃣ INNER JOIN (Matching Data)
```sql
SELECT s.SaleID, c.Name, c.City, s.Product, s.Price, s.Quentity
FROM Sale s
INNER JOIN Customers c ON s.CustomerID = c.CustomerID;
```
👉 Returns **only matching records** (customers who made purchases).  

---

## 5️⃣ LEFT JOIN (All Customers + Their Sales)
```sql
SELECT c.Name, c.City, s.Product, s.Price
FROM Customers c
LEFT JOIN Sale s ON c.CustomerID = s.CustomerID;
```
👉 Returns **all customers** and their sales (if available).  
👉 If no sale, product & price will show `NULL`.  

---

## 6️⃣ City-wise Revenue
```sql
SELECT c.City, SUM(s.Price * s.Quentity) AS TotalRevenue
FROM Customers c
INNER JOIN Sale s ON c.CustomerID = s.CustomerID
GROUP BY c.City;
```
👉 Aggregation: Calculate **total revenue per city**.  

---

## 7️⃣ Top 3 Products by Total Sales
```sql
SELECT TOP 3 s.Product, SUM(s.Price * s.Quentity) AS Revenue
FROM Sale s
GROUP BY s.Product
ORDER BY Revenue DESC;
```
👉 Groups sales by **product**  
👉 Orders by total revenue (highest first)  
👉 Shows only **top 3**  

---

## 📊 Summary
- Created `Customers` & `Sale` tables with a **foreign key relationship**.  
- Used **INNER JOIN** to combine only matching rows.  
- Used **LEFT JOIN** to get all customers with/without sales.  
- Learned **GROUP BY + SUM** for revenue analysis.  
- Found **Top 3 products by sales revenue**.  
