# -------------------------------- GroupBy Basics ------------------------------
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

# -----------------------------------Multiple Aggregations------------------------------------

print(df.groupby("Department")["Salary"].agg(["mean","max","min"]))

# -------------------------------------Pivot Table ----------------------------------------


pivot = df.pivot_table(index = "Department", values = "Salary" , aggfunc = "mean")
print(pivot)

# --------------------------------Small Practice Task-----------------------------------

sales = {
  "Region":["Vasai","Virar","Vasai","Mira Road","Virar","Mira Road"],
  "Product":["Laptop","Mobile","Earphone","Earphone","Laptop","Mobile"],
  "Sales":[20000,50000,40000,35000,30000,55000],
  "Profit":[2000,5000,4000,3500,3000,5500]
}

df = pd.DataFrame(sales)
print(df)
print(df.groupby("Region")["Sales"].sum())
print(df.groupby("Product")["Profit"].mean())
pivot1 = df.pivot_table(index = "Region",values = "Sales", aggfunc="sum")
print(pivot1)