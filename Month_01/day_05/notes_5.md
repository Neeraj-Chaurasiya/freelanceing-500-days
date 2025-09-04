📘 Notes: Pandas – GroupBy, Aggregations & Pivot Tables (Day-5)  

🔹 GroupBy Basics  

import pandas as pd  

data = {
  "Department":["HR","HR","IT","IT","Finance","Finance"],
  "Employee":["Aman","Priya","Ravi","Neeraj","Ashita","Dhiraj"],
  "Salary":[40000,45000,60000,65000,55000,52000],
  "Bonus":[2000,2500,4000,4500,3500,3000]
}

df = pd.DataFrame(data)  
print(df)  

print(df.groupby("Department")["Salary"].mean())  

👉 groupby("Department") → rows ko department ke hisaab se group karega.  
👉 Fir aggregation function (mean, sum, etc.) lagaya ja sakta hai.  

🔹 Multiple Aggregations  

print(df.groupby("Department")["Salary"].agg(["mean","max","min"]))  

👉 agg() ke andar ek se zyada functions apply kar sakte ho.  
👉 Yahan mean, max, min salary har department ke liye calculate hui.  

🔹 Pivot Table  

pivot = df.pivot_table(index = "Department", values = "Salary" , aggfunc = "mean")  
print(pivot)  

👉 pivot_table() bhi groupby() jaisa hi hai, lekin output thoda tabular & flexible hota hai.  
👉 index → kis column par grouping hogi.  
👉 values → kis column ka aggregation karna hai.  
👉 aggfunc → kaunsa function lagana hai (sum, mean, max, etc.).  

🔹 Small Practice Task 🚀  

sales = {
  "Region":["Vasai","Virar","Vasai","Mira Road","Virar","Mira Road"],
  "Product":["Laptop","Mobile","Earphone","Earphone","Laptop","Mobile"],
  "Sales":[20000,50000,40000,35000,30000,55000],
  "Profit":[2000,5000,4000,3500,3000,5500]
}  

df = pd.DataFrame(sales)  
print(df)   

print(df.groupby("Region")["Sales"].sum())     # Total sales per region  
print(df.groupby("Product")["Profit"].mean())  # Avg profit per product  

pivot1 = df.pivot_table(index="Region", values="Sales", aggfunc="sum")  
print(pivot1)   

👉 groupby("Region")["Sales"].sum() → har region ka total sales.  
👉 groupby("Product")["Profit"].mean() → product-wise average profit.  
👉 pivot_table() → data ko summarize karne ka powerful tarika.  

✅ Summary  

groupby() → grouping + aggregation (mean, sum, min, max, etc.).  
agg() → ek sath multiple aggregation apply karne ke liye.  
pivot_table() → table format me summarized data dikhane ke liye.  