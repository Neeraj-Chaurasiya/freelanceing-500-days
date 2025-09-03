# ------------------------------ Dataset Load & Basic Info ------------------------------

import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("https://raw.githubusercontent.com/mwaskom/seaborn-data/master/tips.csv")
print(df.head())     
print(df.info())     
print(df.describe())   

# ----------------------------- Univariate Analysis (Single Column) -------------------------------------

print(df["total_bill"].mean())
print(df["sex"].unique())
print(df["day"].value_counts())

# ---------------------------- Bivariate Analysis (Relation between 2 columns) ----------------------------

print(df.groupby("day")["total_bill"].mean())
print(df.groupby("sex")["tip"].mean())

# ---------------------------- Matplotlib Basic Plots --------------------------------

fig, axes = plt.subplots(1, 3, figsize=(18, 5)) 
df["total_bill"].plot(kind="hist", bins = 10 , title="Total bill distribution",ax=axes[0])
df.groupby("day")["total_bill"].mean().plot(kind="bar", title="Average bill per day",ax=axes[1])
df.plot(kind="scatter",x="total_bill",y="tip", title="bill vs tip",ax=axes[2])
plt.tight_layout() 
plt.show()

# ------------------------------ Practice Task 🚀 ----------------------------------

print(df.groupby("day")["tip"].max().sort_values(ascending=False).head(1))
avr_bill = df.groupby("sex")["total_bill"].mean()
print("Average  bill : ",avr_bill)
print("Average bill different: ", avr_bill["Male"]-avr_bill["Female"])

df.plot(kind= "scatter" , x="size" , y="total_bill", title="size vs total_bill")
plt.show()