use SalesDB
go

-- Basic GROUP BY

Select c.City, sum(s.Price * s.Quentity) as TotalRevenue  -- City-wise total revenue
from sale  s
join customers c on s.CustomerId = c.CustomerId
Group by c.City;

-- GROUP BY with HAVING
select c.City, sum(s.Price * s.Quentity) as TotalRevenue  -- Sirf un cities ko dikhana jaha revenue > 50000
from sale s
join customers c on s.CustomerId = c.CustomerId
Group by c.City
Having sum(s.Price * s.Quentity) > 40000; 

-- Window Function – ROW_NUMBER()

SELECT CustomerId, Product, Price,  -- Har customer ki purchases ko numbering karna
ROW_NUMBER() OVER(PARTITION BY CustomerID ORDER BY Price DESC) AS RowNum
FROM sale;

-- Window Function – RANK()

Select Product, sum(Price * Quentity) as TotalSales,  -- Top selling products by revenue
Rank() over(order by sum(Price * Quentity) desc) as SaleBank
from sale
Group by Product

-- Window Function – AVG() OVER()

SELECT Product, SUM(Price * Quentity) AS ProductSales,  -- Har product ke sales ke sath overall average bhi dikhana
AVG(SUM(Price * Quentity)) OVER() AS AvgSales
FROM Sales
GROUP BY Product;

