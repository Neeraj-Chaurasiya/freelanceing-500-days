# Sales Analysis Notes

## 1️⃣ Dataset Load

```python
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
```

* `pandas` → Data handling (DataFrame creation, cleaning, analysis).
* `matplotlib.pyplot` → Basic plotting.
* `seaborn` → Advanced statistical plots, easy styling.

```python
data = { ... }
df = pd.DataFrame(data)
print(df.head())
```

* `data` → Python dictionary containing sample sales data.
* `pd.DataFrame()` → Convert dictionary to tabular DataFrame.
* `df.head()` → Show first 5 rows.

---

## 2️⃣ Data Cleaning

```python
print(df.isnull().sum())
```

* `isnull()` → Check missing values (NaN).
* `sum()` → Count total missing per column.

```python
duplicate = df.duplicated().sum()
print("Total Duplicates : ",duplicate)
```

* `duplicated()` → Check duplicate rows.
* `sum()` → Count total duplicates.

```python
df["Quantity"] = df["Quantity"].fillna(0)
df["Category"] = df["Category"].fillna("Electronics")
```

* `fillna()` → Replace missing values with given value.

```python
df["Product"] = df["Product"].str.strip()
df["Region"] = df["Region"].str.strip()
```

* `str.strip()` → Remove extra spaces from strings.

---

## 3️⃣ Basic EDA (Exploratory Data Analysis)

```python
print("Total Revenue: ", (df["Quantity"]*df["Price"]).sum())
```

* Multiply `Quantity * Price` → Revenue per row.
* `sum()` → Total revenue.

```python
print("Top sales products :", df.groupby("Product")["Quantity"].sum().sort_index(ascending=False).head(1))
```

* `groupby("Product")` → Aggregate data by product.
* `sum()` → Total quantity sold per product.
* `sort_index()` → Sort product names.
* `head(1)` → Top 1 product.

```python
print("Region-wise sales :", df.groupby("Region")["Price"].sum().sort_values(ascending=False).head(1))
```

* Group by `Region`.
* Sum `Price`.
* Sort descending → Highest sales region.

---

## 4️⃣ Visualization

```python
sns.barplot(x="Product", y="Price", data=df, estimator=sum, palette="Set2")
plt.title("product-wise sales")
plt.show()
```

* `barplot()` → Bar chart.
* `x, y` → Columns to plot.
* `estimator=sum` → Sum values per category.
* `palette` → Color scheme.
* `plt.show()` → Display plot.

```python
sns.barplot(x="Region", y="Price", data=df, estimator=sum, palette="Set1")
plt.title("Region-wise sales")
plt.show()
```

* Same as above but for Region.

```python
sns.heatmap(df.corr(numeric_only=True), annot=True, cmap="coolwarm")
plt.show()
```

* `corr()` → Correlation between numeric columns.
* `heatmap()` → Color map of correlation.
* `annot=True` → Show values on cells.
* `cmap` → Color style.

---

## 5️⃣ Practice Task 🚀

```python
df["revenue"] = df["Quantity"]*df["Price"]
print("Total Revenue :", df["revenue"].sum())
```

* Create new column `revenue`.
* Calculate total revenue.

```python
print("Top sales product :", df.groupby("Product")["revenue"].sum().sort_values(ascending=False).head(1))
```

* Group by product → sum revenue → highest revenue product.

```python
sns.barplot(x="revenue", y="Product", data=df, palette="Set2", estimator=sum)
plt.title("product vs revenue")
plt.show()
```

* Horizontal bar chart → Product vs Revenue.

```python
region_sales = df.groupby("Region")["revenue"].sum()
plt.figure(figsize=(6,6))
plt.pie(region_sales, labels=region_sales.index, autopct="%1.1f%%", startangle=90)
plt.title("Region-wise sales percentages")
plt.show()
```

* `groupby` → Sum revenue per region.
* `plt.pie()` → Pie chart.
* `autopct` → Show % values.
* `startangle` → Rotate start of pie.
* `figsize` → Size of plot.

---

## 6️⃣ Summary

* **DataFrame Creation** → Easily convert dictionary to table.
* **Data Cleaning** → Handle missing values, remove duplicates, fix formatting.
* **EDA** → Calculate total revenue, find top products & regions.
* **Visualization** → Bar plots for comparison, heatmaps for correlation, pie chart for percentages.
* **Practice** → Calculated revenue column and visualized product vs revenue & region-wise distribution.
* **Key Functions to Remember**: `groupby()`, `sum()`, `fillna()`, `str.strip()`, `barplot()`, `heatmap()`, `pie()`.
