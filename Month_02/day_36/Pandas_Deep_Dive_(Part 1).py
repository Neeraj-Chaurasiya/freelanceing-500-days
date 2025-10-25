#  Import Libraries

import pandas as pd

print("Pandas Version : ", pd.__version__)  # Check Version

# Load Dataset

df = pd.read_csv("c:/Freelanceing (500 days)/Month_02/day_36/data/Sales_data.csv")  #Load csv file

print(df.head()) 

print(df.info())

print("Shape :",df.shape)  # Shape of dataset (rows, columns)

# Basic Cleaning

df.rename(columns={"category":"categroy_name" , "quantity":"total_quantity"}, inplace=True)  # Rename columns

df.dropna(inplace=True)  # Drop missing values

df["price"] = df["price"].astype(int) #Convert  price columns to integer
print(df.info())  


df.to_csv("c:/Freelanceing (500 days)/Month_02/day_36/data/Sales_cleaned_data.csv",index=False)  # Save cleaned data

print(df.describe())