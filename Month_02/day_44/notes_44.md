
# 📅 Day 44 – Power BI Data Modeling (Relations, Star Schema, Measures, DAX Basics)

---

## 🎯 Goals (Aaj kya seekhne wale ho)

- Data Modeling ka proper structure samajhna  
- Star Schema design karna (industry best practice)  
- Tables ke beech relationships banana  
- Cardinality & Cross Filter Direction samajhna  
- Basic DAX Measures banana  
- Power BI model ko clean & optimized rakhna  

---

## 📘 1. What is Data Modeling? (Simple Explanation)

**Data Modeling** ka matlab hai Power BI ko clearly batana:

> Kaun si table kis table se kaise connected hai  
> taaki visuals & calculations correct result dikhayein.

Agar model galat hoga → dashboard bhi galat hoga ❌  
Isliye Data Modeling **dashboard ka backbone** hota hai.

---

## 🔸 Types of Schemas

### ⭐ Star Schema (Recommended)

- Center me **Fact Table**
- Uske around **Dimension Tables**
- Simple, fast & scalable

### ❌ Snowflake / Flat Model (Avoid for beginners)

- Complex joins  
- Slow performance  
- Confusing relationships  

---

## 📘 2. Your Model Architecture (Using eCommerce Dataset)

Tumhare **34,500 rows eCommerce dataset** ke liye best structure:

### 📌 Fact Table (Center)

**Sales**
- order_id  
- customer_id  
- product_id  
- quantity  
- price  
- discount  
- final_amount  
- profit / profit_margin  
- region  
- order_date  

👉 Yahin se **numbers (metrics)** aate hain.

---

### 📌 Dimension Tables

#### 🧾 Dim Products
- product_id (PK)
- category
- price

#### 👤 Dim Customers
- customer_id (PK)
- age
- gender
- region

#### 📅 Dim Date
- order_date (PK)
- year
- month
- day

👉 Dimensions = **filters & slicing ke liye** use hoti hain.

---

## 🧩 3. Relationships Setup (Power BI)

### Steps:
1. Open **Power BI → Model View**
2. Drag & drop keys to create relationships

### 🔗 Required Relationships

| From (Fact) | To (Dimension) | Key | Cardinality |
|-------------|---------------|-----|-------------|
| Sales | Products | product_id | Many-to-One |
| Sales | Customers | customer_id | Many-to-One |
| Sales | Date | order_date | Many-to-One |

---

### ⚙ Cross Filter Direction

- ✅ **Single** (Recommended)
- ❌ Both (only if very advanced use-case)

Single direction = better performance & fewer errors.

---

## ⚠ Very Common Mistakes (Avoid These)

❌ Sab tables ko ek hi table me merge karna  
❌ Many-to-Many relationships banana  
❌ Fact table ko dimension se directly filter karwana  

✔ Always:
- 1 Fact table
- Multiple Dimension tables
- Clean star shape

---

## 🧠 4. Create Basic DAX Measures

Power BI → **Modeling → New Measure**

### ⭐ Common & Important Measures

#### 🔹 Total Sales
```
Total Sales = SUM(Sales[final_amount])
```

#### 🔹 Total Quantity
```
Total Quantity = SUM(Sales[quantity])
```

#### 🔹 Average Profit Margin
```
Avg Profit Margin = AVERAGE(Sales[profit_margin])
```

#### 🔹 Total Orders
```
Total Orders = DISTINCTCOUNT(Sales[order_id])
```

#### 🔹 Total Customers
```
Total Customers = DISTINCTCOUNT(Sales[customer_id])
```

👉 Measures hamesha **Fact Table** se bante hain.

---

## 📊 5. Validate Your Model

Model View me check karo:

✔ No zig-zag or crossing lines  
✔ No circular relationships  
✔ Fact table center me ho  
✔ Dimension tables side me ho  

Agar model clean hai → DAX & visuals accurate honge.

---

## 📌 6. Output of Day 44

By end of today tumhare paas hona chahiye:

✔ Clean Star Schema  
✔ All relationships properly defined  
✔ Basic DAX measures created  
✔ Model View screenshot (portfolio ready)  

---

## 🏁 7. Upload to GitHub

### 📂 Folder Structure

```
Month_02/
├── Day_44_PowerBI_Data_Modeling/
│   ├── DAX_Measures.txt
│   ├── Data_Modeling.pbix
│   ├── notes_44.md

```

---

## 🌟 Outcome

Day 44 ke baad:

- Tum Power BI **Data Modeling confidently samajhne lagoge**
- Star Schema ka real-world use clear ho jayega
- Advanced dashboards ke liye strong foundation ban jayega

💼 **Resume Line:**
> “Designed optimized Power BI data models using star schema, relationships, and DAX measures for accurate business reporting.”

---
