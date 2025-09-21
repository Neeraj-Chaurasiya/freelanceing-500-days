use SalesDB
go

-- Aggregate Functions :-

-- 1. Total sales amount

select sum(Price * Quentity) as TotalRevenue from sale

--2.  Average product price

select avg(Price) as AveragePrice from sale

--3. Number of customers

select count(*) as TotalCustomers from customers;

--4. Min & Max Price

select min(Price) as MinPrice, max(Price) as MaxPrice from sale 

-- GROUP BY with HAVING

-- City with revenue > 50000

select c.City, sum(Price * Quentity) as TotalRevenue	
from sale s
inner join  customers c on s.CustomerId = c.CustomerId
group by c.City
Having sum(s.Price * s.Quentity) > 50000;

-- City-wise total revenue

select c.City, sum(Price * Quentity) as TotalRevenue
from sale s
inner join customers c on s.CustomerId  = c.CustomerId
group by c.City

-- Subqueries

-- Products priced above average price

select Product, Price
from sale
where Price > (select avg(Price) from sale)

-- Customers who purchased Laptop

select Name
from customers
where CustomerId in (
select CustomerId from sale where Product = 'Laptop'
)