📘 Notes: Pandas – GroupBy & Aggregations (Day-7)

🔹 Basic GroupBy

import pandas as pd

data = {
    "Department": ["IT", "IT", "HR", "HR", "Finance", "Finance"],
    "Employe": ["Aman", "Ravi", "Priya", "Ashita", "Neeraj", "Dhiraj"],
    "Salary": [50000, 60000, 45000, 55000, 70000, 80000],
}

df = pd.DataFrame(data)  
print(df)  

print(df.groupby("Department")["Salary"].mean())  

👉 groupby("Department") → data ko department ke hisaab se group karega.  
👉 .mean() → har department ki average salary nikal lega.  

🔹 Multiple Aggregations  

print(df.groupby("Department")["Salary"].agg(["mean", "max", "min", "sum"]))  

👉 agg() ek sath multiple functions apply karta hai.  
👉 Yaha per mean, max, min, sum sab nikal rahe hain har department ke liye.  

🔹 GroupBy on Multiple Columns

std = {
    "Class": ["10A", "10A", "10B", "10B", "10A", "10B"],
    "Subject": ["Maths", "Science", "Maths", "Science", "Maths", "Science"],
    "Marks": [85, 90, 78, 88, 92, 81],
}

df1 = pd.DataFrame(std)  
print(df1)  

print(df1.groupby(["Class", "Subject"])["Marks"].mean())  

👉 groupby(["Class","Subject"]) → ek se zyada columns par grouping possible hai.  
👉 Yaha har Class + Subject ke liye average marks nikle.  

🔹 Sorting Values & Groups  

print(df1.groupby("Class")["Marks"].mean().sort_values(ascending=False))  

👉 Group karke jo result aaya usse sort bhi kar sakte ho.  
👉 ascending=False → descending order (highest first).  

🔹 Small Practice Task 🚀

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

👉 Region-wise total sales nikale (sum()).  
👉 Product-wise average sales nikale (mean()).  
👉 Fir product ko sales ke hisaab se sort bhi kiya.  

✅ Summary  

groupby() → data ko group karke aggregation karna.  
.mean(), .sum(), .max(), .min() → group ke andar calculation karna.  
agg() → ek sath multiple functions apply karna.  
Sorting → group ke results ko ascending/descending arrange karna.