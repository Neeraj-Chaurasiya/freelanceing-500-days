CREATE DATABASE SalesDB;
go

use SalesDB;
go

CREATE TABLE Sales (
Id int primary key identity(1,1),
Product nvarchar(50),
Category nvarchar(50),
Price decimal(10,2),
Quentity int
);

insert into Sales(Product, Category,Price,Quentity)
values
('Laptop','Electronics',50000,2),
('Phone','Electronics',20000,5),
('Table','Electronics',15000,3),
('Headphone','Accessories',3000,10),
('Keyboard','Accessories',1500,7);


select * from Sales;

select *from Sales where Price > 20000;


select Category, SUM(Price * Quentity) as total_revenue from Sales group by Category;

-- Practice task

insert into Sales (Product, Category,Price,Quentity)
values
('Earphone','Electronics',35000,2),
('Earbuds','Electronics',65000,4),
('Speaker','Electronics',15000,4),
('Headphone','Accessories',4000,20),
('Keyboard','Accessories',2500,7),
('Speaker','Electronics',50000,6),
('Phone','Electronics',55000,3),
('Earphone','Electronics',25000,3),
('Earbuds','Accessories',5000,14),
('Keyboard','Accessories',12500,7);

select * from Sales

select * from Sales where Price > 30000;

select Category, sum(Price * Quentity) as total_sales from Sales group by Category;