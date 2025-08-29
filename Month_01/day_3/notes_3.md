📘 Notes: Pandas Basics (Day-3)

🔹 Series (1D Data)

import pandas as pd

data = [1, 2, 3, 4, 5, 6]

print(pd.Series(data))

👉 pd.Series ek 1D labeled array hota hai.

👉 Default indexing (0 se n-1) hoti hai.

🔹 Custom Indexing

s = pd.Series([1,2,3], index=["a","b","c"])

print(s)

👉 Hum apna custom index de sakte hain (a, b, c).

🔹 DataFrame (2D Data)

data1 = {
  "Name":["Neeraj","Aman","Ravi"],
  "Age":[21,25,23],
  "Marks":[85,90,88]
}

df = pd.DataFrame(data1)

print(df)

👉 pd.DataFrame ek 2D tabular data structure hai (rows × columns).

🔹 Basic DataFrame Info

print(df.head())      # first 5 rows

print(df.tail())      # last 5 rows

print(df.shape)       # (rows, cols)

print(df.info())      # summary (dtypes, non-null values)

print(df.describe())  # stats for numeric columns

👉 head() & tail() → quick preview.

👉 shape → dataset size.

👉 info() → datatype + null check.

👉 describe() → statistics (mean, std, min, max, etc.).

🔹 Small Practice Task 🚀

data_std = {
  "Name":["Neeraj","Aman","Ravi","Ashita","Daksha"],
  "Age":[19,18,15,19,25],
  "Marks":[75,90,75,80,78],
  "City":["Vasai","Nalasopara","Vasai","Dahisar","Malad"]
}

df_std = pd.DataFrame(data_std)

print(df_std)          # full DataFrame

print(df_std.head(3))  # first 3 rows

print(df_std.shape)    # (5,4)

print(df_std.info())   # structure & datatypes

print(df_std.describe())  # stats of numeric columns

👉 Realistic dataset banaya with Name, Age, Marks, City.

👉 head(3) → first 3 rows.

👉 describe() → min, max, mean, std etc.

✅ Summary

Series = 1D data with indexing.

DataFrame = 2D tabular data (rows × cols).

head(), tail(), shape, info(), describe() → quick data analysis ke liye best functions.