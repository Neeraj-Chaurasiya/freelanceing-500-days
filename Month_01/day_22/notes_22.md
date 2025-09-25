# 📅 Day 22 – SQL Advanced Joins, Nested Queries & Constraints

---

## 🗂️ Database Context
We are using the **SalesDB** database with tables:  
- `customers` → CustomerId, Name, City  
- `sale` → SaleId, Product, Category, Price, Quentity, CustomerId  

Today we practice **Self JOIN, FULL OUTER JOIN, Nested Subqueries, and Constraints**.

---

## 1️⃣ Self JOIN

```sql
SELECT c1.Name AS Customer1, c2.Name AS Customer2, c1.City   -- Customers table me self join (same city ke customers find karna)
FROM Customers c1 
JOIN Customers c2 ON c1.City = c2.City AND c1.CustomerId <> c2.CustomerId;
```
- **Self JOIN** → Join a table with itself.  
- `c1` and `c2` → Aliases for the same Customers table.  
- `c1.City = c2.City` → Matches customers from the same city.  
- `c1.CustomerId <> c2.CustomerId` → Prevents matching a customer with themselves.  
👉 Output = Pairs of customers from the same city.

---

## 2️⃣ FULL OUTER JOIN

```sql
SELECT c.Name, s.Product, s.Price   -- Sales aur Customers ka full outer join
FROM Customers c
FULL OUTER JOIN Sale s ON c.CustomerId = s.CustomerId;
```
- **FULL OUTER JOIN** → Returns all rows from both tables.  
- If a customer has no sales → still included with NULL in sales columns.  
- If a sale has no matching customer → included with NULL in customer columns.  
👉 Ensures **no data loss** from either side.

---

## 3️⃣ Nested Subqueries

```sql
SELECT Name FROM Customers   -- Customers who bought products above average price
WHERE CustomerId IN (
    SELECT CustomerId FROM Sale
    WHERE Price > (SELECT AVG(Price) FROM Sale)
);
```
- **Subquery inside WHERE** → Filters customers based on another query.  
- `(SELECT AVG(Price) FROM Sale)` → Finds average price of all products.  
- `WHERE Price > AVG(Price)` → Finds sales above average price.  
- `CustomerId IN (...)` → Matches customers who bought these expensive products.  
👉 Output = Customers who purchased products above average price.

---

## 4️⃣ Constraints Practice

### Create Employees Table with Constraints
```sql
CREATE TABLE Employees (
    EmpId INT PRIMARY KEY IDENTITY(1,1),
    Name NVARCHAR(50) NOT NULL, 
    Email NVARCHAR(100) UNIQUE,
    Age INT CHECK (Age >= 18),
    City NVARCHAR(50) DEFAULT 'Unknown'
);
```
- **PRIMARY KEY** → `EmpId` uniquely identifies each employee.  
- **IDENTITY(1,1)** → Auto-increment starting at 1.  
- **NOT NULL** → Name cannot be empty.  
- **UNIQUE** → Email must be unique for each employee.  
- **CHECK (Age >= 18)** → Age must be 18 or older.  
- **DEFAULT 'Unknown'** → If no city given, default is 'Unknown'.

### Insert Example Employee
```sql
INSERT INTO Employees (Name, Email, Age, City) 
VALUES ('Rohit','rohit@example.com',25,'Delhi');
```
- Inserts a new employee.  
- `EmpId` auto-generated.  
- All constraints validated before inserting.  

---

## 📌 Summary
- **Self JOIN** → Useful to compare rows within the same table.  
- **FULL OUTER JOIN** → Combines all records from two tables (no loss).  
- **Nested Subqueries** → Allow filtering using conditions inside another query.  
- **Constraints** → Enforce rules at table level (Primary Key, Not Null, Unique, Check, Default).  
- These concepts are key for **data integrity, accuracy, and flexibility** in SQL.

---
