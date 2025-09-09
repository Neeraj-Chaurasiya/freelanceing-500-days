# -------------------------------------- Load Scraped Data --------------------------------

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv(r"C:\Freelanceing (500 days)\Month_01\day_13\CSV extracted dataset\books_full.csv")

print(df.head())
print(df.info())

# ----------------------------------------- Data Cleaning ---------------------------------------

df["Price"] = df["Price"].str.replace("Â£","").astype(float)
rating_map = {"One":1,"Two":2,"Three":3,"Four":4,"Five":5}
df["Rating"] = df["Rating"].map(rating_map)
print(df.isnull().sum())
print(df.head())

# ------------------------------------- Basic Analysis -------------------------------------

print("Average book price :", df["Price"].mean())
print("Most expensive books :\n",df.loc[df["Price"].idxmax()])
print("Average rating : ",df["Rating"].mean())

# --------------------------------- Visualization (Matplotlib/Seaborn) --------------------------------

sns.histplot(df["Price"], bins=20 , kde=True)
plt.title("Book price distribution ")
plt.show()

sns.countplot(x="Rating",data = df)
plt.title("Book rating count : ")
plt.show()

# --------------------------------------- 🚀 Practice Task --------------------------------------

print("Top 10 most expensive books : \n",df.groupby("Title")["Price"].max().sort_values(ascending=False).head(10))
print("Average price by rating : ", df.groupby("Rating")["Price"].mean())

sns.barplot(x="Rating",y="Price", data=df)
plt.title("Rating vs Average price : ")
plt.show()

df.to_csv("books_cleaned.csv", index=False)
print("Saved data to books_cleaned.csv")