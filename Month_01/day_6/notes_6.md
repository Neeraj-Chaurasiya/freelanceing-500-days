📘 Notes: Pandas – Merge, Join & Concatenation (Day-6)

🔹 Concatenation Basics  

import pandas as pd

data1 = {
  "ID":[1,2,3],
  "Name":["Aman","Ravi","Priya"]
}

data2 = {
  "ID":[4,5,6],
  "Name":["Ashita","Neeraj","Dhiraj"]
}

df1 = pd.DataFrame(data1)  
df2 = pd.DataFrame(data2)  

print(pd.concat([df1,df2]))  

👉 pd.concat([df1,df2]) → Dono DataFrames ko row-wise stack karta hai.  
👉 Default = axis=0 (rows). Column-wise concatenate karne ke liye axis=1 use kar sakte ho.  

🔹 Merge (SQL JOIN jaisa)  

data_emp = {
  "EmpId":[1,2,3,4],
  "Name":["Aman","Ravi","Priya","Ashita"]
}

data_salary = {
  "EmpId":[1,2,3,5],
  "Salary":[40000,50000,60000,70000]
}

df_emp = pd.DataFrame(data_emp)  
df_salary = pd.DataFrame(data_salary)  

print(pd.merge(df_emp, df_salary, on="EmpId", how="inner"))  

👉 merge() SQL ke JOIN ki tarah kaam karta hai.  
👉 on="EmpId" → kis column par join karna hai.  
👉 how="inner" → sirf matching rows dikhengi.  

🔹 Different Types of Joins  

print(pd.merge(df_emp, df_salary, on="EmpId", how="left"))  
print(pd.merge(df_emp, df_salary, on="EmpId", how="right"))  
print(pd.merge(df_emp, df_salary, on="EmpId", how="outer"))  

inner → sirf common records.  

left → left table ke sab records + right ke matching.  
right → right table ke sab records + left ke matching.  
outer → dono tables ke sab records (NaN where missing).  

🔹 Join using Index

df1 = pd.DataFrame({"A":[1,2,3]}, index=["a","b","c"])  
df2 = pd.DataFrame({"B":[4,5,6]}, index=["a","b","d"])  

print(df1.join(df2, how="outer"))  

👉 join() → index ke basis par tables combine karta hai.  
👉 how="outer" → dono indexes ka union (sab rows included).  

🔹 Small Practice Task 🚀

std = {
  "Rollno":[1,2,3,4],
  "Name":["Depash","Daksha","Arjun","Karan"],
  "Class":[10,11,12,9]
}

marks = {
  "Rollno":[1,2,3,5],
  "Subject":["Maths","Science","History","Civis"],
  "Marks":[75,80,95,85]
}

df_std = pd.DataFrame(std)  
df_mar = pd.DataFrame(marks)  

final = pd.merge(df_std, df_mar, on="Rollno")  
final = final[["Name","Subject","Marks"]]  
print(final)  

print(pd.concat([df_std, df_mar]))  

👉 merge() se student data aur marks combine kiya.  
👉 Column filter karke sirf Name, Subject, Marks rakha.  
👉 concat() se dono DataFrames ko ek sath joda.  

✅ Summary

concat() → DataFrames ko row-wise ya column-wise stack karna.  
merge() → SQL joins jaisa powerful operation (inner, left, right, outer).  
join() → index ke basis par join karna.