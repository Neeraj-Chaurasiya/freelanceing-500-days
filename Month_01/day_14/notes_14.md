# 📅 Day 14 – Analysis of Scraped Books Dataset

## ✅ Topics Covered

* Load scraped data
* Data Cleaning
* Basic Analysis
* Visualization
* Practice Task

---

## 1️⃣ Load Scraped Data

```python
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv(r"C:\Freelanceing (500 days)\Month_01\day_13\CSV extracted dataset\books_full.csv")

print(df.head())
print(df.info())
```

* `pd.read_csv()` → Load CSV file into DataFrame.
* `df.head()` → Show first 5 rows.
* `df.info()` → Display column info and data types.

---

## 2️⃣ Data Cleaning

```python
df["Price"] = df["Price"].str.replace("Â£","").astype(float)
rating_map = {"One":1,"Two":2,"Three":3,"Four":4,"Five":5}
df["Rating"] = df["Rating"].map(rating_map)
print(df.isnull().sum())
print(df.head())
```

* Remove currency symbol `Â£` from `Price` and convert to float.
* Map textual ratings (`One` → 1, `Two` → 2...) to numeric.
* `isnull().sum()` → Check missing values.

---

## 3️⃣ Basic Analysis

```python
print("Average book price :", df["Price"].mean())
print("Most expensive books :\n",df.loc[df["Price"].idxmax()])
print("Average rating :", df["Rating"].mean())
```

* `mean()` → Calculate average.
* `idxmax()` → Index of maximum price.
* `loc[]` → Access row by index.

---

## 4️⃣ Visualization (Matplotlib/Seaborn)

```python
sns.histplot(df["Price"], bins=20, kde=True)
plt.title("Book price distribution")
plt.show()
```

* Histogram of book prices.
* `bins` → Number of bins.
* `kde=True` → Smooth density curve.

```python
sns.countplot(x="Rating", data=df)
plt.title("Book rating count")
plt.show()
```

* Count plot of book ratings.

---

## 5️⃣ 🚀 Practice Task

```python
print("Top 10 most expensive books : \n", df.groupby("Title")["Price"].max().sort_values(ascending=False).head(10))
print("Average price by rating :", df.groupby("Rating")["Price"].mean())

sns.barplot(x="Rating", y="Price", data=df)
plt.title("Rating vs Average price")
plt.show()
```

* `groupby()` → Aggregate data by Title or Rating.
* `.max()` → Maximum price.
* `.mean()` → Average price.
* Bar plot → Rating vs Average Price.

```python
df.to_csv("books_cleaned.csv", index=False)
print("Saved data to books_cleaned.csv")
```

* Save cleaned dataset to CSV.

---

## 6️⃣ Summary

* Loaded scraped CSV into DataFrame.
* Cleaned `Price` and `Rating` columns.
* Performed basic analysis: average price, most expensive books, average rating.
* Visualized price distribution and rating counts.
* Saved cleaned data for further analysis.
* Key Functions: `read_csv()`, `str.replace()`, `map()`, `groupby()`, `histplot()`, `countplot()`, `barplot()`.
