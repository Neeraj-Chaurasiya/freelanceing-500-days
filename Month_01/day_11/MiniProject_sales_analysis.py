# ------------------------ Mini Project: Sales Analysis ------------------------

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

# ------------------------ Folder Setup ------------------------
if not os.path.exists("images"):
    os.makedirs("images")

# ------------------------ Dataset Load ------------------------
data = {
    "OrderID":[1,2,3,4,5,6,7,8,9,10],
    "Product":["Laptop","Phone","Laptop","Tablet","Phone","Laptop","Tablet","Phone","Laptop","Tablet"],
    "Category":["Electronics","Electronics","Electronics","Electronics","Electronics","Electronics","Electronics",None,"Electronics","Electronics"],
    "Quantity":[1,2,1,3,2,1,3,2,None,1],
    "Price":[60000,20000,65000,15000,22000,70000,15000,20000,65000,15000],
    "Region":["North","South","East","West","North","South","East","West","North","East"]
}

df = pd.DataFrame(data)

# ------------------------ Data Cleaning ------------------------
df["Quantity"] = df["Quantity"].fillna(0)
df["Category"] = df["Category"].fillna("Electronics")
df["Product"] = df["Product"].str.strip()
df["Region"] = df["Region"].str.strip()

# ------------------------ Basic EDA ------------------------
df["revenue"] = df["Quantity"]*df["Price"]
total_revenue = df["revenue"].sum()
print("Total Revenue:", total_revenue)
print("Top sales product:", df.groupby("Product")["revenue"].sum().sort_values(ascending=False).head(1))
print("Region-wise sales:", df.groupby("Region")["revenue"].sum().sort_values(ascending=False).head(1))

# ------------------------ Visualization ------------------------

# 1️⃣ Product-wise Sales
plt.figure(figsize=(6,4))
sns.barplot(x="Product", y="Price", data=df, estimator=sum, palette="Set2")
plt.title("Product-wise Sales")
plt.savefig("images/chart_product_sales.png")
plt.close()

# 2️⃣ Region-wise Sales
plt.figure(figsize=(6,4))
sns.barplot(x="Region", y="Price", data=df, estimator=sum, palette="Set1")
plt.title("Region-wise Sales")
plt.savefig("images/chart_region_sales.png")
plt.close()

# 3️⃣ Correlation Heatmap
plt.figure(figsize=(6,4))
sns.heatmap(df.corr(numeric_only=True), annot=True, cmap="coolwarm")
plt.title("Correlation Heatmap")
plt.savefig("images/chart_correlation.png")
plt.close()

# 4️⃣ Product vs Revenue
plt.figure(figsize=(6,4))
sns.barplot(x="revenue", y="Product", data=df, estimator=sum, palette="Set2")
plt.title("Product vs Revenue")
plt.savefig("images/chart_product_revenue.png")
plt.close()

# 5️⃣ Region-wise Revenue Pie Chart
region_sales = df.groupby("Region")["revenue"].sum()
plt.figure(figsize=(6,6))
plt.pie(region_sales, labels=region_sales.index, autopct="%1.1f%%", startangle=90)
plt.title("Region-wise Sales Percentages")
plt.savefig("images/chart_region_pie.png")
plt.close()

print("✅ All charts saved in 'images/' folder!")
