📘 Notes: Exploratory Data Analysis (EDA) – Seaborn Visualization (Day-10)

---

🔹 Seaborn Import & Basic Setup 

```python  
import seaborn as sns  
import pandas as pd  
import matplotlib.pyplot as plt  

df = pd.read_csv("https://raw.githubusercontent.com/mwaskom/seaborn-data/master/tips.csv")  
print(df.head())   # Dataset ke first 5 rows dekhne ke liye  

👉 seaborn → Advanced visualization library (matplotlib ke upar built).  
👉 tips dataset → Restaurant bills + tips ka sample data.  

🔹 Distribution Plots  

sns.histplot(df["total_bill"], bins=20, kde=True)   # Histogram + KDE  
plt.title("Distribution of total bill")  
plt.show()  

sns.boxplot(x=df["day"], y=df["total_bill"])        # Boxplot day-wise bill distribution  
plt.title("Boxplot: Bill per day")  
plt.show()  
 
👉 Histogram → Data distribution + density (kde=True).  
👉 Boxplot → Outliers aur spread samajhne ke liye.  

🔹 Categorical Plots  

sns.barplot(x="day", y="total_bill", data=df)   # Average bill per day  
plt.title("Average bill by day")  
plt.show()  

sns.countplot(x="sex", data=df)                 # Count of gender  
plt.title("Gender count")  
plt.show()  

👉 Barplot → Mean values show karta hai.  
👉 Countplot → Frequency of categories.  

🔹 Relationship Plots  

sns.scatterplot(x="total_bill", y="tip", hue="sex", data=df)   # Scatter with gender color  
plt.title("Bill vs Tip (gender-wise)")  
plt.show()  

sns.lineplot(x="size", y="total_bill", data=df)                # Lineplot of group size vs bill  
plt.title("Bill by group size")  
plt.show()  

👉 Scatterplot → 2 numerical variables ke relation.  
👉 hue="sex" → Male/Female alag color me.  
👉 Lineplot → Trend analysis.  

🔹 Heatmap (Correlation Matrix)  

corr = df.corr(numeric_only=True)              # Numeric columns correlation  
sns.heatmap(corr, annot=True, cmap="coolwarm") # Annot=True → values display  
plt.title("Correlation Heatmap")   
plt.show()  

👉 Correlation → Columns ke beech relation (-1 to +1).  
👉 Heatmap → Color-coded visualization.  

🔹 Small Practice Task 🚀  

# Male vs Female average tip  
sns.barplot(x="sex", y="tip", data=df)  
plt.title("Male vs Female average tip")  
plt.show()  

# Day-wise bill distribution
sns.boxplot(x="day", y="total_bill", data=df)  
plt.title("Bill per day")  
plt.show()  

# Correlation heatmap
  
corr = df.corr(numeric_only=True)  
sns.heatmap(corr, annot=True, cmap="coolwarm")  
plt.title("Correlation Heatmap")  
plt.show()  

👉 Gender-wise avg tips ka comparison.  
👉 Day-wise bill spread check kiya.  
👉 Correlation heatmap se highest related features samjhe.  

✅ Summary  

Distribution → histplot, boxplot.  
Categorical → barplot, countplot.  
Relationship → scatterplot, lineplot  
Heatmap → Correlation ke liye.  
Practice task → Gender tips, Day-wise bill, Correlation check.