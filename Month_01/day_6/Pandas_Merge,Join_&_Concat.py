# ----------------------------------- concatenation Basics ---------------------------------

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

# --------------------------------- Merge (SQL JOIN jaisa) ---------------------------------

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

print(pd.merge(df_emp,df_salary, on = "EmpId", how="inner"))


# --------------------------------- Different Types of Joins --------------------------

print(pd.merge(df_emp,df_salary, on = "EmpId", how="left"))
print(pd.merge(df_emp,df_salary, on = "EmpId", how = "right"))
print(pd.merge(df_emp,df_salary, on = "EmpId", how="outer"))

# --------------------------------- Join using Index ----------------------------------

df1 = pd.DataFrame({"A":[1,2,3]}, index=["a","b","c"])
df2 = pd.DataFrame({"B":[4,5,6]}, index=["a","b","d"])
print(df1.join(df2, how = "outer"))

# -------------------------------- Small Practice Task ---------------------------------

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

final = pd.merge(df_std,df_mar,on="Rollno")
final = final[["Name","Subject","Marks"]]
print(final)

print(pd.concat([df_std,df_mar]))