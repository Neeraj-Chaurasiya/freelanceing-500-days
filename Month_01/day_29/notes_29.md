
# 📘 Day 29 – SQL Optimization & Query Performance

This session focuses on **query optimization**, **indexing**, and **performance testing** in SQL Server.

---

## 🧩 Step 1: Enable Query Execution Plan

```sql
SET SHOWPLAN_ALL ON;
GO
SELECT * FROM sale WHERE Product = 'Laptop';
GO
SET SHOWPLAN_ALL OFF;
```
**Explanation:**
- `SET SHOWPLAN_ALL ON` → SQL Server will **not execute** the query but will **display the execution plan** (how SQL plans to retrieve data).
- Used for **query optimization analysis**.
- Turn it off after inspection using `SET SHOWPLAN_ALL OFF`.

---

## ⏱ Step 2: Check Query Execution Time

```sql
SET STATISTICS TIME ON;
SELECT * FROM sale WHERE Product = 'Laptop';
SET STATISTICS TIME OFF;
```
**Explanation:**
- `SET STATISTICS TIME ON` → Displays **CPU time and elapsed time** for query execution.
- Helps compare performance before and after indexing.

---

## ⚙️ Step 3: Create an Index (Performance Boost)

```sql
CREATE INDEX idex_Product ON sale(Product);
```
**Explanation:**
- **Index** speeds up searches on large tables.
- Here, we create an index on the `Product` column to make lookups faster.
- Especially useful for `WHERE` conditions or `JOIN` clauses involving `Product`.

---

## 🚀 Step 4: Recheck Query (After Index)

```sql
SET STATISTICS TIME ON;
SELECT * FROM sale WHERE Product = 'Laptop';
SET STATISTICS TIME OFF;
```
**Explanation:**
- After creating the index, re-run the same query.
- You’ll notice **reduced execution time** due to faster data access using the index.

---

## 🧮 Step 5: Composite Index (Multi-column Index)

```sql
CREATE INDEX indx_category_product ON sale(Product, Category);
```
**Explanation:**
- A **composite index** includes multiple columns.
- Improves queries that use both `Product` and `Category` in filtering or sorting.

---

## 🗑 Step 6: Drop Unused Index

```sql
DROP INDEX indx_category_product ON sale;
```
**Explanation:**
- Removes an index when no longer required.
- Reduces unnecessary storage and update overhead.

---

## ⚖️ Step 7: Compare JOIN vs Subquery Performance

```sql
SET STATISTICS TIME ON;
GO

-- Using JOIN
SELECT c.Name, SUM(s.Price * s.Quantity) AS Total
FROM sale s 
JOIN customers c ON c.CustomerId = s.CustomerId
GROUP BY c.Name;

-- Using Subquery
SELECT Name,
    (SELECT SUM(Price * Quantity)
     FROM sale s
     WHERE s.CustomerId = c.CustomerId) AS Total 
FROM customers c;

GO
SET STATISTICS TIME OFF;
```
**Explanation:**
- Both return total revenue per customer.
- **JOIN** usually performs better because it processes in a single pass using internal joins.
- **Subquery** can be slower since it executes multiple inner queries.

---

## 🧠 Summary

| Concept | Description |
|----------|--------------|
| **Execution Plan** | Shows how SQL retrieves data — used for optimization. |
| **STATISTICS TIME** | Measures query execution time (before/after optimization). |
| **Index** | Speeds up data retrieval on specific columns. |
| **Composite Index** | Multi-column index to optimize complex filters. |
| **JOIN vs Subquery** | JOINs are generally faster and more efficient. |

---

✅ **Practice Tip:** Try running the same query **before and after indexing** to visually compare the **execution time improvement**.
