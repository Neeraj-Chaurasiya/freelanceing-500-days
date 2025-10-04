use SalesDB
go 

-- Create Audit Table

Create table Sales_Audit (
	AuditId Int identity Primary key,
	Product nvarchar(50),
	OldPrice Decimal(10,2),
	NewPrice Decimal(10,2),
	Changedon DateTime Default GetDate()
);

-- AFTER UPDATE Trigger

Create Trigger trg_AfterPriceUpdate
on sale
After Update
As
Begin
	Insert into Sales_Audit (Product, OldPrice, NewPrice)
	Select d.Product, d.Price, i.Price
	From deleted d
	Join Inserted i on d.SaleID = i.SaleID;
End;

-- Test Trigger

UPDATE sale
SET Price = Price + 5000
WHERE Product = 'Laptop';

select * from Sales_Audit

-- INSTEAD OF Trigger (Validation Example)

CREATE TRIGGER trg_InsteadOfInsert	
ON customers
INSTEAD OF INSERT
AS
BEGIN
    IF EXISTS (SELECT * FROM inserted WHERE Name IS NULL)
    BEGIN
        -- Error message aur transaction abort
        RAISERROR ('Customer name cannot be null', 16, 1);
        ROLLBACK TRANSACTION;
        RETURN;
    END
    ELSE
    BEGIN
        INSERT INTO customers(Name, City)
        SELECT Name, City FROM inserted;
    END
END;
-- Test Trigger
INSERT INTO Customers (Name, City) VALUES (NULL, 'Mumbai');
select * from customers

