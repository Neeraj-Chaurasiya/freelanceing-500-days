📘 Notes: Exploratory Data Analysis (EDA) – Pandas + Matplotlib (Day-9)

---

🔹 Dataset Load & Basic Info

```python
import pandas as pd  
import matplotlib.pyplot as plt  

df = pd.read_csv("https://raw.githubusercontent.com/mwaskom/seaborn-data/master/tips.csv")  
print(df.head())     # First 5 rows  
print(df.info())     # Columns + DataTypes + Null info   
print(df.describe()) # Statistical summary  

👉 head() → Starting rows dekhta hai.  
👉 info() → Dataset ka structure.  
👉 describe() → Mean, median, std deviation etc.  

🔹 Univariate Analysis (Single Column)  
 
print(df["total_bill"].mean())   # Average bill  
print(df["sex"].unique())        # Unique values in 'sex'  
print(df["day"].value_counts())  # Count of each day  

👉 Univariate = Sirf ek hi column ka analysis.  
👉 .mean(), .unique(), .value_counts() use hote hain.  

🔹 Bivariate Analysis (Relation between 2 Columns)  

print(df.groupby("day")["total_bill"].mean())  # Day-wise avg bill  
print(df.groupby("sex")["tip"].mean())         # Gender-wise avg tip  

👉 Bivariate = Do columns ka relation.  
👉 groupby() + aggregation functions (mean, sum, etc.).  

🔹 Matplotlib Basic Plots  

fig, axes = plt.subplots(1, 3, figsize=(18, 5))   #ek row me 2 plots banayega.    

df["total_bill"].plot(kind="hist", bins=10, title="Total bill distribution", ax=axes[0])  
df.groupby("day")["total_bill"].mean().plot(kind="bar", title="Average bill per day", ax=axes[1])   
df.plot(kind="scatter", x="total_bill", y="tip", title="bill vs tip", ax=axes[2])  

plt.tight_layout()  #dono graphs ke beech spacing adjust karega.  
plt.show()  

👉 Histogram → Distribution samajhne ke liye.  
👉 Bar Chart → Group-wise comparison.  
👉 Scatter Plot → Relationship check.  

🔹 Small Practice Task 🚀  

# Highest tip per day  
print(df.groupby("day")["tip"].max().sort_values(ascending=False).head(1))  

# Average bill difference in gender  
avr_bill = df.groupby("sex")["total_bill"].mean()  
print("Average bill : ", avr_bill)  
print("Average bill difference: ", avr_bill["Male"] - avr_bill["Female"])  

# Scatter Plot: Group size vs Bill  
df.plot(kind="scatter", x="size", y="total_bill", title="Size vs Total Bill")  
plt.show()  

👉 Day-wise max tip nikala.  
👉 Male vs Female ke beech average bill difference calculate kiya.  
👉 Scatter plot banaya size vs total_bill.  

✅ Summary  

head(), info(), describe() → Dataset overview.  
Univariate analysis → .mean(), .unique(), .value_counts().  
Bivariate analysis → groupby() + aggregation.  
Plots → Histogram, Bar, Scatter for data visualization.  
Practice task se: Highest tip, gender-wise avg bill, group size relation samjha.