import pandas as pd 

df = pd.read_csv(r"C:\Freelanceing (500 days)\Month_02\day_48\Data\ecommerce_sales_34500.csv")

df['order_date'] = pd.to_datetime(df['order_date'])

df['final_amount'] = df['price']*df['quantity']*(1-df['discount'])

summary = df.groupby('region')['final_amount'].sum().reset_index()
print(summary)

df.to_csv(r"C:\Freelanceing (500 days)\Month_02\day_48\Data\processed_sales.csv", index=False)
summary.to_csv(r"C:\Freelanceing (500 days)\Month_02\day_48\Data\sales_summary_by_region.csv", index=False)
print("Data processing complete. Processed files saved.")
