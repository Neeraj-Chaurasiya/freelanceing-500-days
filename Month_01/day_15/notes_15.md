# 📅 Day 15 – Books Data Report & Visualization

## ✅ Topics Covered

* Load cleaned dataset
* Summary metrics
* Visualization
* Automated Excel Report

---

## 1️⃣ Load Cleaned Dataset

```python
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

df = pd.read_csv(r"C:\Freelanceing (500 days)\Month_01\day_14\Cleaned data\books_cleaned.csv")
print(df.head())
```

* `read_csv()` → Load cleaned dataset.
* `df.head()` → Show first 5 rows.

---

## 2️⃣ Summary Metrics

```python
total_books = df.shape[0]
avg_price = df["Price"].mean()
avg_rating = df["Rating"].mean()

print("Total books :", total_books)
print("Average price :", avg_price)
print("Average rating :", avg_rating)
```

* `df.shape[0]` → Total number of rows (books).
* `mean()` → Calculate averages for price and rating.

---

## 3️⃣ Visualization (Matplotlib / Seaborn)

### Price Distribution

```python
sns.histplot(df["Price"], bins=20, kde=True)
plt.title("Price distribution")
plt.show()
```

* Histogram with KDE → Distribution of book prices.

### Top 10 Expensive Books

```python
top10 = df.nlargest(10, "Price")
sns.barplot(x="Price", y="Title", data=top10)
plt.title("Top 10 expensive books")
plt.show()
```

* `nlargest()` → Select top 10 by price.
* Horizontal barplot for clear readability.

### Average Price by Rating

```python
avg_by_rating = df.groupby("Rating")["Price"].mean().reset_index()
sns.barplot(x="Rating", y="Price", data=avg_by_rating)
plt.title("Average price by rating")
plt.show()
```

* `groupby()` → Aggregate average price per rating.
* Bar chart for comparison.

---

## 4️⃣ Automated Excel Report (Optional)

```python
with pd.ExcelWriter("books_report.xlsx") as writer:
    df.to_excel(writer, sheet_name="All Books", index=False)
    top10.to_excel(writer, sheet_name="Top10 Expensive", index=False)
    avg_by_rating.to_excel(writer, sheet_name="Avg Price by Rating", index=False)
```

* `writer` → pen hai jisse tum pages bhar rahe ho.
* `with` → kaam khatam hote hi copy apne aap band ho jaati hai.
* `ExcelWriter()` → Save multiple DataFrames into one Excel file.
* `sheet_name` → Each analysis stored in a separate sheet.
* `index=False` → Don’t write row numbers.

---

## 5️⃣ Summary

* Loaded **cleaned dataset** for analysis.
* Calculated summary metrics (total books, average price, average rating).
* Visualized distribution, top 10 expensive books, and average price by rating.
* Generated an **Excel report** with multiple sheets for detailed analysis.
* Key Functions: `nlargest()`, `groupby()`, `mean()`, `ExcelWriter()`.
