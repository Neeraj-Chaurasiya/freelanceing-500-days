use SalesDB
go

-- Views
-- City-wise revenue ka ek view 

CREATE VIEW CityRevenues as
select c.City, sum(s.Price * s.Quentity) as TotalRevenue
from sale s 
inner join customers c on c.CustomerId = s.CustomerId
Group by c.City;

select * from CityRevenues

-- Indexes

-- Customers table pe City column pe index
CREATE INDEX idx_city ON Customers(City);

-- Sales table pe Product column pe index
CREATE INDEX idx_product ON sale(Product);

-- Stored Procedures

-- Procedure to get top N products by revenue

-- Purana procedure delete karo pehle
DROP PROCEDURE IF EXISTS GetTopProducts;
GO

-- Naya procedure create karo
CREATE PROCEDURE GetTopProducts 
    @TopN INT
AS
BEGIN
    SELECT TOP (@TopN) Product, SUM(Price * Quentity) as TotalRevenue
    FROM sale
    GROUP BY Product
    ORDER BY TotalRevenue DESC;
END;
GO

-- Execute karo
EXEC GetTopProducts @TopN = 3;
