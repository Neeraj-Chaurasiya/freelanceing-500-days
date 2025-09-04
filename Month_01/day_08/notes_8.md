📘 Notes: Pandas – Data Cleaning & Preprocessing (Day-8)

🔹 Missing Values Handle

import pandas as pd  
import numpy as np  

data = {
  "Name":["Aman","Ravi","Priya","Neeraj"],
  "Age":[23,np.nan,22,25],
  "City":["Delhi","Mumbai",np.nan,"Pune"]
}

df = pd.DataFrame(data)  
print(df)  

print(df.isnull())          # Missing values check  
print(df.dropna())          # NaN row hata do  
print(df.fillna("Unknown")) # NaN ko replace karo 

👉 isnull() → NaN check karta hai.  
👉 dropna() → NaN wali row hata deta hai.  
👉 fillna() → NaN ko custom value se replace karta hai.  

🔹 Duplicates Remove

data_1 = {
  "ID":[1,2,2,3,4,4,5],
  "Name":["A","B","B","C","D","D","E"]
}

df1 = pd.DataFrame(data_1)  
print(df1)  

print(df1.duplicated())      # Duplicate check  
print(df1.drop_duplicates()) # Duplicate remove 

👉 duplicated() → True/False return karta hai duplicate rows ke liye.  
👉 drop_duplicates() → Duplicate rows hata deta hai.  

🔹 Rename Columns + Replace Values

df1 = df1.rename(columns={"Name":"FullName"})         # Column rename  
df1["FullName"] = df1["FullName"].replace("A","Aman") # Value replace  
print(df1)   
 
👉 rename() → Columns ka naam change karne ke liye.  
👉 replace() → Specific values ko update karne ke liye.  
 
🔹 String Operations  

data2 = {
  "Name":["aman","RAVI","priya"],
  "City":["delhi","MUMBAI","pune"]
}
 
df2 = pd.DataFrame(data2)  
print(df2)  

df2["Name"] = df2["Name"].str.strip().str.title()  
df2["City"] = df2["City"].str.strip().str.upper()  
print(df2)  

👉 str.strip() → Extra spaces remove karta hai.  
👉 str.title() → Har word ka first letter capital.  
👉 str.upper() → String ko uppercase me convert karta hai.  

🔹 Small Practice Task 🚀  

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

👉 Pehle extra spaces hataye.  
👉 Duplicate rows remove kiye.  
👉 NaN values ko "Unknown" se fill kiya.  
 
✅ Summary  

isnull(), dropna(), fillna() → Missing values handle karna.  
duplicated(), drop_duplicates() → Duplicate rows manage karna.  
rename(), replace() → Columns aur values modify karna.  
String functions (strip, title, upper) → Text ko clean karna.   
Complete pipeline → Raw → Clean dataset 🚀  

