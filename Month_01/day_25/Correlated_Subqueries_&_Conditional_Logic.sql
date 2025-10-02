use SalesDB
go

-- Correlated Subquery – Price above average

Select Product, Price
From sale s
Where Price > (
	Select Avg(Price)
	From sale
	Where Category = s.Category
);

select Category, avg(Price) as AvgCategory from sale  -- Average Category
group by Category 

-- Correlated Subquery – Customers with more than 1 purchase

Select c.Name, c.City
From customers c
Where 1 < (
	Select count(*)
	From sale s 
	where c.CustomerId = s.CustomerId
);

-- CASE WHEN – Categorize Products by Price

Select	Product, Price,
	Case 
		When Price < 10000 Then 'Budget'
		When Price Between 10000 and 40000 Then 'Mid-Range'
		Else  'Premium'
	End As PriceCategory
From sale;

-- CASE WHEN with Aggregation – City Revenue Category

Select c.City,
	Sum(s.Price * s.Quantity) As TotalRevenue,
	Case
		When Sum(s.Price * s.Quantity) > 10000 Then 'High revenue'
		When Sum(s.Price * s.Quantity) Between 50000 And 100000 Then 'Medium Revenue'
		Else 'Low Revenue'
	End as RevenueCategory
From sale s 
Join customers c on s.CustomerId = c.CustomerId
Group by c.City;
