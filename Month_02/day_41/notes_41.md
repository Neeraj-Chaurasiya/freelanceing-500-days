
# 📅 Day 41 – Excel Power Query (Import, Clean & Transform Data)

---

## 🎯 Objective

Learn how to use **Excel Power Query** to **import, clean, and transform raw data** — using the same real eCommerce dataset.  
Power Query is an essential tool for every **Data Analyst** to automate data preparation and cleaning. 💼

---

## ✅ Topics Covered

- Power Query Basics  
- Data Import (CSV → Excel)  
- Column Cleaning & Data Type Conversion  
- Creating Calculated Columns  
- Removing Duplicates & Transformations  
- Exporting Cleaned Data to Excel  

---

## 🧩 Step 1 – Power Query Basics

**Power Query** = Excel ka data transformation engine 🔄  
It helps automate the **ETL process** (Extract, Transform, Load).

### 🧠 Use Cases:
- Importing data (CSV, Excel, SQL Server)
- Cleaning messy data
- Removing duplicates or blanks
- Formatting columns
- Adding new calculated fields

💡 Think of Power Query as “Excel’s built-in mini data pipeline.”

---

## ⚙️ Step 2 – Import Data in Excel

### Steps:
1. Open **Microsoft Excel**
2. Go to **Data Tab → Get Data → From File → From Text/CSV**
3. Select your dataset:  
   `ecommerce_sales_34500.csv`
4. Click **Transform Data**  
   → Opens **Power Query Editor**

💡 This editor is where all your cleaning and transformations happen.

---

## 🧹 Step 3 – Data Cleaning (Inside Power Query Editor)

Perform these cleaning operations step-by-step:

| Step | Action | Description |
|------|---------|-------------|
| ✅ | **Remove Columns** | Delete unnecessary ones like `customer_id` if not needed |
| ✅ | **Rename Columns** | Example: `Total_Amount` → `Total Amount` |
| ✅ | **Filter Rows** | Remove null or blank rows |
| ✅ | **Change Data Types** | `Price` → Decimal, `Quantity` → Whole Number, `OrderDate` → Date |
| ✅ | **Add Calculated Column** | Formula → `Final Amount = Price × Quantity × (1 - Discount)` |

💡 Every transformation step gets recorded automatically in **Applied Steps** (right-side panel).

---

## 🔄 Step 4 – Data Transformations

### Try the following in Power Query:

| Action | Description |
|--------|-------------|
| **Remove Duplicates** | Clean duplicate records based on `OrderID` or `CustomerID` |
| **Group By** | Summarize by `Region` or `Category` |
| **Sort** | Arrange sales data descending by Total Sales |
| **Replace Values** | Example → replace `"COD"` with `"Cash on Delivery"` |

💡 Each transformation is fully reversible — Power Query stores steps as a workflow.

---

## 📤 Step 5 – Load Clean Data Back to Excel

After all cleaning & transformations are done:

1. Click **Close & Load**  
2. Choose **Load to → Excel Sheet**
3. Save the file as →  
   `Cleaned_Sales_Data.xlsx`

💡 The cleaned Excel file will be used in Power BI (Day 43–44).

---

## 🚀 Practice Task

### 🎯 Your Task:

1. Import → `ecommerce_sales_34500.csv`
2. Clean data → Rename, Remove, Filter, Change types
3. Add calculated column → `Final Amount`
4. Export clean dataset → `Cleaned_Sales_Data.xlsx`
5. Take screenshots →  
   - Query Editor view  
   - Cleaned Data Table

### 📂 Folder Structure:

```
Month_02/
├── Day_41_Excel_PowerQuery/
│   ├── Cleaned_Sales_Data.xlsx
│   ├── notes_41.md
│   ├── screenshots/
│   │   ├── query_editor.png
│   │   ├── cleaned_table.png
│   └── README.md
```

---

## ✅ Expected Output

✔ You can **import raw data** using Power Query  
✔ Perform **data cleaning & transformations visually**  
✔ Generate **a clean Excel file ready for analysis**  
✔ Build foundation for Power BI dashboard (Day 43–44)

---

## 🧠 Summary

| Step | Task | Output |
|------|------|---------|
| 1 | Open Power Query | Data Editor launched |
| 2 | Clean & Rename Columns | Properly formatted data |
| 3 | Add Calculated Column | Final Amount created |
| 4 | Remove Duplicates & Sort | Organized dataset |
| 5 | Export | Cleaned_Sales_Data.xlsx saved |

---

## 🌟 Outcome

By end of Day 41:  
You’ve mastered **Power Query basics** — importing, cleaning, and transforming data.  
This is one of the **most demanded skills** for Excel-based Data Analysts.

💼 **Resume Tip:**  
> “Cleaned and transformed raw e-commerce data in Excel Power Query, creating analysis-ready datasets for Power BI dashboards.”

---
