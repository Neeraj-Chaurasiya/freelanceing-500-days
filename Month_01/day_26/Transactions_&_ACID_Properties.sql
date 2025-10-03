use SalesDB
go 

-- Start a Transaction

Begin Transaction;
 Insert into customers (Name,City) Values ('Ravi','Delhi');
 Insert into sale (Product, Category,Price, Quantity, CustomerId) Values
 ('Laptop','Electronics',55000, 1, 5);

 Commit;

 -- Rollback Example

 Begin Transaction;

 Update sale
 Set Price = Price * 0.5
 Where Product = 'Laptop';

 Rollback;
 
 -- Savepoint Example

 Begin transaction;

 Insert into customers (Name,City) values ('Priya','Mumbai')
 Save Transaction SavePoint1;
 
 Insert into customers (Name,City) values ('Amit','Kolkata');

 RollBack Transaction Savepoint1;
 Commit;

 -- Isolation Example (theory + check)

 Set Transaction Isolation Level Read Committed;
 Begin Transaction;
 Select * From sale Where  Product = 'Laptop';

 select * from sale