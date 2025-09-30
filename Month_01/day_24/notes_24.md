# 📘 Day 24 – SQL CTEs, Window Functions & Temp Tables

---

## 🔹 1. Non-Recursive CTE (Common Table Expression)

```sql
With CityRevenue As 
(
  Select c.City,
         Sum(s.Price * s.Quentity) as TotalRevenue
  from sale s
  join customers c On c.CustomerId = s.CustomerId
  Group by c.City
)
Select City, TotalRevenue 
From CityRevenue
Where TotalRevenue > 40000
Order by TotalRevenue DESC;
```

**Explanation:**
- `WITH CityRevenue AS (...)` → Define a temporary result set (CTE).
- Inside query → Joins **sale** and **customers** then groups by city and calculates revenue.
- Outer query → Filters only cities with revenue > 40,000 and sorts descending.

---

## 🔹 2. Derived Subquery (Same as CTE)

```sql
Select City, TotalRevenue
From
(
  Select c.City, Sum(s.Price * s.Quentity) as TotalRevenue
  from sale s
  join customers c on s.CustomerId = c.CustomerId
  Group by c.City
) As t
Where TotalRevenue > 40000
Order by TotalRevenue DESC; 
```

**Explanation:**
- Same logic as above, but instead of `WITH` we use a **subquery in FROM** clause (`AS t`).

---

## 🔹 3. Recursive CTE (Generate numbers 1 to 10)

```sql
With Number As
(
  Select 1 As n
  Union All
  Select n + 1 From Number
  Where n < 10
)
Select n From Number
Option (Maxrecursion 0)
```

**Explanation:**
- First part (`Select 1 As n`) → Anchor query, starting value 1.
- `Union All` + recursive select (`n+1`) → Keep adding +1 until 10.
- `Option (Maxrecursion 0)` → Allow unlimited recursion (otherwise default limit is 100).

Output: Numbers 1, 2, … 10.

---

## 🔹 4. CTE with Window Function (Ranking Products)

```sql
With ProdSales As
(
  Select Product, Sum(Price * Quentity) as Revenue
  From sale
  Group by Product
)
Select Product, Revenue,
       Rank() Over (Order by Revenue DESC) as SaleRank
From ProdSales;
```

**Explanation:**
- Step 1: CTE calculates total revenue per product.
- Step 2: Apply `RANK()` window function → Assigns rank to each product by revenue (highest = 1).

---

## 🔹 5. Temp Table (SELECT INTO)

```sql
Select TOP 5 Product, Sum(Price * Quantity) AS Revenue
Into #TopProducts
From sale
Group by Product
Order by Revenue DESC;
```

**Explanation:**
- `SELECT INTO #TopProducts` → Creates a **temporary table** with top 5 products by revenue.
- Temp tables exist only for the session.

```sql
Select * From #TopProducts;
```
→ View temp table data.

---

## 🔹 6. Using Temp Table in Join

```sql
Select s.*
From sale s
join #TopProducts t on s.Product = t.Product;
```

**Explanation:**
- Joins the temp table with `sale` to fetch detailed rows of only top products.

---

## 🔹 7. Update Example (with Temp Table context)

```sql
UPDATE sale
SET Price = Price * 0.95
WHERE Product = 'Laptop';
```

**Explanation:**
- Reduces the price of Laptop by **5%**.

```sql
SELECT * FROM sale WHERE Product = 'Laptop';
```
→ Verify updated price.

---

## 🔹 8. Drop Temp Table

```sql
DROP TABLE #TopProducts;
```

**Explanation:**
- Manually deletes the temp table.  
- Not mandatory, because SQL auto-drops temp tables at end of session.

---

## 📊 Summary

- **CTE (WITH)** → Temporary named query, easier to reuse.  
- **Recursive CTE** → Useful for generating sequences or hierarchical data.  
- **Derived Subquery** → Alternative to CTE, inline usage.  
- **Window Functions (RANK, etc.)** → Advanced analytics without collapsing rows.  
- **Temp Tables** → Store intermediate results, can be reused within session.  
- **Update with Temp Tables** → Easy for batch modifications.

---
