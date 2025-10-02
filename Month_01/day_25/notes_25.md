# 📘 Day 25 – SQL Correlated Subqueries & CASE WHEN

---

## 1️⃣ Correlated Subquery – Price Above Average (per Category)

```sql
Select Product, Price
From sale s
Where Price > (
    Select Avg(Price)
    From sale
    Where Category = s.Category
);
```

### 🔎 Explanation
- `From sale s` → Outer query me `sale` table ka alias `s`.  
- `Where Price > (...)` → Har row ka price compare hoga ek subquery ke result se.  
- `Subquery` → `Select Avg(Price) From sale Where Category = s.Category`  
   - Yaha `s.Category` outer query se aata hai → isi liye ye **correlated subquery** hai.  
   - Matlab: Har product ka price uske apne category ke average se compare hoga.  

👉 Result: Sirf wo products jo apni category ke average price se **zyada** hain.

---

## 2️⃣ Average Price per Category (for comparison)

```sql
select Category, avg(Price) as AvgCategory
from sale
group by Category;
```

### 🔎 Explanation
- `Group by Category` → Category wise grouping.  
- `avg(Price)` → Har category ka average price nikalta hai.  
👉 Is result ko correlated subquery ke output ke sath relate kar sakte ho.

---

## 3️⃣ Correlated Subquery – Customers with More than 1 Purchase

```sql
Select c.Name, c.City
From customers c
Where 1 < (
    Select count(*)
    From sale s 
    Where c.CustomerId = s.CustomerId
);
```

### 🔎 Explanation
- `From customers c` → Outer query.  
- Subquery: `Select count(*) From sale s Where c.CustomerId = s.CustomerId`  
   - Ye count karega ki customer ne kitni sales ki hain.  
- `Where 1 < (...)` → Matlab count 1 se zyada ho.  

👉 Output: Sirf wo customers jinhe **1 se zyada purchases** hain.

---

## 4️⃣ CASE WHEN – Categorize Products by Price

```sql
Select Product, Price,
    Case 
        When Price < 10000 Then 'Budget'
        When Price Between 10000 and 40000 Then 'Mid-Range'
        Else  'Premium'
    End As PriceCategory
From sale;
```

### 🔎 Explanation
- `CASE WHEN` → Conditional logic jaisa kaam karta hai.  
- Agar `Price < 10000` → Label = **Budget**  
- Agar `Price 10000–40000` → Label = **Mid-Range**  
- Else → **Premium**  
👉 Har product ko ek price category assign ho jata hai.

---

## 5️⃣ CASE WHEN with Aggregation – City Revenue Category

```sql
Select c.City,
    Sum(s.Price * s.Quantity) As TotalRevenue,
    Case
        When Sum(s.Price * s.Quantity) > 100000 Then 'High revenue'
        When Sum(s.Price * s.Quantity) Between 50000 And 100000 Then 'Medium Revenue'
        Else 'Low Revenue'
    End as RevenueCategory
From sale s 
Join customers c on s.CustomerId = c.CustomerId
Group by c.City;
```

### 🔎 Explanation
- `Sum(s.Price * s.Quantity)` → Har city ka total revenue.  
- `CASE` lagake revenue ranges banayi gayi hain:  
   - `> 100000` → High Revenue  
   - `50000–100000` → Medium Revenue  
   - Else → Low Revenue  
- `Group by c.City` → City-wise grouping.

👉 Output: Har city ke revenue ko ek category assign hota hai.

---

# 📝 Summary

- **Correlated Subquery**: Outer query ke row ke hisaab se subquery execute hoti hai. Example → Price above category average, customers with >1 purchase.  
- **CASE WHEN**: SQL me IF-ELSE ki tarah kaam karta hai, data ko categorize karne ke liye use hota hai.  
- **Combined**: CASE WHEN ko aggregate functions ke sath use karke insights generate kar sakte ho (e.g., city revenue category).

---
