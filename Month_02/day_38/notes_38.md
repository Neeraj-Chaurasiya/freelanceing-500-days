
# 📅 Day 38 – Pandas Deep Dive (Part 3): Data Visualization & Insights

---

## 🎯 Objective

Python ke **Matplotlib** aur **Seaborn** libraries ka use karke data ko **visualize** karna aur **business insights** draw karna seekhna.  
Ye tumhara data analysis ko ek **presentation-level** form me convert karta hai 📊

---

## ✅ Topics Covered

- Importing & styling Seaborn visualizations  
- Bar charts, line charts, and heatmaps  
- Region & category-wise comparisons  
- Exporting charts as PNG  
- Correlation insights

---

## 🧩 Step 1 – Import Libraries & Load Data

```python
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv(r"C:\Freelanceing (500 days)\Month_02\day_38/data/region_category_sales.csv")
```

**Explanation:**  
- `pandas` → Load CSV data into DataFrame.  
- `matplotlib.pyplot` → For static charts.  
- `seaborn` → For modern and stylish visuals.  
- `read_csv()` → Reads your cleaned dataset from Day 37.

---

## 🎨 Step 2 – Apply Professional Style

```python
sns.set_style("whitegrid")
plt.rcParams["figure.facecolor"] = "white"
plt.rcParams["axes.edgecolor"] = "#333333"
plt.rcParams["axes.labelcolor"] = "#333333"
plt.rcParams["axes.titlesize"] = 14
```

**Explanation:**  
- Adds a professional, white-background chart theme.  
- `rcParams` customizes figure appearance globally.  
- Makes visuals clean and presentation-ready.

💡 Tip: You can use other styles like `"darkgrid"` or `"ticks"`.

---

## 📊 Step 3 – Total Sales by Category & Region (Bar Chart)

```python
plt.figure(figsize=(10,6))
sns.barplot(x="category", y="total_sales", data=df, hue="region")
plt.title("Total Sales by Category & Region", fontsize=14, fontweight="bold")
plt.xlabel("Product Category", fontsize=12)
plt.ylabel("Total Sales (₹)", fontsize=12)
plt.xticks(rotation=45, ha="right")
plt.legend(title="Region")
plt.tight_layout(pad=2.0)
plt.savefig(r"c:/Freelanceing (500 days)/Month_02/day_38/visuals/total_sales_by_category.png")
plt.show()
```

**Explanation:**  
- `sns.barplot()` → Creates grouped bars by category and region.  
- `hue="region"` → Separates data per region for visual comparison.  
- `savefig()` → Saves chart image to your visuals folder.

💡 Insight: Compare sales per region for each product category.

---

## 📈 Step 4 – Average Sales by Region (Horizontal Bar)

```python
plt.figure(figsize=(8,5))
sns.barplot(x="avg_sales", y="region", data=df, ci=None, palette="crest")
plt.title("Average Sales by regions :")
plt.xlabel("Average sale ")
plt.ylabel("Region")
plt.tight_layout()
plt.savefig(r"c:/Freelanceing (500 days)/Month_02/day_38/visuals/avg_sales_by_region.png")
plt.show()
```

**Explanation:**  
- Horizontal barplot compares average sales per region.  
- `palette="crest"` gives gradient effect.  
- `ci=None` removes confidence intervals.

💡 Insight: Which region performs better on average sales?

---

## 📉 Step 5 – Quantity Comparison (Line Plot)

```python
plt.figure(figsize=(8,5))
sns.lineplot(x="category", y="total_qty", hue="region", data=df, marker="o", markersize=10 ,linewidth=2) 
plt.title("Quantity Comparison ")
plt.xlabel("Category")
plt.ylabel("Quantity")
plt.tight_layout()
plt.savefig(r"c:/Freelanceing (500 days)/Month_02/day_38/visuals/quantity_comparison.png")
plt.show()
```

**Explanation:**  
- `sns.lineplot()` → Displays category-wise trend of total quantity.  
- `marker="o"` → Marks each point clearly.  
- `hue="region"` → Adds color-coded region differentiation.

💡 Insight: Detect demand variation by product category across regions.

---

## 🔥 Step 6 – Correlation Heatmap

```python
plt.figure(figsize=(6,4))
corr = df[["total_sales","avg_sales","max_sales","total_qty"]].corr()
sns.heatmap(corr, annot=True, cmap="coolwarm", fmt=".2f")
plt.title("Correlation between sales metrics")
plt.tight_layout()
plt.savefig(r"c:/Freelanceing (500 days)/Month_02/day_38/visuals/region_category_heatmap.png")
plt.show()
```

**Explanation:**  
- `corr()` → Calculates numeric column relationships.  
- `sns.heatmap()` → Visualizes how columns relate to each other.  
- `annot=True` → Displays exact correlation values.

💡 Insight: See if `total_sales` correlates strongly with `total_qty`.

---

## 💾 Step 7 – Export Visuals

All generated visuals are saved in:  

```
C:/Freelanceing (500 days)/Month_02/day_38/visuals/
│
├── total_sales_by_category.png
├── avg_sales_by_region.png
├── quantity_comparison.png
└── region_category_heatmap.png
```

💡 Always store charts with meaningful names for reports.

---

## 🧠 Summary

| Step | Visualization | Purpose |
|------|----------------|----------|
| 1 | Bar Chart | Compare total sales across category & region |
| 2 | Horizontal Bar | Regional average sales analysis |
| 3 | Line Chart | Quantity trends comparison |
| 4 | Heatmap | Correlation between sales metrics |

---

## 🌟 Outcome

By end of Day 38:  
You learned how to build **professional visual reports** with Seaborn + Matplotlib.  
These plots can be used directly in dashboards or client presentations.

💼 **Resume Tip:**  
> “Developed business-ready visualizations in Python using Matplotlib & Seaborn to identify regional and category-level trends.”

---
