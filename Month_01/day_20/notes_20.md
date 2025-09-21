# 📘 Day 20 – SQL Aggregations & Subqueries

---

## 🗂️ Database Context
We are working on the `SalesDB` database which contains two tables:
- **customers** → CustomerId, Name, City  
- **sale** → SaleId, Product, Category, Price, Quentity, CustomerId  

This day focuses on **Aggregate Functions, GROUP BY + HAVING, and Subqueries**.

---

## 🔢 Aggregate Functions

### 1. Total Sales Amount
```sql
SELECT SUM(Price * Quentity) AS TotalRevenue 
FROM sale;
```
- **SUM()** → Adds all values together.  
- `Price * Quentity` → Calculates revenue per row.  
- `AS TotalRevenue` → Alias for readability.  
👉 Gives **total revenue from all sales**.

---

### 2. Average Product Price
```sql
SELECT AVG(Price) AS AveragePrice 
FROM sale;
```
- **AVG()** → Returns the average of a numeric column.  
👉 Finds the **average price of all products**.

---

### 3. Number of Customers
```sql
SELECT COUNT(*) AS TotalCustomers 
FROM customers;
```
- **COUNT(*)** → Counts total rows in a table.  
👉 Shows **total number of customers** in the table.

---

### 4. Min & Max Price
```sql
SELECT MIN(Price) AS MinPrice, MAX(Price) AS MaxPrice 
FROM sale;
```
- **MIN()** → Lowest value.  
- **MAX()** → Highest value.  
👉 Finds **cheapest and most expensive product price**.

---

## 🧮 GROUP BY with HAVING

### 5. City with revenue > 50,000
```sql
SELECT c.City, SUM(s.Price * s.Quentity) AS TotalRevenue	
FROM sale s
INNER JOIN customers c ON s.CustomerId = c.CustomerId
GROUP BY c.City
HAVING SUM(s.Price * s.Quentity) > 50000;
```
- **INNER JOIN** → Combines sales with customer city.  
- **GROUP BY c.City** → Groups revenue by city.  
- **HAVING** → Filters groups after aggregation.  
👉 Shows only **cities where total revenue > 50,000**.

---

### 6. City-wise Total Revenue
```sql
SELECT c.City, SUM(s.Price * s.Quentity) AS TotalRevenue
FROM sale s
INNER JOIN customers c ON s.CustomerId = c.CustomerId
GROUP BY c.City;
```
👉 Similar to above but **without HAVING condition**.  
Shows revenue of **all cities**.

---

## 🌀 Subqueries

### 7. Products priced above average price
```sql
SELECT Product, Price
FROM sale
WHERE Price > (SELECT AVG(Price) FROM sale);
```
- Inner query → Finds **average product price**.  
- Outer query → Selects products **priced higher than average**.

---

### 8. Customers who purchased Laptop
```sql
SELECT Name
FROM customers
WHERE CustomerId IN (
    SELECT CustomerId 
    FROM sale 
    WHERE Product = 'Laptop'
);
```
- Inner query → Finds all `CustomerId` who bought "Laptop".  
- Outer query → Returns names of those customers.  

👉 Result = **List of customers who purchased Laptop**.

---

## 📌 Summary
- **SUM, AVG, MIN, MAX, COUNT** → Useful for aggregation.  
- **GROUP BY + HAVING** → For grouped analysis with conditions.  
- **Subqueries** → Query inside another query (used for filtering or calculations).  

✅ This day helps us analyze **sales patterns, city-wise revenue, and customer-product relations** using SQL.

---
