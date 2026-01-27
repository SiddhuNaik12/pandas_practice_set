import pandas as pd

#load data
df=pd.read_csv("set1_data.csv")
#convert order_date to datetime
df["order_date"]=pd.to_datetime(df["order_date"])
#Monthly total revenue
monthly_revenue = (
    df.groupby(df["order_date"].dt.to_period("M"))["order_amount"].sum()
)
print("Monthly Revenue:",monthly_revenue)
#uniue customers per month
unique_customers = (
    df.groupby(df["order_date"].dt.to_period("M"))["customer_id"].nunique()
)
print("unique customers per month",unique_customers)
#month with highest customers
highest_customer_month = unique_customers.idxmax()
print("\nMonth with highest unique customers:",highest_customer_month)
