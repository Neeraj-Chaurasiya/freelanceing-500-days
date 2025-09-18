use SalesDB
go

-- Filtering Queries
-- Price 1000 aur 50000 ke beech

select * from sale
WHERE Price BETWEEN 1000 AND 40000;

-- Product Laptop ya Phone ho

select * from sale
where Product in ('Laptop','Phone');

-- Customer ka naam 'N' se start hota ho

select * from customers
where Name like 'N%';

-- Jinki sales NULL hai

select c.Name, s.Product  
from customers c 
left join sale s on c.customerId = s.customerId
where s.Product is null; 

-- Functions Practice
-- Customer name length

select Name, len(Name) as namelength from customers

-- Product ko uppercase

select Product, UPPER(Product) as PRODUCT from sale

-- Price round off

select Product, ROUND(Price, -2) as roundedprice from sale;

-- Current date & year

select GETDATE() as today, YEAR(GETDATE()) as yearnow;

-- ORDER BY multiple

select * from customers
order by City ASC, Name DESC;