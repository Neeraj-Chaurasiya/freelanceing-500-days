
# 📅 Day 42 – Excel Formulas for Analysis (SUMIFS, VLOOKUP, INDEX-MATCH)

---

## 🎯 Objective

Learn **Excel ke powerful analysis formulas** jo data cleaning, lookup aur automation me help karte hain.  
Ye formulas **freelancing dashboards, data validation, aur business reporting** ke liye must-know hain. 💼

---

## ✅ Topics Covered

- Conditional Formulas (SUMIFS, COUNTIFS, AVERAGEIFS)  
- Lookup Formulas (VLOOKUP, INDEX-MATCH)  
- Logical Formulas (IF, Nested IF, IFS)  
- Combined Formulas for Real-world Analysis  

---

## 🔹 1. SUMIFS() — Conditional Summation

Used for **multi-condition total निकालने** ke liye.

### 🧠 Formula Syntax
```
=SUMIFS(sum_range, criteria_range1, criteria1, [criteria_range2], [criteria2], ...)
```

### 💡 Example
Total sales for **Electronics category in South region**:

```
=SUMIFS(H:H, D:D, "Electronics", L:L, "South")
```

👉 H:H = Final Amount  
👉 D:D = Category  
👉 L:L = Region  

### 🧩 Practice Tasks
- Category-wise total revenue  
- Region-wise total revenue  
- Payment method-wise total sales  

💡 **Tip:** SUMIFS can handle multiple filters — very useful for dashboard summaries.

---

## 🔹 2. COUNTIFS() — Conditional Count

Used to count rows that match **multiple conditions**.

### 💡 Example
Count orders where payment is “Credit Card” and Region is “North”:

```
=COUNTIFS(J:J, "Credit Card", L:L, "North")
```

### 💬 Output
Number of sales transactions matching both conditions.

💡 **Pro Tip:** Use COUNTIFS to build KPI cards like “Orders by Region” or “Online vs COD.”

---

## 🔹 3. AVERAGEIFS() — Conditional Average

Average निकालने के लिए जब conditions हों.

### 💡 Example
Average discount for Electronics category:

```
=AVERAGEIFS(E:E, D:D, "Electronics")
```

👉 E:E = Discount column  
👉 D:D = Category column  

💡 **Use Case:** Measure average profit margin or average discount per category.

---

## 🔹 4. VLOOKUP() — Lookup Function (Single Key)

Used when you need to **fetch related information from another sheet**.

### 💡 Example
Find Product Name from Product ID list:

```
=VLOOKUP(C2, Products!A:B, 2, FALSE)
```

📌 C2 → Product ID to search  
📌 Products!A:B → Lookup table range  
📌 2 → Column number from which to return value  
📌 FALSE → Exact match only  

💡 **Tip:** VLOOKUP always searches **left-to-right** and can’t look to the left side.

---

## 🔹 5. INDEX + MATCH — Advanced Lookup

Better than VLOOKUP because ye **left-side lookup aur dynamic columns** support karta hai.

### 💡 Example
```
=INDEX(B:B, MATCH("P234890", C:C, 0))
```

👉 MATCH() finds the row number.  
👉 INDEX() returns the corresponding value.  

💡 **Why Better:**  
- Works in both directions (left or right).  
- Faster in large datasets.  
- Doesn’t break when you insert new columns.

---

## 🔹 6. IF(), Nested IF, and IFS()

Used for applying **conditional logic** in Excel.

### 💡 Example
Profit Margin ke basis par Category define karna:

```
=IF(N2>0.2, "High", IF(N2>0.1, "Medium", "Low"))
```

OR (modern version using IFS):

```
=IFS(N2>0.2, "High", N2>0.1, "Medium", TRUE, "Low")
```

💡 **Tip:** IF formulas are essential for business logic (profit bands, risk levels, status tracking).

---

## 🔹 7. Combine Formulas (Real-World Example)

Real-world scenario jahan **multiple formulas ek sath use** hote hain.

### 💡 Example
Total sales for “Electronics” category and “Credit Card” transactions:

```
=SUMIFS(H:H, D:D, "Electronics", J:J, "Credit Card")
```

💡 Combine conditions dynamically using cell references instead of hard-coded text.

---

## 🚀 Practice Task

### 📘 Task Overview:

Create a sheet → `Formulas_Day42.xlsx`  
Apply the following formulas:

| Task | Formula Used | Expected Output |
|------|---------------|----------------|
| Category-wise Sales | SUMIFS() | Total revenue per category |
| Region-wise Orders | COUNTIFS() | Orders per region |
| Average Discount | AVERAGEIFS() | Avg discount by payment type |
| Lookup Product Name | VLOOKUP / INDEX-MATCH | Product names fetched from another sheet |
| Profit Band | IF() | Label each sale as High / Medium / Low |

💡 Format your tables properly → use borders, colors, and number formats.

---

## 📁 Folder Structure

```
Month_02/
├── Day_42_Excel_Formulas/
│   ├── Formulas_Day42.xlsx
│   ├── notes_42.md
│   ├── screenshots/
│   │   ├── sumifs_example.png
│   │   ├── vlookup_example.png
│   │   ├── if_formula_table.png
│   └── README.md
```

---

## ✅ Expected Output

✔ You’ve applied **7 Excel analysis formulas** practically  
✔ Created **automated summary tables** and **lookups**  
✔ Built base for Excel dashboards and reports  
✔ Understood **real-world automation using formulas**  

---

## 🧠 Summary

| Formula | Use Case | Example |
|----------|-----------|----------|
| SUMIFS() | Conditional total | Total revenue by region & category |
| COUNTIFS() | Conditional count | Count orders by region & payment |
| AVERAGEIFS() | Conditional average | Avg discount per category |
| VLOOKUP() | Lookup value | Fetch Product Name from ID |
| INDEX+MATCH | Dynamic lookup | Find values left or right |
| IF() | Conditional logic | Profit band categorization |

---

## 🌟 Outcome

By end of Day 42:  
You’ll master Excel formulas for business analysis and automation.  
These are **must-have freelancing & corporate reporting skills**.

💼 **Resume Tip:**  
> “Created dynamic Excel dashboards using SUMIFS, COUNTIFS, VLOOKUP, INDEX-MATCH, and conditional logic to automate data analysis and reporting.”

---
