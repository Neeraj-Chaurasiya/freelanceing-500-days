import pandas as pd

data = [1, 2, 3, 4, 5, 6]
print(pd.Series(data))

# ----------------Custom indexing-------------------------
s = pd.Series([1,2,3],index = ["a","b","c"])
print(s)

# -----------------------DataFrame(2D data)-----------------------

data1 = {
  "Name":["Neeraj","Aman","Ravi"],
  "Age":[21,25,23],
  "Marks":[85,90,88]
}

df = pd.DataFrame(data1)
print(df)

# ------------------------Basic DataFrame Info------------------------

print(df.head())
print(df.tail())
print(df.shape)
print(df.info())
print(df.describe())

# ------------------------------small practice task------------------------------

data_std = {
  "Name":["Neeraj","Aman","Ravi","Ashita","Daksha"],
  "Age":[19,18,15,19,25],
  "Marks":[75,90,75,80,78],
  "City":["Vasai","Nalasopara","Vasai","Dahisar","Malad"]
}

df_std = pd.DataFrame(data_std)
print(df_std)
print(df_std.head(3))
print(df_std.shape)
print(df_std.info())
print(df_std.describe())