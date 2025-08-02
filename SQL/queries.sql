-- QUERY 1. TOTAL REVENUE PER CUSTOMER 

SELECT 
    "CustomerID", 
    ROUND(SUM("TotalPrice")::numeric, 2) AS total_revenue
FROM 
    transection
GROUP BY 
    "CustomerID"
ORDER BY 
    total_revenue DESC;


 --Query 2. MONTHLY REVENUE TREND 

SELECT DATE_TRUNC('month', "InvoiceDate"::timestamp) AS month, round(SUM("TotalPrice")::numeric,2) AS revenue
FROM transection
GROUP BY month
ORDER BY month;

-- Query 3. TOP 10 CUSTOMERS 

select "CustomerID" ,round(sum("TotalPrice")::numeric,2) as total_spent 
from transection
group by "CustomerID"
order by total_spent  DESC
limit 10


-- Query 4. AVERAGE ORDER VALUE 

SELECT round(AVG(order_total),2) AS average_order_value
FROM (
    SELECT "InvoiceNo", SUM("TotalPrice")::numeric AS order_total
    FROM transection
    GROUP BY "InvoiceNo"
) AS orders;

-- QUERY 5. FREQUENCY OF PURCHASE 
select "CustomerID", count( distinct"InvoiceNo") as Purchase_frequency
from transection
group by "CustomerID"
