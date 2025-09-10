# -------------------------------- Load Cleaned Dataset ---------------------------------

import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

df = pd.read_csv(r"C:\Freelanceing (500 days)\Month_01\day_14\Cleaned data\books_cleaned.csv")
print(df.head())

# ----------------------------------- Summary Metrics -------------------------------------

total_books = df.shape[0]
avg_price = df["Price"].mean()
avg_rating = df["Rating"].mean()

print("Total books : ",total_books)
print("Average price : ",avg_price)
print("Average rating : ",avg_rating)

# ------------------------------------ Visualization (Matplotlib / Seaborn) -----------------------------

sns.histplot(df["Price"], bins=20 , kde= True)
plt.title("Price distribution ")
plt.show()

top10 = df.nlargest(10,"Price")
sns.barplot(x="Price",y="Title", data=top10)
plt.title("top 10 expensive book ")
plt.show()

avg_by_rating = df.groupby("Rating")["Price"].mean().reset_index()
sns.barplot(x="Rating",y="Price", data=avg_by_rating)
plt.title("Average price by rating")
plt.show()

# ----------------------------- Automated Excel Report (Optional) ----------------------------------

with pd.ExcelWriter("books_report.xlsx") as writer:
    df.to_excel(writer, sheet_name="All Books", index=False)
    top10.to_excel(writer, sheet_name="Top10 Expensive", index=False)
    avg_by_rating.to_excel(writer, sheet_name="Avg Price by Rating", index=False)


# --------------------------------------- 🚀 Practice Task --------------------------------------

# practice task are same as we did above
