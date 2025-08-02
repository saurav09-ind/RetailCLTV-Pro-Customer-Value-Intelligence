

-- for crating transection table 
create table transection as 
select * from retail_cleaned ;

-- for creating customers table 
CREATE TABLE customers AS
SELECT DISTINCT "CustomerID", "Country"
FROM retail_cleaned
WHERE "CustomerID" IS NOT NULL

-- for creating product table 
create table product as 
select distinct "StockCode", "Description", "UnitPrice"
from retail_cleaned
