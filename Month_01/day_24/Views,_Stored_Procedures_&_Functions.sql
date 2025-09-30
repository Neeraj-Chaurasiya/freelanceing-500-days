use SalesDB
go

-- Non-recursive CTE: City-wise revenue (CTE + filter)

With CityRevenue As 
(Select c.City,
Sum(s.Price * s.Quantity) as TotalRevenue
from sale s
join customers c On c.CustomerId = s.CustomerId
Group by c.City
)
Select City, TotalRevenue 
From CityRevenue
Where TotalRevenue > 40000
Order by TotalRevenue DESC;

-- Same result using derived subquery (for comparison)

Select City, TotalRevenue
From
(Select c.City, Sum(s.Price * s.Quantity) as TotalRevenue
from sale s
join customers c on s.CustomerId = c.CustomerId
Group by c.City
) As t
Where TotalRevenue > 40000
Order by TotalRevenue DESC; 

-- Recursive CTE: Generate numbers 1..10

With Number As
(Select 1 As n
Union All
Select n + 1 From Number
Where n < 10
)
Select n From Number
Option (Maxrecursion 0)

-- CTE + Window Function (ranking products)

With  ProdSales As
( Select Product, Sum(Price * Quantity) as Revenue
From sale
Group by Product
)
Select Product,Revenue,
Rank() Over (Order by Revenue DESC) as SaleRank
From ProdSales;

-- Temp table (SELECT INTO) — create & use

-- EXEC sp_rename 'sale.Quentity', 'Quantity', 'COLUMN';
Select TOP 5 Product, Sum(Price * Quantity) AS Revenue	 -- Create temp table and insert top 5 products into it
Into #TopProducts
From sale
Group by Product
Order by Revenue DESC;

Select * From #TopProducts  -- Check temp table

Select s.*  -- Example use: join back to Sales to see rows for top products
From sale s
join #TopProducts  t on s.Product = t.Product

-- Update using temp table (example)

UPDATE sale
SET Price = Price * 0.95
WHERE Product = 'Laptop';

-- Verify
SELECT * FROM sale WHERE Product = 'Laptop';

-- Drop temp table (optional)

DROP TABLE #TopProducts;   -- optional; otherwise session end pe auto drop