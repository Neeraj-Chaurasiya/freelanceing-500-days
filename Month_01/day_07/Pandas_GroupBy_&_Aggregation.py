# ----------------------------- Basic GroupBy ----------------------------------------
import pandas as pd

data = {
    "Department": ["IT", "IT", "HR", "HR", "Finance", "Finance"],
    "Employe": ["Aman", "Ravi", "Priya", "Ashita", "Neeraj", "Dhiraj"],
    "Salary": [50000, 60000, 45000, 55000, 70000, 80000],
}

df = pd.DataFrame(data)
print(df)

print(df.groupby("Department")["Salary"].mean())

# ----------------------------------- Multiple Aggregations ----------------------------------

print(df.groupby("Department")["Salary"].agg(["mean", "max", "min", "sum"]))

# ------------------------------------- GroupBy on Multiple Columns ----------------------------

std = {
    "Class": ["10A", "10A", "10B", "10B", "10A", "10B"],
    "Subject": ["Maths", "Science", "Maths", "Science", "Maths", "Science"],
    "Marks": [85, 90, 78, 88, 92, 81],
}

df1 = pd.DataFrame(std)
print(df1)

print(df1.groupby(["Class", "Subject"])["Marks"].mean())

# ------------------------------------- Sorting Values & Groups ---------------------------------

print(df1.groupby("Class")["Marks"].mean().sort_values(ascending=False))

# ----------------------------------- Small Practice Task --------------------------------

sales = {
    "Region": ["Vasai", "Virar", "Vasai", "Mira Road", "Virar", "Mira Road"],
    "Product": ["Laptop", "Mobile", "Earphone", "Earphone", "Laptop", "Mobile"],
    "Sales": [20000, 50000, 40000, 35000, 30000, 55000],
}

df_sal = pd.DataFrame(sales)
print(df_sal)

print(df_sal.groupby("Region")["Sales"].sum())
print(df_sal.groupby("Product")["Sales"].mean())
print(df_sal.groupby("Product")["Sales"].mean().sort_values(ascending=False))
