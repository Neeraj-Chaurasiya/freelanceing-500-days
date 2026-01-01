
# 📅 Day 48 – Python + Power BI Automation (Step-by-Step)

---

## 🎯 Objective

Build an **automated data pipeline using Python** and connect its output directly to **Power BI**.

👉 Ye step tumhe **manual analyst se automation-driven analyst** banata hai 🔥

---

## 🧩 Step 1: Same Dataset Use Karna (IMPORTANT)

✔ Dataset **change nahi hoga**  
✔ Sirf **processing method change hogi**

### 📂 Dataset
```
ecommerce_sales_34500.csv
```

### 🧠 Real-World Logic
- Companies rarely change datasets daily  
- They change **pipelines, transformations & logic**  

👉 Isi wajah se same dataset use kar rahe hain.

---

## 🐍 Step 2: Python Automation Script

### 📁 Folder Structure

```
Day_48/
├── data/
│   ├── ecommerce_sales_34500.csv
│   ├── processed_sales.csv
│   └── region_summary.csv
├── python_pipeline.py
└── notes.md
```

---

### 🧪 python_pipeline.py (Core Automation)

```python
import pandas as pd

# Load data
df = pd.read_csv("data/ecommerce_sales_34500.csv")

# Basic cleaning
df["order_date"] = pd.to_datetime(df["order_date"])

# Business logic
df["final_amount"] = df["price"] * df["quantity"] * (1 - df["discount"])

# Aggregation (example)
summary = df.groupby("region")["final_amount"].sum().reset_index()

# Save outputs
df.to_csv("data/processed_sales.csv", index=False)
summary.to_csv("data/region_summary.csv", index=False)

print("✅ Data processed & exported successfully")
```

---

### 🔍 Script Kya Karta Hai?

✔ Raw CSV load karta hai  
✔ Date column clean karta hai  
✔ Business logic apply karta hai (Final Amount)  
✔ Aggregated summary banata hai  
✔ Power BI ke liye clean CSV export karta hai  

👉 Ye **real client-style Python pipeline** hai.

---

## 📊 Step 3: Power BI me Python Output Connect Karna

### Steps:
1. Open **Power BI Desktop**
2. Click → **Get Data**
3. Select → **Text/CSV**
4. Choose → `processed_sales.csv`
5. Click → **Load**

👉 Ab Power BI **direct Python ke output** pe kaam kar raha hai 🔥

---

## 🔁 Step 4: Automation Concept (MOST IMPORTANT)

### 🧠 Workflow Samjho:

```
Raw CSV
   ↓
Python Script (Automation)
   ↓
Processed CSV
   ↓
Power BI Refresh
```

### 🗣 Client Ko Bolne Wali Line:
> “This dashboard is powered by an automated Python data pipeline.”

💡 Freelancing proposals & interviews me ye line **gold** hai.

---

## 📝 Step 5: notes.md Me Kya Likha

```md
# 📅 Day 48 – Python + Power BI Integration

## Objective
Build an automated data pipeline using Python and connect it with Power BI.

## What I Did
- Loaded raw sales data in Python
- Cleaned & transformed data
- Calculated final sales amount
- Exported processed CSV
- Connected Power BI to Python output

## Tools Used
- Python (Pandas)
- Power BI Desktop

## Key Learning
- Python can act as a data engine
- Power BI works as visualization layer
- This approach is used in real client projects
```

---

## ⭐ Day 48 ka REAL VALUE

✔ Python + Power BI integration  
✔ Automation mindset develop hua  
✔ Freelancing proposal me likhne layak skill  
✔ Interview me **strong talking point**  

---

## 🌟 Outcome

Day 48 ke baad:

- Tum **Python + BI integrated workflow** bana chuke ho  
- Manual analysis se automation ki taraf shift ho gaya  
- Day 49–50 ke **final Power BI project** ke liye ready ho 🚀  

💼 **Resume Line:**
> “Built an automated Python data pipeline and integrated it with Power BI for dynamic sales reporting.”

---
