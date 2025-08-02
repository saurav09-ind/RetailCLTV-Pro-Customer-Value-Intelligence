from sqlalchemy import create_engine
import pandas as pd 

engine = create_engine('postgresql://postgres:1234@localhost:5432/CLTV_db')
df = pd.read_csv('D:\\Python basics\\CLTV-360\\Notebook\\Cleaned_online_retail.csv')

output_dir ="D:\\Python basics\\CLTV-360\\CSV files"

# Query 1: Total Revenue per Customer
query1= """
SELECT 
    "CustomerID", 
    ROUND(SUM("TotalPrice")::numeric, 2) AS total_revenue
FROM 
    transection
GROUP BY 
    "CustomerID"
ORDER BY 
    total_revenue DESC;
    """

df1 = pd.read_sql ( query1,con= engine)
df1.to_csv(output_dir + "\\Customer_revenue.csv", index=False)

# Query 2: Monthly Revenue Trend

query2 = """
SELECT DATE_TRUNC('month', "InvoiceDate"::timestamp) AS month, round(SUM("TotalPrice")::numeric,2) AS revenue
FROM transection
GROUP BY month
ORDER BY month;
"""
df2 = pd.read_sql ( query2, con= engine)
df2.to_csv(output_dir + "\\Monthly_revenue.csv", index=False)

# Query 3: Top 10 Customers
query3 = """
select "CustomerID" ,round(sum("TotalPrice")::numeric,2) as total_spent 
from transection
group by "CustomerID"
order by total_spent  DESC
limit 10
"""
df3 = pd.read_sql ( query3, con= engine)
df3.to_csv( output_dir + "\\top_10_customer.csv",index= False)


# Query 4 : Average order value 
query4 = """
SELECT round(AVG(order_total),2) AS average_order_value
FROM (
    SELECT "InvoiceNo", SUM("TotalPrice")::numeric AS order_total
    FROM transection
    GROUP BY "InvoiceNo"
) AS orders;
"""
df4 = pd.read_sql ( query4, con= engine)
df4.to_csv( output_dir + "//Avg_order_value.csv",index=False)

# Query 5: Frequency of Purchase
query5 = """
select "CustomerID", count( distinct"InvoiceNo") as Purchase_frequency
from transection
group by "CustomerID"
"""
df5 = pd.read_sql ( query5, con= engine)
df5.to_csv ( output_dir + "//Freq_of_purchas.csv",index= False)

