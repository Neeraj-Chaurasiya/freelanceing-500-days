# Import Libraries & Load Data

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset
df = pd.read_csv(r"C:\Freelanceing (500 days)\Month_02\day_38/data/region_category_sales.csv")
print(df.head())

# Add a Professional Style

sns.set_style("whitegrid")
plt.rcParams["figure.facecolor"] = "white"
plt.rcParams["axes.edgecolor"] = "#333333"
plt.rcParams["axes.labelcolor"] = "#333333"
plt.rcParams["axes.titlesize"] = 14

# Total Sales by Category
plt.figure(figsize=(10,6))
sns.barplot(x="category", y="total_sales", data=df, hue="region")
plt.title("Total Sales by Category & Region", fontsize=14, fontweight="bold")
plt.xlabel("Product Category", fontsize=12)
plt.ylabel("Total Sales (₹)", fontsize=12)
plt.xticks(rotation=45, ha="right")
plt.legend(title="Region")
plt.tight_layout(pad=2.0)
plt.savefig(r"c:/Freelanceing (500 days)/Month_02/day_38/visuals/total_sales_by_category.png")
plt.show()

# Average Sales by Region (Horizontal Bar)

plt.figure(figsize=(8,5))
sns.barplot(x="avg_sales", y="region", data=df, ci=None, palette="crest")
plt.title("Average Sales by regions :")
plt.xlabel("Average sale ")
plt.ylabel("Region")
plt.tight_layout()
plt.savefig(r"c:/Freelanceing (500 days)/Month_02/day_38/visuals/avg_sales_by_region.png")
plt.show()

# Quantity Comparison (Line Plot)

plt.figure(figsize=(8,5))
sns.lineplot(x="category", y="total_qty", hue="region", data=df, marker="o",markersize=10 ,linewidth=2) 
plt.title("Quantity Comparison ")
plt.xlabel("Category")
plt.ylabel("Quantity")
plt.tight_layout()
plt.savefig(r"c:/Freelanceing (500 days)/Month_02/day_38/visuals/quantity_comparison.png")
plt.show()

# Correlation Heatmap

plt.figure(figsize=(6,4))
corr = df[["total_sales","avg_sales","max_sales","total_qty"]].corr()
sns.heatmap(corr, annot = True , cmap="coolwarm" , fmt = ".2f")
plt.title("Correlation between sales metrics")
plt.tight_layout()
plt.savefig(r"c:/Freelanceing (500 days)/Month_02/day_38/visuals/region_category_heatmap.png")
plt.show()

