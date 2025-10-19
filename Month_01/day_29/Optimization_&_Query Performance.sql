use SalesDB
go 

-- Enable Query Execution Plan

SET SHOWPLAN_ALL ON;
GO
SELECT * FROM sale WHERE Product = 'Laptop';
GO
SET SHOWPLAN_ALL OFF;

-- Check Query Execution Time

SET STATISTICS TIME ON;
SELECT * FROM sale WHERE Product = 'Laptop';
SET STATISTICS TIME OFF;

-- Create an Index (Performance Boost)

Create Index idex_Product on sale(Product);

-- Check Query Again (After Index)

Set Statistics Time on ;
Select * From sale where Product = 'Laptop';
Set Statistics Time off;

-- Composite Index (Multi-column)
Create Index indx_category_product on sale(Product, Category);

-- Drop Unused Index

Drop Index indx_category_Product on sale;

-- Compare Join v/s Subquery performance 


Set Statistics Time on;
go
   -- using join
Select c.Name, SUM(s.Price * s.Quantity) as Total
From sale s 
join customers c on c.CustomerId = s.CustomerId
Group by c.Name

   -- using subquery
Select Name,
	(Select SUM(Price * Quantity)
	From sale s
	Where s.CustomerId = c.CustomerId) as Total 
From customers c; 

go
Set Statistics Time off;