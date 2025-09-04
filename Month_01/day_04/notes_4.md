📘 Notes: Pandas – Indexing, Selection & Filtering (Day-4)

🔹 Column Selection

import pandas as pd  

data = {
  "Name":["Neeraj","Ravi","Dhiraj","Ashita","Aman"],
  "Age":[19,15,17,19,20],
  "Marks":[75,88,92,80,96],
  "City":["vasai","vasai","panval","dahisar","nallasopara"]
}

df = pd.DataFrame(data)  

print(df)                 # Full DataFrame  
print(df["Name"])         # Single column  
print(df[["Name","Marks"]])  # Multiple columns  

👉 Single ya multiple columns ko square brackets [] ke andar likh kar select kar sakte ho.  

🔹 Row Selection with iloc (Index-based)

print(df.iloc[0])      # First row  
print(df.iloc[1:3])    # Row 1 and 2  

👉 iloc → integer-based indexing (0 se start hoti hai).  
👉 iloc[1:3] → row 1 & 2 return karega.  

🔹 Row Selection with loc (Label-based) 

print(df.loc[0])                        # Row with label 0  
print(df.loc[0:2, ["Name","Marks"]])    # Rows 0–2 with specific cols  
print(df.loc[2:5, ["Age","Name"]])      # Rows 2–5 with selected cols  


👉 loc → label-based selection.  
👉 Range me last value bhi include hoti hai.  

🔹 Conditional Filtering

print(df[df["Marks"] > 88])                   # Marks greater than 88  
print(df[df["City"] == "vasai"])              # City = vasai  
print(df[(df["Age"] > 18) | (df["Marks"] >= 80)])  # OR condition  


👉 Conditions use karke specific rows filter kar sakte ho.  
👉 & = AND, | = OR.  

🔹 Adding & Dropping Columns
df["Grade"] = ['A','B','A','C','A+']   # Add new column  
df = df.drop("City", axis=1)           # Drop City column  


👉 axis=1 → column drop.  
👉 axis=0 → row drop.  

🔹 Small Practice Task 🚀

emp = {
  "EmpID":[123,465,789,357,159],
  "Name":["Neeraj","Ashita","Dhiraj","Dhirandra","Manish"],
  "Age":[19,19,18,20,21],
  "Department":["HR","Sales","Finance","Management","Software"],
  "Salary":[35000,45000,25000,21000,22000]
}

employ = pd.DataFrame(emp)

print(employ[["Name","Salary"]])         # Select name & salary  
print(employ[employ["Salary"] > 25000])  # Filter employees > 25k  
employ["Bonus"] = [3500,4500,2500,2100,2200]  # Add Bonus column  
employ = employ.drop("Department", axis=1)    # Drop Department  


👉 Columns ko select/filter/add/drop karna seekh liya.

✅ Summary

iloc → integer-based row selection.  
loc → label-based row/column selection.  
Filtering → conditional operators (>, <, ==, |, &).  
Add/Drop columns → assign new column or use drop().