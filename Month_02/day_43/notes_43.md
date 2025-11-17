
# 📅 Day 43 – Excel Charts + Dashboards (Professional Level)

---

## 🎯 Goal

Create a **dynamic professional Excel dashboard** using charts, slicers, and advanced formatting.  
This lesson focuses on **visual storytelling** with your eCommerce dataset — transforming raw numbers into business insights. 📊

---

## ✅ 1. Dataset Ready?

Use the same file → **`ecommerce_sales_34500.xlsx`**  

Ensure these columns exist:

| Column Name | Description |
|--------------|-------------|
| Category | Product Category |
| Price | Unit Price |
| Quantity | Number of Items Sold |
| Discount | % Discount Applied |
| Final Amount | Net Revenue (Price × Quantity × (1 - Discount)) |
| Payment Method | e.g., UPI, COD, Credit Card |
| Region | North, South, East, West |
| Order Date | Date of Purchase |
| Delivery Time Days | Days to Deliver |

💡 Tip: Make sure all data types are correct (dates, numbers, text).

---

## ✅ 2. Create Summary Tables (Using Pivot Tables)

### Step 1️⃣ – Insert Pivot Table
1. Select entire dataset → **Ctrl + A**
2. Go to → **Insert → PivotTable**
3. Select → **New Worksheet**

### Step 2️⃣ – Create These Pivot Tables

| Pivot Table | Rows | Values | Purpose |
|--------------|------|---------|----------|
| Pivot 1 | Category | Sum of Final Amount | Category-wise sales |
| Pivot 2 | Region | Sum of Final Amount | Regional performance |
| Pivot 3 | Order Date (Group by Month + Year) | Sum of Final Amount | Monthly sales trend |
| Pivot 4 | Payment Method | Count of Order_ID | Payment usage count |

💡 Tip: Rename pivots clearly (Pivot_Category, Pivot_Region, etc.)

---

## ✅ 3. Convert Pivot Tables into Charts

| Chart Type | Source Pivot | Description |
|-------------|---------------|--------------|
| **Chart 1:** Column Chart | Pivot 1 | Category-wise Total Sales |
| **Chart 2:** Bar Chart | Pivot 2 | Region-wise Total Revenue |
| **Chart 3:** Line Chart | Pivot 3 | Monthly Sales Trend |
| **Chart 4:** Pie Chart | Pivot 4 | Payment Method Distribution |

### 🧩 Customization Tips:
- Add **Data Labels** → for clarity
- Use **Professional Colors** (blue/green tones)
- Add **Bold Titles**
- Remove chart borders for a clean design

---

## ✅ 4. Add Slicers (Dashboard Filtering)

Make your dashboard **interactive** using slicers!

### Steps:
1. Select any Pivot Table  
2. Go to → **PivotTable Analyze → Insert Slicer**
3. Add slicers for:
   - Category
   - Region
   - Payment Method
   - Year

### 📌 Important:
Right-click each slicer → **Report Connections** → tick all pivot tables → apply slicer to all charts.

💡 Slicers act as dashboard filters that instantly update all visuals.

---

## ✅ 5. Build Dashboard Page

### Create a New Sheet
Rename → `Dashboard_Day43`

### Layout Guide (2×2 Grid)
| Row | Chart |
|------|--------|
| Row 1 | Category Sales & Region Sales |
| Row 2 | Monthly Trend & Payment Method Pie |

### Add KPIs (Cards / Metrics)
- Total Sales → `=SUM(Final Amount)`  
- Total Orders → `=COUNTA(Order_ID)`  
- Total Customers → `=COUNTA(UNIQUE(Customer_ID))`  
- Average Profit Margin → (if applicable)

### Add Title
Use **Insert → Shapes → Rectangle → "Sales Dashboard"**  
Format with soft shadow + color fill.

💡 Arrange everything neatly — make it look “client-ready.”

---

## 🎨 6. Professional Formatting Rules

Follow these formatting best practices:

| Element | Style |
|----------|--------|
| Background | White / Light Grey |
| Theme | Blue or Green |
| Chart Fonts | Calibri / Segoe UI (12–14 pt) |
| Title Font | Bold, 16 pt |
| Gridlines | Remove for clarity |
| Chart Borders | None (use shadows instead) |
| KPI Cards | Bold numbers with subtle background |

💡 Simplicity = Professionalism.

---

## 📝 7. Save + Export

Once dashboard is ready:

1. Save Excel file as → `eCommerce_Dashboard.xlsx`
2. Go to → **File → Export → Create PDF/XPS**
3. Export as `Dashboard.pdf`

This PDF version can be shared with clients or recruiters.

---

## 📤 8. Upload to GitHub

Create structure:

```
Month_02/
├── Day_43_Excel_Dashboard/
│   ├── eCommerce_Dashboard.xlsx
│   ├── Dashboard.pdf
│   ├── notes_43.md
│   ├── README.md
│   └── screenshots/
│       ├── dashboard_full.png
│       ├── category_chart.png
│       ├── region_chart.png
│       ├── slicers_view.png
```

💡 Include screenshots for GitHub and LinkedIn portfolio posts.

---

## 🎯 9. Expected Output

By the end of Day 43, you’ll have:

✔ Category-wise Sales Chart  
✔ Region-wise Sales Chart  
✔ Monthly Trend Line Chart  
✔ Payment Method Pie Chart  
✔ Interactive Slicers  
✔ KPI Cards & Title  
✔ Fully formatted Dashboard  
✔ PDF Export + GitHub Upload  

---

## 🌟 Outcome

You’ve built a **Professional Excel Sales Dashboard** with interactivity and automation.  
This is a **real-world project** recruiters love to see in a portfolio.

💼 **Resume Tip:**  
> “Designed interactive Excel dashboards with Pivot Tables, charts, slicers, and KPIs to visualize e-commerce sales trends and business performance.”

---
