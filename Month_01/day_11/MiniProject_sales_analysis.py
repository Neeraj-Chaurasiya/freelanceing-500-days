# ----------------------------------- Dataset Load ----------------------------------

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

data = {
    "OrderID":[1,2,3,4,5,6,7,8,9,10],
    "Product":[" Laptop","Phone","Laptop","Tablet","Phone ","Laptop","Tablet","Phone","Laptop","Tablet"],
    "Category":["Electronics","Electronics","Electronics","Electronics","Electronics","Electronics","Electronics",None,"Electronics","Electronics"],
    "Quantity":[1,2,1,3,2,1,3,2,None,1],
    "Price":[60000,20000,65000,15000,22000,70000,15000,20000,65000,15000],
    "Region":["North"," South","East","West","North","South","East","West","North"," East"]
}

df = pd.DataFrame(data)
print(df.head())

# ----------------------------------- Data Cleaning ----------------------------------

print(df.isnull().sum())
duplicate = df.duplicated().sum()
print("Total Dublicates : ",duplicate)
df["Quantity"] = df["Quantity"].fillna(0)
df["Category"] = df["Category"].fillna("Electronics")
df["Product"] = df["Product"].str.strip()
df["Region"] = df["Region"].str.strip()
print(df)

# ----------------------------------- Basic EDA ----------------------------------

print("Total Revenue: \n",(df["Quantity"]*df["Price"]).sum())
print("Top sales products : \n ",df.groupby("Product")["Quantity"].sum().sort_index(ascending=False).head(1))
print("Region-wise sales :\n",df.groupby("Region")["Price"].sum().sort_values(ascending=False).head(1))

# -------------------------------- Visualization (Matplotlib / Seaborn) -----------------------------

sns.barplot(x="Product", y="Price", data = df, estimator=sum , palette= "Set2")
plt.title("product-wise sales ")
plt.show()

sns.barplot(x="Region",y="Price",data=df,estimator=sum , palette= "Set1")
plt.title("Region-wise sales")
plt.show()

sns.heatmap(df.corr(numeric_only=True), annot=True, cmap="coolwarm")
plt.show()

# ------------------------------------- Practice Task 🚀 ---------------------------------

df["revenue"] = df["Quantity"]*df["Price"]
print("Total Revenue : ",df["revenue"].sum())
print("Top sales product :",df.groupby("Product")["revenue"].sum().sort_values(ascending=False).head(1))

sns.barplot(x="revenue", y="Product",data = df , palette="Set2", estimator=sum)
plt.title("product vs revenue ")
plt.show()

region_sales = df.groupby("Region")["revenue"].sum()
plt.figure(figsize=(6,6))
plt.pie(region_sales, labels=region_sales.index, autopct="%1.1f%%", startangle=90)
plt.title("Region-wise sales persentages ")
plt.show()