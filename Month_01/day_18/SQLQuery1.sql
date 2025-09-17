use SalesDB
go

select * from Sales

create table customers (
CustomerId int primary key identity(1,1),
Name nvarchar(50),
City nvarchar(50)
);

insert into customers (Name,City) values
('Amit','Delhi'),
('Neha','Mumbai'),
('Ravi','Kolkata'),
('Priya','Delhi'),
('Karan','Bangalore');


create table sale (
SaleID int primary key identity(1,1),
Product nvarchar(50),
Category nvarchar(50),
Price decimal(10,2),
Quentity int,
CustomerId int foreign key references customers(CustomerId)
);

insert into sale (Product, Category, Price, Quentity, CustomerId) values
('Laptop','Electronics',50000,1,1),
('Phone','Electronics',20000,2,2),
('Tablet','Electronics',15000,1,3),
('Headphones','Accessories',3000,3,1),
('Keyboard','Accessories',2000,2,4),
('Monitor','Electronics',12000,1,5),
('Mouse','Accessories',1000,5,2);

select * from sale

--INNER JOIN (matching data)

SELECT s.SaleID, c.Name, c.City, s.Product, s.Price, s.Quentity
FROM Sale s
INNER JOIN Customers c ON s.CustomerID = c.CustomerID;


 --LEFT JOIN

SELECT c.Name, c.City, s.Product, s.Price
FROM Customers c
LEFT JOIN Sale s ON c.CustomerID = s.CustomerID;

 --City-wise Revenue

SELECT c.City, SUM(s.Price * s.Quentity) AS TotalRevenue
FROM Customers c
INNER JOIN Sale s ON c.CustomerID = s.CustomerID
GROUP BY c.City;

 --Top 3 Products by Total Sales

SELECT TOP 3 s.Product, SUM(s.Price * s.Quentity) AS Revenue
FROM Sale s
GROUP BY s.Product
ORDER BY Revenue DESC;
