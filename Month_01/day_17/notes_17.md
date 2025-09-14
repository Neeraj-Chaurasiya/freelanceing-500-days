# 📘 Day 17 -- SQL Basics (Database, Tables, Insert & Queries)

------------------------------------------------------------------------

## 🎯 Topics Covered

-   Creating a new Database
-   Creating Tables with constraints
-   Inserting records into tables
-   Basic `SELECT` queries
-   Filtering with `WHERE`
-   Aggregation with `GROUP BY`
-   Practice Task

------------------------------------------------------------------------

## 🛠 Step 1: Create Database

``` sql
CREATE DATABASE SalesDB;
GO

USE SalesDB;
GO
```

------------------------------------------------------------------------

## 🛠 Step 2: Create Table

``` sql
CREATE TABLE Sales (
    Id INT PRIMARY KEY IDENTITY(1,1),
    Product NVARCHAR(50),
    Category NVARCHAR(50),
    Price DECIMAL(10,2),
    Quentity INT
);
```

------------------------------------------------------------------------

## 🛠 Step 3: Insert Records

``` sql
INSERT INTO Sales (Product, Category, Price, Quentity)
VALUES
('Laptop','Electronics',50000,2),
('Phone','Electronics',20000,5),
('Table','Electronics',15000,3),
('Headphone','Accessories',3000,10),
('Keyboard','Accessories',1500,7);
```

------------------------------------------------------------------------

## 🛠 Step 4: View Data

``` sql
SELECT * FROM Sales;
```

------------------------------------------------------------------------

## 🛠 Step 5: Filtering Data

``` sql
SELECT * FROM Sales WHERE Price > 20000;
```

------------------------------------------------------------------------

## 🛠 Step 6: Aggregation with GROUP BY

``` sql
SELECT Category, SUM(Price * Quentity) AS total_revenue 
FROM Sales 
GROUP BY Category;
```

------------------------------------------------------------------------

## 🚀 Practice Task

### Insert More Data

``` sql
INSERT INTO Sales (Product, Category, Price, Quentity)
VALUES
('Earphone','Electronics',35000,2),
('Earbuds','Electronics',65000,4),
('Speaker','Electronics',15000,4),
('Headphone','Accessories',4000,20),
('Keyboard','Accessories',2500,7),
('Speaker','Electronics',50000,6),
('Phone','Electronics',55000,3),
('Earphone','Electronics',25000,3),
('Earbuds','Accessories',5000,14),
('Keyboard','Accessories',12500,7);
```

### View Updated Data

``` sql
SELECT * FROM Sales;
```

### Filter Expensive Products

``` sql
SELECT * FROM Sales WHERE Price > 30000;
```

### Calculate Total Sales by Category

``` sql
SELECT Category, SUM(Price * Quentity) AS total_sales 
FROM Sales 
GROUP BY Category;
```

------------------------------------------------------------------------

## 📊 Summary

-   Created **SalesDB** database\
-   Defined **Sales** table with `PRIMARY KEY` and `IDENTITY`\
-   Inserted sample records\
-   Practiced **SELECT**, **WHERE**, and **GROUP BY** queries\
-   Inserted additional records for hands-on practice

------------------------------------------------------------------------
