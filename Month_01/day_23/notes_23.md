# 📘 Day 23 – SQL GROUP BY & Window Functions

---

## 🔹 1. Basic GROUP BY

```sql
SELECT c.City, SUM(s.Price * s.Quentity) AS TotalRevenue  -- City-wise total revenue
FROM sale s
JOIN customers c ON s.CustomerId = c.CustomerId
GROUP BY c.City;
```

### Explanation:
- `JOIN customers c ON s.CustomerId = c.CustomerId` → Sale table ko Customers table se join kiya using `CustomerId`.
- `SUM(s.Price * s.Quentity)` → Har city ke total revenue (Price × Quantity) calculate kar raha hai.
- `GROUP BY c.City` → City ke hisaab se grouping kar raha hai, taaki har city ka revenue mile.

---

## 🔹 2. GROUP BY with HAVING

```sql
SELECT c.City, SUM(s.Price * s.Quentity) AS TotalRevenue  -- Sirf un cities ko dikhana jaha revenue > 40000
FROM sale s
JOIN customers c ON s.CustomerId = c.CustomerId
GROUP BY c.City
HAVING SUM(s.Price * s.Quentity) > 40000; 
```

### Explanation:
- `GROUP BY c.City` → City wise grouping.
- `HAVING SUM(...) > 40000` → Sirf un groups (cities) ko show karega jinka total revenue 40,000 se zyada hai.
- `HAVING` → `WHERE` ki tarah hota hai, but yeh **groups** par condition lagata hai.

---

## 🔹 3. Window Function – ROW_NUMBER()

```sql
SELECT CustomerId, Product, Price,  -- Har customer ki purchases ko numbering karna
ROW_NUMBER() OVER(PARTITION BY CustomerID ORDER BY Price DESC) AS RowNum
FROM sale;
```

### Explanation:
- `ROW_NUMBER()` → Har row ko ek unique number deta hai.
- `PARTITION BY CustomerID` → Har customer ke liye numbering alag se shuru hoti hai.
- `ORDER BY Price DESC` → Har customer ke liye sabse mehenga product ko RowNum = 1 milega.

Example:
Customer 1 ke 3 products hain → Unko 1,2,3 numbering mil jaayegi based on price (high → low).

---

## 🔹 4. Window Function – RANK()

```sql
SELECT Product, SUM(Price * Quentity) AS TotalSales,  -- Top selling products by revenue
RANK() OVER(ORDER BY SUM(Price * Quentity) DESC) AS SaleRank
FROM sale
GROUP BY Product;
```

### Explanation:
- `SUM(Price * Quentity)` → Har product ka total sales revenue.
- `GROUP BY Product` → Product ke basis par grouping.
- `RANK() OVER(ORDER BY ...)` → Products ko rank karta hai highest revenue → lowest revenue.
- Agar do products ka sales same hai, unhe same rank milega (aur agla rank skip ho jaayega).

---

## 🔹 5. Window Function – AVG() OVER()

```sql
SELECT Product, SUM(Price * Quentity) AS ProductSales,  -- Har product ke sales ke sath overall average bhi dikhana
AVG(SUM(Price * Quentity)) OVER() AS AvgSales
FROM sale
GROUP BY Product;
```

### Explanation:
- `SUM(Price * Quentity)` → Har product ka sales nikalta hai.
- `GROUP BY Product` → Product ke basis par grouping.
- `AVG(SUM(...) OVER())` → Puri table ka **overall average sales** nikalta hai aur har row ke saath dikhata hai.
- Isliye **AvgSales har product ke liye same value** hoga.

---

## 🚀 Summary

1. **GROUP BY** → Data ko group karne ke liye (jaise city ya product-wise).  
2. **HAVING** → Grouped data par condition lagane ke liye.  
3. **ROW_NUMBER()** → Partition ke andar har row ko ek unique number deta hai.  
4. **RANK()** → Ranking deta hai based on order (ties ke case me same rank).  
5. **AVG() OVER()** → Har row ke sath overall average show karta hai.  

👉 Aaj humne **GROUP BY + Window Functions** seekha jo reporting aur analysis ke liye bahut powerful hai.
