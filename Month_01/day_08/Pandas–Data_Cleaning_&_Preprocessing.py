# --------------------------- Missing Values Handle --------------------------------

import pandas as pd
import numpy as np

data = {
  "Name":["Aman","Ravi","Priya","Neeraj"],
  "Age":[23,np.nan,22,25],
  "City":["Delhi","Mumbai",np.nan,"Pune"]
}

df = pd.DataFrame(data)
print(df)
print(df.isnull())
print(df.dropna())
print(df.fillna("Unknown"))

# ---------------------------- Duplicates Remove --------------------------------

data_1 = {
  "ID":[1,2,2,3,4,4,5],
  "Name":["A","B","B","C","D","D","E"]
}

df1 = pd.DataFrame(data_1)

print(df1)
print(df1.duplicated())
print(df1.drop_duplicates())

# ----------------------------- Rename Columns + Replace Values -------------------------------

df1 = df1.rename(columns={"Name":"FullName"})
df1["FullName"] = df1["FullName"].replace("A","Aman")
print(df1)

# ---------------------------------- String Operations ------------------------------------

data2 = {
  "Name":["aman","RAVI","priya"],
  "City":["delhi","MUMBAI","pune"]
}
df2 = pd.DataFrame(data2)
print(df2)

df2["Name"]=df2["Name"].str.strip().str.title()
df2["City"] = df2["City"].str.strip().str.upper()
print(df2)

# ------------------------------------- Practice Task ------------------------------------

data_task = {
    "Name": ["  aman ", "Ravi", "Priya", "Neeraj", "Ravi"],   # extra spaces + duplicate
    "Age": [23, np.nan, 22, 25, np.nan],                      # NaN values
    "City": [" delhi", "mumbai ", np.nan, "Pune ", "mumbai "] # extra spaces + NaN
}

df4 = pd.DataFrame(data_task)
print(df4)

df4["Name"] = df4["Name"].str.strip().str.title()
df4["City"] = df4["City"].str.strip().str.title()
df4 = df4.drop_duplicates()
df4 = df4.fillna("Unknown")
print("Cleaned data : \n", df4)

