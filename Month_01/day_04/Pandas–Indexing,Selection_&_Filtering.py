#--------------------- Column Selection --------------------------------------
import pandas as pd

data = {
  "Name":["Neeraj","Ravi","Dhiraj","Ashita","Aman"],
  "Age":[19,15,17,19,20],
  "Marks":[75,88,92,80,96],
  "City":["vasai","vasai","panval","dahisar","nallasopara"]
}

df = pd.DataFrame(data)
print(df)
print(df["Name"])
print(df[["Name","Marks"]])

# ------------------- Row selection with iloc (index based) ----------------------------

print(df.iloc[0])
print(df.iloc[1:3])

# ---------------------- Row selection with loc(label-based) --------------------------------

print(df.loc[0])
print(df.loc[0:2,["Name","Marks"]])
print(df.loc[2:5,["Age","Name"]])

# -------------------------- Conditional Filtering ------------------------------

print(df[df["Marks"] > 88])
print(df[df["City"] == "vasai"])
print(df[(df["Age"] > 18) | (df["Marks"] >= 80)])

# ------------------------- Adding and Droping Columns -----------------------------

df["Grade"] = ['A','B','A','C','A+']
# print(df)
df = df.drop("City", axis=1)
# print(df)

# --------------------------- Small Practice Task ------------------------------------

emp = {
  "EmpID":[123,465,789,357,159],
  "Name":["Neeraj","Ashita","Dhiraj","Dhirandra","Manish"],
  "Age":[19,19,18,20,21],
  "Department":["HR","Sales","Finance","Management","Software"],
  "Salary":[35000,45000,25000,21000,22000]
}

employ = pd.DataFrame(emp)
# print(employ)
print(employ[["Name","Salary"]])
print(employ[employ["Salary"] > 25000])
employ["Bonus"] = [3500,4500,2500,2100,2200]
# print(employ)
employ = employ.drop("Department", axis = 1)
# print(employ)