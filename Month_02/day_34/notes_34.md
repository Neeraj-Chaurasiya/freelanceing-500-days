
# 📅 Day 34 – Power BI Dashboard (Part 2): Visual Design & Insights

---

## 🎯 Objective

SQL data se Power BI me **interactive dashboard** banana jisme ho — Revenue by City, Top Products, Category Trends, aur KPIs.  
Ye tumhara **first professional Power BI dashboard project** hoga jo GitHub + LinkedIn dono pe upload kar sakte ho 💼

---

## ✅ Topics Covered

- Creating visuals in Power BI  
- Revenue & Product performance charts  
- KPI cards (Total Revenue, Customers, Sales Count)  
- Adding filters (Slicers)  
- Formatting & theme design  

---

## 🧩 Pre-Setup

- Database: **ECommerceDB**  
- Model ready from **Day 33** (Customers, Products, Sales linked)  
- Column available: **TotalAmount (Price × Quantity)**  

---

## 🚀 Step-by-Step Practice

### 🔹 Step 1 – Open your Power BI file

Open file:  
`ECommerce_Dashboard_Part1.pbix`  

Then click:  
**File → Save As → ECommerce_Dashboard_Part2.pbix**

💡 This ensures your original data model stays safe.

---

### 🔹 Step 2 – Create Key KPI Cards

Go to **Report View** (middle icon on left sidebar)

Create KPI Cards for:

| KPI | Field | Aggregation |
|------|--------|-------------|
| Total Revenue | TotalAmount | SUM |
| Total Quantity Sold | Quantity | SUM |
| Total Customers | CustomerName | DISTINCTCOUNT |

💡 Tip: Use **Insert → Card Visual**, then drag fields into the card.

🧠 Rename each visual title clearly (e.g., *Total Revenue*, *Total Customers*).

---

### 🔹 Step 3 – City-wise Revenue Chart

Use **Bar Chart** visual from right panel.

| Setting | Field |
|----------|--------|
| Axis | City (from Customers) |
| Values | TotalAmount (SUM) |

🧠 Title → “City-wise Revenue”  
💡 Tip: Turn **Data Labels = ON** for clarity.

---

### 🔹 Step 4 – Category-wise Sales Chart

Add another **Bar Chart**:

| Setting | Field |
|----------|--------|
| Axis | Category (from Products) |
| Values | TotalAmount (SUM) |

🧠 Sort → Descending by Total Sales  
🧠 Title → “Category-wise Total Sales”

💡 Tip: Use different color to make this chart stand out.

---

### 🔹 Step 5 – Top 5 Products by Revenue

Add **Column Chart**:

| Setting | Field |
|----------|--------|
| Axis | ProductName |
| Values | TotalAmount (SUM) |

Then apply visual filter:  
**Top N → N = 5 → Apply Filter**

🧠 Title → “Top 5 Products by Revenue”  
💡 Add data labels for better visibility.

---

### 🔹 Step 6 – Date-wise Trend (Line Chart)

Use **Line Chart** visual.

| Setting | Field |
|----------|--------|
| Axis | SaleDate |
| Values | TotalAmount (SUM) |

🧠 Title → “Revenue Over Time”  
💡 Great for showing performance trends across days.

---

### 🔹 Step 7 – Add Filters (Slicers)

Go to **Insert → Slicer**  
Add slicers for:

- City  
- Category  

💡 These slicers allow **interactive dashboard filtering**, similar to real business dashboards.

---

### 🔹 Step 8 – Format & Design

🎨 Go to **View → Themes** → Select “Executive” or “Minimal”.

Recommended layout:

```
Row 1: KPI Cards (Revenue | Quantity | Customers)
Row 2: Charts (City-wise | Category | Top 5 Products)
Row 3: Line Chart + Slicers
```

💡 Design Tips:  
- Background: Light grey or white  
- Accent Colors: Blue / Orange  
- Font Size: 14–16 for titles  
- Remove gridlines for clean visuals  

---

### 🔹 Step 9 – Export Dashboard

Go to **File → Export →**  
- **PDF** → For client reports  
- **PBIX** → For GitHub upload  
- Take **screenshots** for LinkedIn post

Recommended folder structure:

```
Month_02/
 ├── Day_34_PowerBI_Dashboard/
 │   ├── ECommerce_Dashboard_Part2.pbix
 │   ├── README.md
 │   └── screenshots/
 │       ├── city_revenue_chart.png
 │       ├── category_sales_chart.png
 │       ├── top5_products.png
 │       ├── kpi_cards.png
 │       ├── line_chart.png
```

---

## ✅ Expected Output

✔ Professional Power BI dashboard ready  
✔ Interactive filters & KPIs working  
✔ Business insights clearly visible  
✔ Project ready for GitHub & LinkedIn 🚀

---

## 🌟 Portfolio Value

- Proof of ability to **build dashboards from SQL data**  
- **Freelancing-ready visualization skill**  
- Adds **strong visual storytelling** power to your resume  
- Perfect showcase for LinkedIn / GitHub portfolio

---

## 🧠 Summary

| Step | Description |
|------|--------------|
| 1 | Open existing Power BI model and save new version |
| 2 | Create KPI Cards (Revenue, Quantity, Customers) |
| 3 | Add charts for City, Category, and Top Products |
| 4 | Add line chart for trend analysis |
| 5 | Add slicers for interactivity |
| 6 | Apply themes, format, and export project |

---

## 💼 Outcome

By end of Day 34:  
You built a **professional interactive Power BI dashboard** from SQL data, ready for client presentations or your portfolio.

🧩 Next (Day 35): Learn how to **Publish Dashboard to Power BI Service** and share it online.

---
