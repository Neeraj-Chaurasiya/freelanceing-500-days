use SalesDB
go

-- Self JOIN

select c1.Name as Customer1, c2.Name as Customer2, c1.City   -- Customers table me self join (same city ke customers find karna)
from Customers c1 
join customers c2 on c1.City = c2.City and c1.CustomerId <> c2.CustomerId;

-- FULL OUTER JOIN

select c.Name,s.Product , s.Price   -- Sales aur Customers ka full outer join
from customers c
full outer join sale s on c.CustomerId  = s.CustomerId;


-- Nested Subqueries

select Name from customers   -- Customers who bought products above average price
where CustomerId in (
select CustomerId from sale
where Price > (select avg(Price) from sale)
);

-- Constraints Practice

Create table Employees (
EmpId int primary key identity(1,1),
Name nvarchar(50) not null, 
Email nvarchar(100)	Unique,
Age int check (age >= 18),
City nvarchar(50) default 'Unknown'
);

Insert into Employees (Name, Email, Age, City) Values
('Rohit','rohit@example.com',25,'Delhi');
