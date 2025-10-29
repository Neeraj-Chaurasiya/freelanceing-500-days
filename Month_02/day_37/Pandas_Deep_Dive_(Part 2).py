# Import and load data

import pandas as pd 

df = pd.read_csv("c:/Freelanceing (500 days)/Month_02/day_37/data/ecommerce_sales_34500.csv")

print(df.info())
print(df.head(3))

# Filtering Examples

high_sales = df[df["total_amount"] > 1000 ] # Filter sales above ₹1,000
print(high_sales.head()) #Top 5

North_Sales = df[df["region"] == 'North']      # Filter for a specific region 
print("North sales count: ", len(North_Sales))

# Sorting

df_sort = df.sort_values(by='total_amount', ascending=False)  # Sort by TotalAmount (descending)
print(df_sort.head(5))

# GroupBy (SQL → Pandas equivalent)

Region_revenue = df.groupby('region')['total_amount'].sum().reset_index() # region-wise total revenue
print(Region_revenue.head(4))

category_avg = df.groupby('category')['total_amount'].mean().reset_index()   # Category-wise average sales
print(category_avg)

# Multiple Aggregations

report = (
    df.groupby(["region", "category"])
    .agg(
        total_sales=("total_amount", "sum"),
        avg_sales=("total_amount", "mean"),
        max_sales=("total_amount", "max"),
        total_qty=("quantity", "sum")
    )
    .reset_index()
    .sort_values(by="total_sales", ascending=False)
)

print(report.head())  # Group by Region and Category

# Top N Analysis

top_Product = df.groupby("category")["total_amount"].sum().reset_index().sort_values(by="total_amount", ascending=False)
print(top_Product.head(5))  # Top 5 Category by total revenue

# Unique & Counts

print("Unique Regions : ",df["region"].nunique())
print("Unique Categories : ", df["category"].unique())
print(df["category"].value_counts())

# Export Final Report

report.to_csv(r"c:/Freelanceing (500 days)/Month_02/day_37/Outputs/region_category_sales.csv", index=False)
print("Report exported successfully")