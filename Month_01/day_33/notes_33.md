
# 📅 Day 33 – Power BI Dashboard (Part 1): Connect & Model Data

---

## 🎯 Objective

SQL Server database se Power BI me **data import**, **model**, aur **clean** karna seekhna.  
Ye foundation hai ek **dynamic dashboard** banane ke liye (real-world client style).

---

## ✅ Topics Covered

- Power BI Interface Overview  
- SQL Server se data import karna  
- Table relationships (Data Model)  
- Data transformation using Power Query Editor  
- Basic cleaning (rename, remove columns, format types)

---

## 🧩 Pre-Setup

1. **Install Power BI Desktop**  
   🔗 Download: [https://powerbi.microsoft.com/desktop](https://powerbi.microsoft.com/desktop)

2. Tumhara SQL Database ready ho → **ECommerceDB** (from Day 30).  
3. SSMS me tables check karo:  
   - Sales  
   - Customers  
   - Products ✅

---

## 🚀 Step-by-Step Guide

### 🔹 Step 1 – Launch Power BI
- Open **Power BI Desktop**
- Go to **Home → Get Data → SQL Server**

💡 **Tip:** Shortcut → `Alt + H + D + S` opens the SQL Server connection box.

---

### 🔹 Step 2 – Connect to SQL Server

**Server:** `LAPTOP-XXXX\SQLEXPRESS`  
**Database:** `ECommerceDB`  
**Mode:** Import  
Click **OK**

🧠 Power BI ab tumhare SQL database se data fetch karega.

💡 Import mode is faster; DirectQuery is for live SQL data.

---

### 🔹 Step 3 – Select Tables

Select:  
- Customers  
- Products  
- Sales  

Click **Load**

💡 Loaded tables visible in **Data View** (2nd icon on sidebar).

---

### 🔹 Step 4 – Manage Relationships

Go to **Model View** (3rd icon on sidebar)

Power BI auto-detects:  
```
Sales.CustomerID → Customers.CustomerID
Sales.ProductID → Products.ProductID
```

If missing → Manage Relationships → New → Add manually.

💡 Press `Ctrl + Scroll` to zoom in/out of model view.

---

### 🔹 Step 5 – Clean Data (Power Query Editor)

Go to **Home → Transform Data**

Perform:

| Task | Action |
|------|---------|
| Rename Columns | e.g. `CustomerName → Name` |
| Remove Columns | Right-click → Remove |
| Change Data Types | e.g. `Price → Decimal`, `SaleDate → Date` |
| Add Column | Add Column → Custom Column → `= [Quantity] * [Price]` |

Click **Close & Apply** to load changes.

💡 Press `Ctrl + Z` to undo changes in Power Query.

---

### 🔹 Step 6 – Verify Data Model

Go to **Model View** → You should see:  
`Customers → Sales ← Products`

Hover over arrows to view relationships.

---

### 🔹 Step 7 – Save File

Save as:  
`ECommerce_Dashboard_Part1.pbix`

Recommended folder structure:
```
Month_02/
 ├── Day_33_PowerBI_Connect/
 │   ├── ECommerce_Dashboard_Part1.pbix
 │   ├── README.md
 │   └── screenshots/
 │       ├── model_view.png
 │       ├── query_editor.png
```

💡 Take screenshots of Model View & Query Editor.

---

## ✅ Expected Output

✔ SQL data connected in Power BI  
✔ Clean 3-table relational model  
✔ Data ready for visualization (Day 34)

---

## 🌟 Portfolio Value

- Adds “Power BI Data Modeling & SQL Integration” skill  
- Demonstrates business-ready dashboard foundations  
- Real project-style structure for GitHub portfolio

---

## 💡 Beginner Tips

| Action | Shortcut / Tip |
|--------|----------------|
| Open SQL Connection | `Alt + H + D + S` |
| Switch Views | Left sidebar icons (Report / Data / Model) |
| Rename Fields | Double-click column name |
| Quick Format | Modeling → Format → Currency |
| Manage Relationships | Home → Manage Relationships |
| Export Data | Right-click → Export / Copy Table |

---

## 🧠 Summary

| Step | Description |
|------|--------------|
| 1 | Launch Power BI and connect to SQL Server |
| 2 | Load 3 tables (Customers, Products, Sales) |
| 3 | Manage & verify table relationships |
| 4 | Clean and transform data |
| 5 | Save project and folder setup |

---

## 💼 Outcome

By end of Day 33:  
You created a clean Power BI data model ready for visuals.  
Next → **Day 34: Build E-Commerce Dashboard Visuals (KPIs, charts, insights).**

---
