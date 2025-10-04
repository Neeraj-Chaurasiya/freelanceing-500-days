
# 📘 Day 27 – SQL Triggers (AFTER & INSTEAD OF)

---

## 🧠 Concept Overview

**Triggers** are special SQL procedures that automatically run (fire) when an event such as `INSERT`, `UPDATE`, or `DELETE` happens on a table.

Types of triggers:
- **AFTER Trigger** → Runs after the operation completes.
- **INSTEAD OF Trigger** → Replaces the original action with custom logic.

---

## 🏗️ Step 1: Select Database

```sql
use SalesDB
go
```
👉 It selects the `SalesDB` database where all operations will happen.

---

## 🧾 Step 2: Create Audit Table

```sql
Create table Sales_Audit (
    AuditId Int identity Primary key,
    Product nvarchar(50),
    OldPrice Decimal(10,2),
    NewPrice Decimal(10,2),
    Changedon DateTime Default GetDate()
);
```
👉 This creates a new table `Sales_Audit` to record price changes in the `sale` table.

- `AuditId` → Auto-incremented primary key.  
- `OldPrice` & `NewPrice` → Store previous and new prices.  
- `Changedon` → Automatically captures date and time of change.

---

## ⚙️ Step 3: AFTER UPDATE Trigger

```sql
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
```
👉 This trigger runs **after** any update on the `sale` table.

- `deleted` → Holds old rows before update.  
- `inserted` → Holds new rows after update.  
- We join both to record what changed.

💡 Example use case: Maintain a price change history log.

---

## 🧪 Step 4: Test AFTER Trigger

```sql
UPDATE sale
SET Price = Price + 5000
WHERE Product = 'Laptop';
```
👉 Increases the price of laptops by ₹5000.  
This automatically fires the trigger and logs data in `Sales_Audit`.

```sql
select * from Sales_Audit
```
👉 Shows the logged price changes (old and new values).

---

## ⚙️ Step 5: INSTEAD OF Trigger (Validation Example)

```sql
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
```
👉 This trigger replaces the default insert action.

- If someone tries to insert a record with `Name = NULL`, it raises an error and **rolls back** the transaction.
- Otherwise, the data gets successfully inserted into the `customers` table.

---

## 🧪 Step 6: Test INSTEAD OF Trigger

```sql
INSERT INTO Customers (Name, City) VALUES (NULL, 'Mumbai');
```
👉 This fails with error: `Customer name cannot be null`  
because of the validation check inside the trigger.

```sql
select * from customers
```
👉 Verify that invalid data was **not** inserted.

---

## ✅ Summary

| Trigger Type | Fires When | Use Case |
|---------------|-------------|-----------|
| AFTER Trigger | After INSERT/UPDATE/DELETE | Logging or auditing changes |
| INSTEAD OF Trigger | Instead of original action | Validation or conditional insertion |

💡 **Practical Use Cases**
- Maintain audit logs of data changes  
- Prevent invalid data entry  
- Automatically update related tables

---
