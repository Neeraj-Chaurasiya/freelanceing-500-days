# 📅 Day 19 – SQL Advanced Filtering & Functions

## ✅ Topics Covered
- Filtering Queries (`WHERE`, `BETWEEN`, `IN`, `LIKE`, `IS NULL`)
- SQL Functions (String, Numeric, Date)
- ORDER BY Multiple Columns

---

## 1️⃣ Filtering Queries

### a) Price 1000 aur 40000 ke beech
```sql
SELECT * FROM Sale
WHERE Price BETWEEN 1000 AND 40000;
```
👉 `BETWEEN` → Selects values within a range (inclusive).  

---

### b) Product Laptop ya Phone ho
```sql
SELECT * FROM Sale
WHERE Product IN ('Laptop','Phone');
```
👉 `IN` → Matches against multiple values.  

---

### c) Customer ka naam 'N' se start hota ho
```sql
SELECT * FROM Customers
WHERE Name LIKE 'N%';
```
👉 `LIKE` + `%` → Pattern matching (names starting with N).  

---

### d) Jinki sales `NULL` hai
```sql
SELECT c.Name, s.Product  
FROM Customers c 
LEFT JOIN Sale s ON c.CustomerId = s.CustomerId
WHERE s.Product IS NULL;
```
👉 `IS NULL` → Finds customers with no sales.  

---

## 2️⃣ Functions Practice

### a) Customer name length
```sql
SELECT Name, LEN(Name) AS NameLength 
FROM Customers;
```
👉 `LEN()` → Returns string length.  

---

### b) Product ko uppercase
```sql
SELECT Product, UPPER(Product) AS PRODUCT 
FROM Sale;
```
👉 `UPPER()` → Convert text to uppercase.  

---

### c) Price round off (nearest 100)
```sql
SELECT Product, ROUND(Price, -2) AS RoundedPrice 
FROM Sale;
```
👉 `ROUND(Price, -2)` → Rounds price to nearest hundred.  

---

### d) Current date & year
```sql
SELECT GETDATE() AS Today, YEAR(GETDATE()) AS YearNow;
```
👉 `GETDATE()` → Current system date & time.  
👉 `YEAR()` → Extracts year.  

---

## 3️⃣ ORDER BY Multiple Columns
```sql
SELECT * FROM Customers
ORDER BY City ASC, Name DESC;
```
👉 Orders first by **City (A→Z)** and then by **Name (Z→A)**.  

---

## 📊 Summary
- Learned advanced filtering using `BETWEEN`, `IN`, `LIKE`, `IS NULL`.  
- Practiced SQL **functions** → `LEN()`, `UPPER()`, `ROUND()`, `GETDATE()`, `YEAR()`.  
- Used `ORDER BY` with multiple columns for sorting.  
