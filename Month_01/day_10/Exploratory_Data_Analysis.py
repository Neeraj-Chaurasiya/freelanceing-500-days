# ------------------------ Seaborn Import & Basic Setup -------------------------------


import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("https://raw.githubusercontent.com/mwaskom/seaborn-data/master/tips.csv")
print(df.haead())

# --------------------------------- Distribution Plots ----------------------------------


sns.histplot(df["total_bill"], bins= 20 , kde= True, )
plt.title("Distribution of totle bill")
plt.show()

sns.boxplot(x=df["day"], y= df["total_bill"])
plt.title("boxplot: bill per day")
plt.show()

# ----------------------------------- Categorical Plots ----------------------------------------

sns.barplot(x="day",y="total_bill", data=df)
plt.title("average bill by day")
plt.show()

sns.countplot(x= "sex", data=df)
plt.title("gender count")
plt.show()

# --------------------------------- Relationship Plots -----------------------------------

sns.scatterplot(x="total_bill", y="tip",hue = "sex",data=df )
plt.title("bill vs tip (gender-wise)")
plt.show()

sns.lineplot(x="size",y="total_bill",data=df)
plt.title("bill by group size ")
plt.show()

# ---------------------------------- Heatmap (Correlation Matrix) ---------------------------

corr = df.corr(numeric_only = True)
sns.heatmap(corr , annot=True , cmap="coolwarm")
plt.title("correlation Heatmat ")
plt.show()

# --------------------------------- Practice Task 🚀 -----------------------------------

sns.barplot(x="sex", y="tip",data=df)
plt.title("Male vs Female average tip ")
plt.show()

sns.boxplot(x="day",y="total_bill",data=df)
plt.title("bill per day")
plt.show()

corr = df.corr( numeric_only=True)
sns.heatmap(corr, annot=True, cmap="coolwarm")
plt.title("correlation heatmap ")
plt.show()